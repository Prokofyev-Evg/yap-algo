import random


def sort(arr, left, right):
    if left == right+1:
        return
    pivot = random.choice(arr[left:right+1])
    left_index = left
    right_index = right
    while left_index != right_index - 1:
        if arr[left_index] < pivot:
            left_index += 1
        elif arr[right_index] >= pivot:
            right_index -= 1
        else:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
    print(f"pivot - {pivot}, left - {left}, right - {right}")
    sort(arr, left, left_index)
    sort(arr, right_index, right)

test_arr = [4, 8, 9, 20, 1, 5, 3, 10]
sort(test_arr, 0, len(test_arr)-1)
print(test_arr)