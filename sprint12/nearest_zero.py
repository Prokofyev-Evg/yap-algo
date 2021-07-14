# ID Правильного решения 52069567
import sys
from math import inf


def main():
    input()
    street = sys.stdin.readline().rstrip().split('0 ')
    print(street)
    for part in street:
        if part == '':
            print(0)
        else:
            print(part.strip())


if __name__ == '__main__':
    main()
