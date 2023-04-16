#!/usr/bin/env python3

def main():
    file_handle = open('mbox-short.txt')
    count = 0
    for line in file_handle:
        count += 1
    print('Line Count:', count)

main()
