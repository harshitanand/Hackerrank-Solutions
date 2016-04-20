import sys

if __name__ == "__main__":

    args = input()

    for i in range(args):
        A = map(int, raw_input().split(' '))
        print int(math.floor(math.sqrt(A[1])) - math.ceil(math.sqrt(A[0])) + 1)
