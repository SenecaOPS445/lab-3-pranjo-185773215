#!/usr/bin/env python3
'''Description: Learning functions with arguments'''

def square(number):
    return number ** 2

print(square(5))
print(square(10))
print(square(12))
print(square(square(2)))
#print(square('2')) # Produces an error as the argument is a string and not a integer

def sum_numbers(number1, number2):
    return int(number1) + int(number2)

sum_numbers(5, 10)
sum_numbers(50, 100)
print(square(sum_numbers(5, 5)))