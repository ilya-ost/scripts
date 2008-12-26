#!/usr/bin/env python2.5

from __future__ import with_statement
import sys
import os
import shutil
import re

if len(sys.argv) == 2:
    org_file_name = sys.argv[1]
else:
    print 'usage: org-table2latex.py filename'
    exit(1)

heading_re = re.compile(r'^\* ')
delim_re = re.compile(r'^\|-')
item_re = re.compile(r'\|[^|]+')

org_file = open(org_file_name, 'r')
tex_file_name = org_file_name.replace('.org', '.tex')
preamble_file_name = os.path.expanduser('~/src/LaTeX/refcards/preamble.tex')
shutil.copy(preamble_file_name, tex_file_name)
tex_file = open(tex_file_name, 'a')

tex_file.write("\\begin{document}\n")
new_table = True
org_iter = org_file.xreadlines()

def latex_escape(str):
    l_re = re.compile(r"([`&$%^#_{}])")
    l_bs_re = re.compile(r"\\")
    l_bs1_re = re.compile(r"\textbackslash")
    l_str = l_bs_re.sub(r"\textbackslash", str)
    l_str = l_re.sub(r"\\\1{}", l_str)
    l_str = l_bs1_re.sub(r"\\textbackslash{}", l_str)
    return l_str

for line in (l.strip() for l in org_iter if len(l.strip()) > 0):
    if heading_re.search(line):
        heading = heading_re.sub('', line).strip()
        new_table = True
        print "\nheading: ", heading
    elif delim_re.search(line):
        if new_table:
            tex_file.write("\\begin{mykeys}{%s}\n" % heading)
            line = org_iter.next().strip()
            format = [line[m.start()+1:m.end()-1].strip() for m in item_re.finditer(line)]
        else:
            tex_file.write("\\end{mykeys}\n")
        new_table = not new_table
        print "format: ", format
    else:
        items = [latex_escape(line[m.start()+1:m.end()-1].strip()) for m in item_re.finditer(line)]
        tex_file.write("\\keydescr{%s}{%s}\n" % (items[0], items[1]))
        print items[0], items[1]
            
tex_file.write("\\end{document}")
