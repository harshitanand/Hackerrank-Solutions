import sys

if __name__ == "__main__":

    n,t = raw_input().strip().split(' ')
    n,t = [int(n),int(t)]
    width = map(int,raw_input().strip().split(' '))

    for a0 in xrange(t):
        i,j = raw_input().strip().split(' ')
        i,j = [int(i),int(j)]
        res = width[i]
        for item in range(i, j+1):
            if res>width[item]:
                res = width[item]
        print res
