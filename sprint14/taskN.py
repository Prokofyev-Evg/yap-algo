import sys



def merge_sort(array):
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] >= array[1]:
            array.reverse()
        return array
    left = merge_sort(array[0: len(array)//2])
    right = merge_sort(array[len(array)//2: len(array)])
    result = [0] * len(array)
    l, r, k = 0, 0, 0

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
        k += 1

    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    
    return result


def main():
    qty = int(input())
    flower_beds = []
    for _ in range(qty):
        flower_beds.append([int(x)
                           for x in sys.stdin.readline().rstrip().split()])
    flower_beds = merge_sort(flower_beds)
    left, right = flower_beds[0]
    result = []
    for part in flower_beds:
        if part[0] > right:
            result.append((str(left), str(right)))
            left, right = part
        else:
            if part[1] > right:
                right = part[1]
    result.append((str(left), str(right)))
    for part in result:
        print(' '.join(part))


if __name__ == '__main__':
    main()
