#!/usr/bin/env python

enter_first = input("Enter the first number: ")
enter_second = input("Enter the second number: ")

result = int(enter_first)*int(enter_second)
symbol = '' 

if result > 0:
    symbol = "positive"
elif result < 0:
    symbol = "negative"
elif result == 0:
    symbol = "positive and negative"


print(f"{enter_first}" + " x " + f"{enter_second}" + " = " + f"{result}")
print(f"The result is {symbol}.")

