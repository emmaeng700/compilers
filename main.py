import sys, os, re

# expected form of a C program without line breaks
source_re = r"int main\s*\(\s*\)\s*{\s*return\s+(?P<ret>[0-9]+)\s*;\s*}"

assemly_form = """
    .global _main
_main:
    movl     ${}, %eax
    retq
"""

source_file = sys.argv[1]
print(source_file)
assemly_file = os.path.splitext(source_file)[0] + ".s"
print(assemly_file)

with open(source_file, "r") as infile, open(assemly_file, "w") as outfile:
    source = infile.read().strip()
    match = re.match(source_re, source)

    # extract the named "retq" group, containing the return value
    retqval = match.group("ret")
    outfile.write(assemly_form.format(retqval))