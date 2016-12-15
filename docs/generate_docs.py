import os
from jinja2 import Template
import yaml


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WRAPPER_DIR = os.path.dirname(BASE_DIR)
OUTPUT_DIR = os.path.join(BASE_DIR, "wrappers")
SCRIPTS = {"wrapper.py", "wrapper.R"}
BLACKLIST = {"docs", "environment.yaml", ".git", ".gitignore", "README.md"} | SCRIPTS

with open(os.path.join(BASE_DIR, "_templates", "tool.rst")) as f:
    TOOL_TEMPLATE = Template(f.read())

with open(os.path.join(BASE_DIR, "_templates", "wrapper.rst")) as f:
    TEMPLATE = Template(f.read())


def get_tool_dir(tool):
    outdir = os.path.join(OUTPUT_DIR, tool)
    os.makedirs(outdir, exist_ok=True)
    return outdir


def render_tool(tool, subcmds):
   with open(os.path.join(get_tool_dir(tool) + ".rst"), "w") as f:
       f.write(TOOL_TEMPLATE.render(name=tool, subcmds=subcmds))


def render_wrapper(path, target):
    print("rendering", path)
    with open(os.path.join(path, "meta.yaml")) as meta:
        meta = yaml.load(meta)
    with open(os.path.join(path, "environment.yaml")) as env:
        env = yaml.load(env)
        pkgs = env["dependencies"]
    with open(os.path.join(path, "Snakefile")) as snakefile:
        snakefile = snakefile.read()
    name = meta["name"].replace(" ", "_") + ".rst"
    with open(target, "w") as readme:
        rst = TEMPLATE.render(snakefile=snakefile, pkgs=pkgs, **meta)
        readme.write(rst)
    return name


def setup(*args):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for discipline in os.listdir(WRAPPER_DIR):
        if discipline in BLACKLIST:
            continue
        for tool in os.listdir(os.path.join(WRAPPER_DIR, discipline)):
            path = os.path.join(WRAPPER_DIR, discipline, tool)
            if any(f in SCRIPTS for f in os.listdir(path)):
                render_wrapper(path, os.path.join(OUTPUT_DIR, tool + ".rst"))
                continue
            subcmds = list(os.listdir(path))
            for subcommand in subcmds:
                render_wrapper(os.path.join(path, subcommand), os.path.join(get_tool_dir(tool), subcommand + ".rst"))
            render_tool(tool, subcmds)


if __name__ == '__main__':
    setup()
