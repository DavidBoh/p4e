#!/usr/bin/env python3
import  re 
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+',x) # without the +, prints indivitul digits
print(y)

