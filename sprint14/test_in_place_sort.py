from in_place_quick_sort import in_place_quick_sort, partition

test_arr = [4, 8, 9, 20, 1, 5, 3, 10]


def test_partition():
    arr = test_arr[:]
    for pivot in test_arr:
        index = partition(arr, pivot, 0, len(arr))
        for i in range(len(arr)):
            if i < index:
                assert arr[i] <= pivot
            else:
                assert arr[i] > pivot


def test_sort():
    arr = test_arr[:]
    in_place_quick_sort(arr, 0, len(arr))
    assert arr == [1, 3, 4, 5, 8, 9, 10, 20]
