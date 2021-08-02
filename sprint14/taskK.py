

def merge(arr: list, left: int, mid: int, right: int):
    l = left
    r = mid
    k = left
    res = arr[:]
    while l < mid and r < right:
        if arr[l] < arr[r]:
            res[k] = arr[l]
            l += 1
        else:
            res[k] = arr[r]
            r += 1
        k += 1
    while r < right:
        res[k] = arr[r]
        r += 1
        k += 1
    while l < mid:
        res[k] = arr[l]
        l += 1
        k += 1
    return res


def merge_sort(arr: list, left: int, right: int):
    if right - left <= 1:
        return arr
    mid = (right + left) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid, right)
    res = arr[:]
    arr.clear()
    arr.extend(merge(res, left, mid, right))


arr = [18, -19, 15, -8, 14, 6, -6, 8, 17]
merge_sort(arr, 0, 9)
print(arr)