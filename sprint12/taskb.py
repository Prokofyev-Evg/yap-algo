import sys

line = sys.stdin.readline().rstrip()
value_1, value_2, value_3 = list(map(int, line.split()))

if (value_1 % 2 == value_2 % 2 == value_3 % 2):
    print("WIN")
else:
    print("FAIL")
