#!/bin/python

from sys import argv, exit
from pathlib import Path
from subprocess import run
if len(argv) != 2:
        sys.exit(99)
p = Path(argv[1])
pictures = [x for x in p.iterdir() if x.is_file()]
already_conv = [x for x in pictures if 'sw' not in x.name and (x.stem+ "_sw" + x.suffixes[0]) not in [y.name for y in pictures]]
for img in already_conv:
    run(['convert', str(img), '-set', 'colorspace', 'Gray', '-seperate', 'average', str(img.parents[0]) + "/" +img.stem + "_sw" + img.suffixes[0]])
