import sys


def main():
    lines = int(input())
    columns = int(input())
    matrix = [[0 for x in range(lines)] for y in range(columns)]
    for i in range(lines):
        line = sys.stdin.readline().rstrip().split(' ')
        for j in range(columns):
            matrix[j][i] = line[j]
    for i in range(columns):
        print(' '.join(matrix[i]))


if __name__ == '__main__':
    main()
