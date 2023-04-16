#!/usr/bin/env python3

import re
x = 'From: Using the: character'
y = re.findall('^F.+:',x)
print(y)

