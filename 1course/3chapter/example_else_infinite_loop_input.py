#!/usr/bin/env python3

def compare_nums(my_num):
    if my_num > 10:
        print("{} is bigger than 10".format(my_num))
    else:
        print("{} is smaller than 10".format(my_num))

def main():
    
    #User input infinite loop
    while True:
        x = input("Please input a number: ")
        try:
            x = int(x)
            break
        except:
            print("You did not input a valid number, please try again")
            continue
    
    compare_nums(x)
    #Variable x WAS BEING PASSED AS STR BECAUSE I DID NOT write X = INT X line

main()
