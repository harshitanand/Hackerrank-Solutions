#!/bin/python

import sys

if __name__ == "__main__":
    n = int(raw_input().strip())
    res = 0
    for i in xrange(n):
        arr = map(int,raw_input().strip().split(' ')) 
        res += arr[i]-arr[-(i+1)]
    print abs(res) 
