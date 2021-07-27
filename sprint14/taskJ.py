import sys


def bubble_sort(arr):
    for j in range(len(arr) - 1):
        flag = False
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i+1]:
                arr[i+1], arr[i] = arr[i], arr[i+1]
                flag = True
        if flag:
            print(' '.join([str(x) for x in arr]))
    return arr


def main():
    input()
    arr = [int(x) for x in sys.stdin.readline().rstrip().split()]
    res = bubble_sort(arr[:])
    if res == arr:
        print(' '.join([str(x) for x in res]))


if __name__ == '__main__':
    main()
