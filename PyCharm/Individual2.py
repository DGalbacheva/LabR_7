#!usr/bi/env python3
# -*- coding utf-8 -*-

import sys

if __name__ == '__main__':
    a = list(map(int, input("Введите элементы в списке: ").split()))
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    max_num = max(a)
    print("Максимальный элемент в списке: ", max_num)

    a_min = a_max = 0
    for a_min, v in enumerate(a):
        if v > 0:
            break
    for a_max, v in enumerate(reversed(a)):
        if v > 0:
            break
    s = sum(a[a_min+1: -a_max-1])
    print("Сумма элементов списка, расположенных между ", "\n",
          "первым и последним положительным элементами: ", s)

