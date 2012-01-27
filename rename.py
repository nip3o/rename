#!/usr/bin/env python
from argparse import RawTextHelpFormatter

import os, re
import sys
import argparse

parser = argparse.ArgumentParser(description="""
Rename is a tool for batch-renaming files matching a regular expression, replacing with a replacement pattern. Capturing groups can be referenced in the replacement pattern as \N, where N is the number of the group starting with 1.\n

Example:
replace "foo(\d).bar" "\1bar.foo"
foo1.bar -> 1bar.foo
foo2.bar -> 2bar.foo
foo3.bar -> 3bar.foo
""", formatter_class=RawTextHelpFormatter)

parser.add_argument('pattern', help='regex pattern to search for')
parser.add_argument('replacement', help='new format to replace with')
parser.add_argument('-d', '--dry-run', dest='dryrun', help="don't rename anything, just show what whould be renamed", action='store_true')   

args = parser.parse_args()
match = False

for filename in os.listdir(os.getcwd()):
	if re.search(args.pattern, filename):
		new = re.sub(args.pattern, args.replacement, filename)
		match = True

		print "%s -> %s" % (filename, new)

		if not args.dryrun:
			os.rename(filename, new)

if not match:
	print "No files matched the pattern."