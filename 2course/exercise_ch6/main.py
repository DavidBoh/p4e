#!/usr/bin/env python3

def util():
    def dry():
        print("Current type: ")
        print(type(my_float))
        print(my_float)
        print("")
    my_str = 'X-DSPAM-Confidence:0.8475'
    
    colon_position = my_str.find(":")
    my_float = my_str[colon_position + 1:]
    dry()
    my_float = float(my_float)
    dry()

def main():
    util()
main()
