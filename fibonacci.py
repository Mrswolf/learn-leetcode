# -*- coding: utf-8 -*-
#
# Fibonacci Number
# Leetcode: 509
from typing import List

# slow version, many recursion
def fib(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib(n-1) + fib(n-2)

# time: O(n^2)

# bottom-up
# 2, 1, 0
# 3, 2, 1
def fib(n: int) -> int:
    if n <=1:
        return n
    f0, f1 = 0, 1
    for i in range(1, n):
        f2 = f1 + f0
        f0, f1 = f1, f2
    return f2
# time: O(n) space: O(1)

# matrix version
# Fn+1 = Fn + Fn-1
# Fn   = Fn + 0*Fn-1
# [Fn+1, Fn] = [[1, 1], [1, 0]] * [Fn, Fn-1]

def multiply(A: List[List[int]], B: List[List[int]]) -> List[List[n]]:
    x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    w = A[1][0] * B[0][1] + A[1][1] * B[1][1]

    return [[x, y], [z, w]]

def mat_power(A, n):
    if n<=1:
        return A
    A = mat_power(A, n//2)
    A = multiply(A, A)
    B = [[1, 1], [1, 0]]
    if n%2 != 0:
        A = multiply(A, B)
    return A

def fib(n: int) -> int:
    if n<=1:
        return n
    A = [[1, 1], [1, 0]]
    A = mat_power(A, n-1)
    return A[0][0]    

