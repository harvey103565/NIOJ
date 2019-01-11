#! /user/bin/python3
# -*- coding: utf-8 -*-


def RootOfNumber(n):
    if n < 0:
        n = -n
    root = 0
    while n > 9:
        root += n % 10
        n = n // 10
        if n < 10:
            root += n
            n, root = root, 0

    return n

def RootOfNumber_Optimal(n):
    if n < 0:
        n = -n
    
    if not n:
        return 0
    
    return (n - 1) % 9 + 1


r = RootOfNumber(0)
print(r)
r = RootOfNumber_Optimal(0)
print(r)

r = RootOfNumber(10000)
print(r)
r = RootOfNumber_Optimal(10000)
print(r)

r = RootOfNumber(123)
print(r)
r = RootOfNumber_Optimal(123)
print(r)

r = RootOfNumber(123456)
print(r)
r = RootOfNumber_Optimal(123456)
print(r)
