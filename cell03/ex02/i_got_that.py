#!/usr/bin/env python

user_input = input("What you gotta say?: ")

while user_input:
    if user_input == "STOP":
        break
    else:
        user_input = input("I got that! Anything else: ")