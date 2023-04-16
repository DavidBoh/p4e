#!/usr/bin/env python3
"""
"""

import re

hand = open('mbox-short.txt')


for line in hand:
    line = line.rstrip()
    y = re.findall('^From (\S+@\S+)', line)
    if not y:
        continue
    print(y)

