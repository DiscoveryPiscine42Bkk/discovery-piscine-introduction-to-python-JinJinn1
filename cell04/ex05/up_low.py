#!/usr/bin/env python3

string = input("Insert a string: ")
new_string = ''

for i in string:
    if i.isupper():
        new_string += i.lower()
    elif i.islower():
        new_string += i.upper()
    else:
        new_string += i


print(new_string)