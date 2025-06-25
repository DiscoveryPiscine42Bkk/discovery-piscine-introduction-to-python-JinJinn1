#!/usr/bin/env python

give_number = input("Give me a number: ")
answer = ''
final_value = float(give_number)

if final_value.is_integer():
    answer = 'n integer'
else:
    answer = ' float'


print(f"This number is a{answer}")