import sys

if __name__ == "__main__":

    n = int(raw_input().strip())
    arr = map(int,raw_input().strip().split(' '))
    print n

    while len(arr)!=0:
        red = min(arr)
        res = []
        for item in arr:
            item = item - red
            if item != 0:
                res.append(item)
        arr = res
        if len(arr) != 0:
            print len(arr)
