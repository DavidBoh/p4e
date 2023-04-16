#!/usr/bin/env python3
import re

file_handler = open('mbox-short.txt')

numlist = list()

for line in file_handler:
    line = line.rstrip()
    extracted_stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(extracted_stuff) is not 1:
        continue

    print(extracted_stuff)    
    num = float(extracted_stuff[0])
    numlist.append(num)

print('Maximum: ', max(numlist))
#max() finds the largest number in an iterable

