#!/usr/bin/env python3
"""
the .find() function returns the NUMBER where the string passed is located. For example if we create the variable my_string = "this is america" if we do my_string.find("am"), 8 will be returned, because "am" is found in that string in the index 8. If we said my_string.find("x") the number -1 will be returned. This is why Dr. Chuck is using that comparison linefind('From: ') >= 0, because if From is not found on that line, -1 will be returned, the line will be skipped, and the loop will continue to the next line
"""


hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip() #remember strip, rstrip, lstrip remove white space. "split" turns into dict. 
    if line.find('From: ') >= 0:
        print(line)



