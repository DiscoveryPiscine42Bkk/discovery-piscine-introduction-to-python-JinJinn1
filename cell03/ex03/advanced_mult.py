#!/usr/bin/env python
#Super Messy Code

number = 0
inner_number = 0
round = 0

while number <= 10:

    inner_number = 0
    print(f"Table de {number}:", end=" ")
    
    while round <= 10:
        print(inner_number, end=" ")
        inner_number += 0 + number
        round += 1
    
    number += 1
    round = 0
    print("")