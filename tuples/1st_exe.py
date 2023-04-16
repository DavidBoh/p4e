#!/usr/bin/env python3

import re

file_name = str(input("Enter a file name: "))

try:
    file_handler = open(file_name)
except:
    print("File not found")


my_dict = dict()
counter = list()

for line in file_handler:
    line = line.lower()
    words = line.strip()
    extracted = re.findall('^From: (\S+@\S+)',words)

    for word in words:
        if word not in counter:
            counter[words] = 1
        else:
            counter[words] += 1

    my_dict[]


