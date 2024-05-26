#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
        print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [x ** 2 for x in int_list]

def fizzbuzz():
    # code goes here!
    for num in range (1, 101):
        result = ""
        if num % 3 == 0:
            result += "Fizz"
        if num % 5 == 0:
            result += "Buzz"
        print (result or num)
