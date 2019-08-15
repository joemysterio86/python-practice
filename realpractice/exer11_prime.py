#!/usr/bin/env python3

num = input("Please enter a number to determine if it's a prime number.\n\n")

def primeCheck():
    if int(num) % 2 == 0:
        print("The number " + num + " is not a prime number.")
    else:
        print("The number " + num + " is a prime number!")

primeCheck()