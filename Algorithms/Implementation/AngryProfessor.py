import sys

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n,k = raw_input().strip().split(' ')
        n,k = [int(n),int(k)]
        count = 0
        a = map(int,raw_input().strip().split(' '))
        for students in a:
            if students <= 0:
                count += 1
        if count >= k:
            print "NO"
        else:
            print "YES"
