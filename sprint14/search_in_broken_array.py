def binary_search_in_shifted_array(arr, left, right, value):
    mid = (left + right) // 2
    if arr[mid] == value:
        return mid
    if left >= right:
        return -1
    if arr[0] < arr[mid]: # left is sorted part
        if arr[0] <= value < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else: 
        if arr[mid] < value <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1
    return binary_search_in_shifted_array(arr, left, right, value)


def broken_search(nums, target) -> int:
    return binary_search_in_shifted_array(nums, 0, len(nums) - 1, target)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6
