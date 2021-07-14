import sys

str_1 = list(sys.stdin.readline().rstrip())
str_2 = list(sys.stdin.readline().rstrip())

str_1.sort()
str_2.sort()

str_1.append(' ')

ans = ''

for l1, l2 in zip(str_1, str_2):
    if l1 != l2:
        ans = l2
        break

print(ans)
