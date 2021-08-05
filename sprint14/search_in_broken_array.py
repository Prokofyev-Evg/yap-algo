# ID правильного решения 52295335

def binary_search_in_shifted_array(arr, left, right, value):
    mid = (left + right) // 2
    if arr[mid] == value:
        return mid
    if left >= right:
        return -1
    left, right = narrow_boundaries(arr, left, right, value, mid)
    return binary_search_in_shifted_array(arr, left, right, value)


def narrow_boundaries(arr, left, right, value, mid):
    if arr[left] < arr[mid]:
        if arr[left] <= value < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if arr[mid] < value <= arr[right]:
            left = mid + 1
        else:
            right = mid - 1
    return left, right


def broken_search(nums, target) -> int:
    return binary_search_in_shifted_array(nums, 0, len(nums) - 1, target)
