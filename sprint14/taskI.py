import sys
import random

def comparsion(x, pivot):
    pass

def partition(array, pivot):
    less = [x for x in array if x[1] > pivot[1] or (x[1] == pivot[1] and x[0] < pivot[0])]
    center = [x for x in array if x == pivot]
    greater = [x for x in array if x[1] < pivot[1] or (x[1] == pivot[1] and x[0] > pivot[0])]
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
    universities = sys.stdin.readline().rstrip().split()
    k = int(input())
    ids = dict.fromkeys(set(universities), 0)
    for item in universities:
        ids[item] += 1
    ids_list = [(x,  ids[x]) for x in ids]
    ids_list = quicksort(ids_list)
    print(' '.join([x[0] for x in ids_list[:k]]))

if __name__ == '__main__':
    main()
