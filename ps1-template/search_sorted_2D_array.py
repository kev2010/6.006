#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 22:13:44 2018

@author: fengy
"""

def search_sorted_2D_array(A, v):
    '''
    Return tuple (x, y) such that A[y][x] == v, or None.
    Input: A | Array of equal length arrays of integers
             | representing the rows of a 2D array
             | where A[y][x] >= A[y - 1][x] and
             | A[y][x] >= A[y][x - 1]
             | for all (x, y) in range.
           v | An integer to search for in A.
    '''
    a = len(A)-1
    b = 0
    guess = A[a][b]
    n = len(A)
    m = len(A[0])
    x = None
    y = None
    
    while n > 0 and m > 0:
        if v == guess:
            x = b
            y = a
            break
        elif v > guess:
            b += 1
            m -= 1
            guess = A[a][b]
        elif v < guess:
            a -= 1
            n -= 1
            guess = A[a][b]
    
    if x != None:
        return (x,y)
    else: return None
    