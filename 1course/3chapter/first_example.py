#!/usr/bin/env python3

def tasks(x):
    if x > 2:
        print('Bigger than 2')
        print('Still bigger')
    print('Done with 2')
    print('_______________')

    for i in range(5):
        if i > 2: 
            print('{} is bigger than 2'.format(i))
        print('Done with i = ', i)
    print('All done')

def main():
    x = 5
    tasks(x)

main()
