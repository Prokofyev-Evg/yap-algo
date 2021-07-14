import sys

lines = int(input())
columns = int(input())
matrix = []
result = []
for i in range(lines):
    matrix.append(sys.stdin.readline().rstrip())

x = int(input())
y = int(input())

if x >= 1:
    result.append(int(matrix[x-1].split()[y]))
if x <= lines - 2:
    result.append(int(matrix[x+1].split()[y]))
if y >= 1:
    result.append(int(matrix[x].split()[y-1]))
if y <= columns - 2:
    result.append(int(matrix[x].split()[y+1]))
result.sort()
print(' '.join(str(val) for val in result))
