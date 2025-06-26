#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) != 2:
    print("none")
else:
    start = int(args[0])
    end = int(args[1]) + 1  
    numbers = list(range(start, end))
    print(numbers)
