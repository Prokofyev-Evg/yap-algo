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

print(quicksort([8, 2, 6, 5, 9, 7, 5, 6, 2, 9, 4, 6, 5, 8]))