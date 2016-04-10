#!/bin/python

import sys

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    print sum((x for x in arr))
