#!usr/bi/env python3
# -*- coding utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввести список одной строкой
    a = list(map(int, input().split()))
    a1 = []
    s = 0
    for i, v in enumerate(a):
        if v == 0:
            a1.append(i)
            s +=1
    print(f"В списке 0 встреаетс: {s} раза")
    print("Их индекси: ", *a1)
