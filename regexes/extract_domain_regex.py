#!/usr/bin/env python3

import re

data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'

y = re.findall('@([^ ]*)',data)
print(y)

