#!/usr/bin/env python3

def gross_pay(work_hours,work_rate):
    return work_rate * work_hours

def main():

    work_hours = float(input("Please enter Hours: "))
    work_rate = float(input("Please input Rate: "))

    print(str(gross_pay(work_hours,work_rate)))


main()
