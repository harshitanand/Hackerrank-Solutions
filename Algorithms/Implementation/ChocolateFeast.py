import sys

def calc(wrap, res, cost_wrap):

    if wrap>=cost_wrap:
        wrap -= cost_wrap
        res += 1
        return calc(wrap+1, res, cost_wrap)
    else:
        return res

if __name__ == "__main__":

    t = int(raw_input().strip())

    for a0 in xrange(t):
        n,c,m = raw_input().strip().split(' ')
        n,c,m = [int(n),int(c),int(m)]
        choc = n/c
        print choc + calc(choc, 0, m)
