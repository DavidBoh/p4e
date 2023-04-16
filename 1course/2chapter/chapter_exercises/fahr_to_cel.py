#!/usr/bin/env python3

def convert_temperature(celsius):
    result = (celsius * 9/5) + 32
    return result

def main():
    print("Celsius to Fahr converter")
    celsius = input("Please input value in Celsius: ")
    celsius = int(celsius)

    fahr = convert_temperature(celsius)
    print("{} degrees celsius = {} degrees Fahrenheit " \
          .format(str(celsius),str(fahr)))



main()
