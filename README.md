[![Snakemake](https://img.shields.io/badge/snakemake-≥3.6.0-brightgreen.svg?style=flat-square)](https://bitbucket.org/johanneskoester/snakemake)

# The Snakemake Wrapper Repository

The Snakemake Wrapper Repository is a collection of reusable wrappers that allow to quickly use popular command line tools 
from [Snakemake](https://bitbucket.org/johanneskoester/snakemake) rules and workflows.

## Structure

Wrappers can be found under

```
<discipline>/<name>/
```

in this repository.
The general strategy is to include these into your workflow via the [wrapper](https://bitbucket.org/snakemake/snakemake/wiki/Documentation#markdown-header-external-wrapper) directive, e.g.
```
#!python

rule samtools_sort:
    input:
        "mapped/{sample}.bam"
    output:
        "mapped/{sample}.sorted.bam"
    params:
        "-m 4G"
    threads: 8
    wrapper:
        "0.0.8/bio/samtools_sort"
```
Here, Snakemake will automatically download the corresponding wrapper from https://bitbucket.org/snakemake/snakemake-wrappers/src/0.0.8/bio/samtools_sort/wrapper.py. Thereby, 0.0.8 can be replaced with the version tag you want to use, or a commit id (see [here](https://bitbucket.org/snakemake/snakemake-wrappers/commits/)). This ensures reproducibility since changes in the wrapper implementation won't be propagated automatically to your workflow.
Examples for each wrapper can be found in the READMEs located in the wrapper subdirectories.

## Contribute

We invite anybody to contribute to the Snakemake Workflow Repository.
If you want to contribute we suggest the following procedure:

* fork the repository
* develop your contribution
* perform a pull request

The pull request will be reviewed and included as fast as possible.
Thereby, contributions should follow the coding style of the already present examples, i.e.

* provide a README.md describing the usage and purpose,
* define author with email address and a license,
* follow the python [style guide](http://legacy.python.org/dev/peps/pep-0008),
* use 4 spaces for indentation.