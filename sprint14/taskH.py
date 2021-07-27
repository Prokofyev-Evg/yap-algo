import sys


def is_first_number_bigger(number_1, number_2):
    for index in range(max(len(number_1), len(number_1))):
        if index >= len(number_1):
            return False
        if index >= len(number_2):
            return True
        if int(number_1[index]) == int(number_2[index]):
            continue
        return int(number_1[index]) > int(number_2[index])
    return len(number_1) < len(number_2)


def insertion_sort_by_comparator(array, less):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and less(item_to_insert, array[j-1]):
            array[j] = array[j-1]
            j -= 1
        array[j] = item_to_insert


def main():
    input()
    numbers = sys.stdin.readline().rstrip().split()
    insertion_sort_by_comparator(numbers, is_first_number_bigger)
    print(''.join([str(x) for x in numbers]))


if __name__ == '__main__':
    main()
