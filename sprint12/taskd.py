import sys

days_cnt = int(input())
days = sys.stdin.readline().rstrip().split()
res = 0

if days_cnt == 1:
    res = 1
else:
    if int(days[0]) > int(days[1]):
        res += 1
    if int(days[days_cnt-1]) > int(days[days_cnt-2]):
        res += 1

    for i in range(1, days_cnt-1):
        if int(days[i-1]) < int(days[i]) > int(days[i+1]):
            res += 1

print(res)
