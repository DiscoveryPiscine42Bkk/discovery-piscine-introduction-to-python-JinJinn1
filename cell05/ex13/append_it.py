#!/usr/bin/env python3
import sys

args = sys.argv[1:]
output_found = False

for word in args:
    if not word.endswith("ism"):
        print(word + "ism")
        output_found = True

if not args or not output_found:
    print("none")