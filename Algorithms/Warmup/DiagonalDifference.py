#!/bin/python

import sys

if name == "_main_":
    n = int(raw_input().strip())
    res = 0
    for i in xrange(n):
        arr = map(int,raw_input().strip().split(' ')) 
        res += arr[i]-arr[-(i+1)]
    print abs(res) 
