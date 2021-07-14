import sys

len_k = int(input())
k_str = sys.stdin.readline().rstrip().split()
x = int(input())
y = int(''.join(k_str)) + x

print(' '.join(list(str(y))))
