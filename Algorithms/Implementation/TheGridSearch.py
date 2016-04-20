import sys, bisect

if __name == "__main__":

    t = int(raw_input().strip())

    for a0 in xrange(t):
        R,C = raw_input().strip().split(' ')
        R,C = [int(R),int(C)]
        G = []
        G_i = 0
        for G_i in xrange(R):
           G_t = str(raw_input().strip())
           G.append(G_t)
        r,c = raw_input().strip().split(' ')
        r,c = [int(r),int(c)]
        P = []
        P_i = 0
        for P_i in xrange(r):
           P_t = str(raw_input().strip())
           P.append(P_t)
 
        pos, ind, len1, s = [], [], 0, 0
        for i in xrange(r):
            for j in xrange(R):
                cond = G[j].find(P[i])
                if cond!=-1:
                    if j not in pos:
                        bisect.insort_left(pos, j)
                        len1 += 1
                    bisect.insort_left(ind, cond)
 
        flag = "YES"
        if len1 >= r:
            for i in xrange(len1-1) :
                if pos[i]+1==pos[i+1] and ind[i]==ind[i+1]:
                    flag = "YES"
                else:
                    flag = "NO"
        else:
            flag = "NO"
        print flag
