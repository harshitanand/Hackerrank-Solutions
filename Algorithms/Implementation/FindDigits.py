import sys

if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        digits = []
        count = 0
        digits = [c for c in raw_input().strip()]
        number = int(''.join(digits))
        digits = [int(c) for c in digits]
        for digit in digits:
            if digit != 0:
                if number%digit == 0:
                    count += 1
        print count
