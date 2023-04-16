#!/usr/bin/env python3

def tasks(x):

    print("Nested decisions demonstration")
    if x > 1:
        print('{} is more than 1'.format(x))
        if x < 100:
            print('{} is less than 100'.format(x))
    print("End of programme")

def main():
    x = 42
    tasks(x)

main()
