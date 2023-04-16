#!/usr/bin/env python3

def word_count():
    try:
        name = input('Enter file: ')
        handle = open(name, 'r')
        counts = dict()
    except:
        print("Error, invalid file name or file not found")

    for line in handle:
        words = line.split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1

    bigcount = None
    bigword = None

    for word, count in list(counts.items()):
        if bigcount is None or count > bigcount:
            bigword = word
            bigcount = count

    print(bigword, bigcount)

def main():
    word_count()

main()
