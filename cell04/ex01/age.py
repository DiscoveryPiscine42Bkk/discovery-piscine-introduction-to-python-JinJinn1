#!/usr/bin/env python

age = int(input("Please tell me your age:" ))
print(f"You are currently {age} years old.")
counter = 10

while counter <= 30:
    age += 10
    print(f"In {counter} years, you'll be {age} years old.")
    counter += 10