import sys

def calc(interval):
    res = 1
    if interval == 0:
        return 1
    for i in range(1, interval+1):
        if i%2 != 0:
            res = 2*res
        elif i%2 == 0:
            res += 1
    return res

if __name__ == "__main__":        
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print calc(n)
