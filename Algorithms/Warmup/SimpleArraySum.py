import sys

if name == "_main_":
    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    print sum(arr)
