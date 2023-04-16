#!/usr/bin/env python3

def main():
    word = 'banana'
    count = 0
    for index in word:
        if index == 'a':
            count += 1

    print("The word {} has {} a's".format(word,str(count)))

main()
