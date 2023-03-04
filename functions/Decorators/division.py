#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 10:16:16 2023

@author: aziz
"""
# Make a division function in such a way that it doest not allow denominator to be 0 but
# if it allows denomintor to be zero then print "Can't be divisible" without changing
# code in original function.(Hint: use Decorator function)

def decor(div):
    def inner(x, y):
        if y==0:
            return "Can't be divisible"
        return div(x, y)
    return inner

@decor
def div(x, y):
    return x/y
print(div(3, 0))
print(div(4, 2))