#!/usr/bin/env python

user_input = int(input("Input a number: "))
table = -1

while table <= 8:
    table += 1
    result = table * user_input
    print(f"{table} x {user_input} = {result}")