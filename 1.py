#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    import sys
a = tuple(map(float, input().split()))

if len(a) != 10:
    print("Неверный размер списка", file=sys.stderr)
    exit(1)

a_fil = tuple()

for elem in a:
    if elem > 8 and elem < 18 and elem % 10 == 0:
        a_fil += tuple([elem])
if len(a_fil) == 0:
    print(0)
else:
    res = 1
    for elem in a_fil:
        res *= elem

print(res)