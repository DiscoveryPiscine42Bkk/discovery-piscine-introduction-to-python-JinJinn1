#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    word = sys.argv[1]
    word_search = sys.argv[2]

    matches = re.findall(re.escape(word), word_search)

    if matches:
        print(len(matches))
    else:
        print("none")