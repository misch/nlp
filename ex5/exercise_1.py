#!/usr/bin/python

def fnv(input):
    # Define offset and FNV_prime according to http://www.isthe.com/chongo/tech/comp/fnv/#FNV-param
    offset_basis32 = 2166136261
    FNV_prime32 = 16777619

    # Go through each character of the string
    hash = offset_basis32
    for s in input:
        hash *= FNV_prime32
        hash %= (2**32)
        hash ^= ord(s)
    return hash