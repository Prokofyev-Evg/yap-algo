import sys
import random

def partition(array, pivot):
    less = [x for x in array if x < pivot]
    center = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]
    return less, center, greater

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = random.choice(array)
        less, center, greater = partition(array, pivot)
        return quicksort(less) + center + quicksort(greater) 

def main():
    input()
    cookies = [int(x) for x in sys.stdin.readline().rstrip().split()]
    input()
    kids = [int(x) for x in sys.stdin.readline().rstrip().split()]
    cookies = quicksort(cookies)
    kids = quicksort(kids)
    i, k = 0, 0

    while i < len(cookies) and k < len(kids):
        if cookies[i] <= kids[k]:
            i += 1
        k += 1

    print(i)

if __name__ == '__main__':
    main()
