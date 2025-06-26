#!/usr/bin/env python3

number_array = [2,8,9,48,8,22,-12,2]
final_set = set()

for i in number_array:
    if i > 5:
        final_set.add(i+2)

print(f"Original Array: {number_array}")
print(f"Output: {final_set}")