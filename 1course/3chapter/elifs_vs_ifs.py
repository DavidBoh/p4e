#!/usr/bin/env python3

def correct_logic(flag):

    print("executing correct logic")
    if flag == 'p':
        print("your input was {} everything OK".format(flag))
    elif flag == 's': 
        print("your input was {} everything OK".format(flag))
    elif flag == 'c':
        print("your input was {} everything OK".format(flag))
    else:
        print("your input was not p, s, nor c")
    # These if, elifs and else work together. Else will NEVER RUN if one them is found to
    # be True

def wrong_logic(flag):
    
    print("executing wrong logic")

    ########### These IF statements run independently
    if flag == 'p':
        print("your input was {}".format(flag))
    if flag == 's': #when program finds 'p' to be True, this if block is skipped \
            # not evaluated
        print("your input was {}".format(flag))
    ########### Else block at the botton will ALWAYS RUN regardless of the outcome of these

    ############# This IF statement works with the subsequent ELSE statement
    if flag == 'c': 
        print("your input was {}".format(flag))
    else:
        print("this ELSE block should've only executed if your input was c or\n \
                something other than p or s")
        print("wrong input")
    ############### Else block will NEVER RUN if program finds that flag = 'c'
def main():
    
    print("Please input 1 for program with correct logic")
    print("Please input 2 for program with incorrect logic")
    program_option = input()

    flag = input("Please input the letters p, s, or c: ")

    if program_option == "1":
        correct_logic(flag)
    elif program_option == "2":
        wrong_logic(flag)
    
main()
