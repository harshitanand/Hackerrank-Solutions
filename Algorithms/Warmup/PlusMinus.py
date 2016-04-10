import sys

if __name__ == "__main__":
    size = input()
    array = map(int, raw_input().split())
    neg, zer, pos = 0, 0, 0

    for item in array:
        if item<0:
            neg += 1
        elif item == 0:
            zer += 1
        else:
            pos += 1
            
    print round(pos/size, 6)
    print round(neg/size, 6)
    print round(zer/size, 6)
