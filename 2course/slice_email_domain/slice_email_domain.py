#!/usr/bin/env python3

def find_slice():
    email_meta = "From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008"
    at_position = email_meta.find('@')
    print(email_meta)
    space_position = email_meta.find(' ',at_position)

    host = email_meta[at_position+1 : space_position]
    
    print("Sliced domain: {}".format(host))

def main():
    find_slice()
main()
