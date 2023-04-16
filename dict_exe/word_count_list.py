#!/usr/bin/env python3

def main():
    word = 'brontosaurus'
    d = dict()
    #for count in word:
    #    if count not in d:
    #        d[count] = 1
    #    else:
    #        d[count] = d[count] + 1

    for c in word:
        d[c] = d.get(c,0) + 1
    print(d)
main()
