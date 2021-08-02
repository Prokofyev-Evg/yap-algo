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
        return quicksort(greater) + center + quicksort(less)

def main():
    input()
    sides = [int(x) for x in sys.stdin.readline().rstrip().split()]
    sides = quicksort(sides)
    for i in range(2, len(sides)):
        if sides[i - 2] < sides[i - 1] + sides[i]:
            print(sides[i - 2] + sides[i - 1] + sides[i])
            return 

if __name__ == '__main__':
    main()
