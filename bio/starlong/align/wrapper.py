__author__ = "John Hover"
__copyright__ = "Copyright 2021, John Hover"
__email__ = "jhover@pobox.com, hover@cshl.edu"
__license__ = "MIT"

import os
from snakemake.shell import shell

print('in STARlong wrapper...')
extra = snakemake.params.get("extra", "")
log = snakemake.log_fmt_shell(stdout=True, stderr=True, append=True)
fq1 = snakemake.input.get("fq1")

#fq1 = (
#    [snakemake.input.fq1]
#    if isinstance(snakemake.input.fq1, str)
#    else snakemake.input.fq1
#)

if fq1.endswith(".gz"):
    readcmd = "--readFilesCommand zcat"
else:
    readcmd = ""

print(f"fq1 is {fq1}")
print(f"snakemake.output is {snakemake.output}")
print(f"snakemake.params.outprefix is {snakemake.params.outprefix}")

shell(
    "STARlong "
    "{extra} "
    "--runThreadN {snakemake.threads} "
    "--outFileNamePrefix {snakemake.params.outprefix} "
    "--genomeDir {snakemake.params.index} "
    "--twopassMode Basic " 
    "--twopass1readsN -1 " 
    "--outSAMtype BAM Unsorted "  
    "--quantMode GeneCounts " 
    "--readFilesIn {snakemake.input.fq1} "
    "{readcmd} "
    "--outStd Log "
    "{log}"
)
