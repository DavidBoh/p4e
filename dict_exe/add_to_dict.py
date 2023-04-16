#!/usr/bin/env python3

def main():
    blog = {'Website':'Journaldev', 'tutorial':'Append to Python dictionary'}
    print("Here are the current details: ", blog)
    
    # Adding the author details to the dictionary
    blog.update({'Author':'Pankaj Kumar'})
    print("Updated dictionary is: ", blog)
    
    # Appending another dictionary
    guests = {'Guest1':'Meghna'}
    blog.update(guests)
    print("Updated dictionary is: ", blog)

main()
