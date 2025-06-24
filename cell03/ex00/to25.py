#!/usr/bin/env python

user_input = int(input("Enter a number: "))
number = 0

if user_input <= 25:
    while user_input <= 25:
        print(f"Inside the loop, my variable is {user_input}")
        user_input += 1
        if user_input > 25:
            break
    
elif user_input > 25:
    print("Error")