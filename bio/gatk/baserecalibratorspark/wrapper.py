__author__ = "Christopher Schröder"
__copyright__ = "Copyright 2020, Christopher Schröder"
__email__ = "christopher.schroeder@tu-dortmund.de"
__license__ = "MIT"

import tempfile

from snakemake.shell import shell
from snakemake_wrapper_utils.java import get_java_opts

extra = snakemake.params.get("extra", "")
spark_runner = snakemake.params.get("spark_runner", "LOCAL")
spark_master = snakemake.params.get(
    "spark_master", "local[{}]".format(snakemake.threads)
)
spark_extra = snakemake.params.get("spark_extra", "")
java_opts = get_java_opts(snakemake)

tmpdir = tempfile.gettempdir()

log = snakemake.log_fmt_shell(stdout=True, stderr=True)
known = snakemake.input.get("known", "")
if known:
    known = "--known-sites {}".format(known)

shell(
    "gatk --java-options '{java_opts}' BaseRecalibratorSpark {extra} "
    "-R {snakemake.input.ref} -I {snakemake.input.bam} "
    "--output {snakemake.output.recal_table} {known} "
    "--tmp-dir {tmpdir} "
    "-- --spark-runner {spark_runner} --spark-master {spark_master} {spark_extra} "
    "{log}"
)
