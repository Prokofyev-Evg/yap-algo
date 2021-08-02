import sys


def is_first_number_bigger(number_1, number_2):
    return int(number_1 + number_2) > int(number_2 + number_1)


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
