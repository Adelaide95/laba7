#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = tuple(map(float, input().split()))
    C = float(input())
count = 0
for elem in a:
    if elem > C:
        count += 1

print("Количество чисел больших С:", count)

max_elem = 0
for i, item in enumerate(a):
    elem_abs = abs(item)
    if elem_abs > max_elem:
        max_elem, max_elem_ind = elem_abs, i

if max_elem_ind == len(a) - 1:
    print(0)
else:
    res = 1
    for elem in a[max_elem_ind + 1:len(a)]:
        res *= elem
    print("Произведение чисел после максимального по модулю числа", res)

a_pos = tuple()
a_neg = tuple()

for elem in a:
    if elem >= 0:
        a_pos += tuple([elem])
    else:
        a_neg += tuple([elem])
print("Кортеж сначала с отрицательными, а потом позитивными числами:", a_neg + a_pos)
