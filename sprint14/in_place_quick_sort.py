import random
import sys


class Participant:
    def __init__(self, name, points, falls):
        self.name = name
        self.points = points
        self.falls = falls


def first_participant_is_higher(first, second):
    if first.points == second.points:
        if first.falls == second.falls:
            return first.name < second.name
        else:
            return first.falls < second.falls
    else:
        return first.points > second.points


def in_place_quick_sort(arr, left, right, comparator):
    if left >= right - 1:
        return
    index = partition(arr, left, right, comparator)
    in_place_quick_sort(arr, left, index, comparator)
    in_place_quick_sort(arr, index, right, comparator)


def partition(arr, left_index, right_index, comparator):
    pivot = random.choice(arr[left_index:right_index])
    while left_index < right_index:
        if comparator(arr[left_index], pivot):
            left_index += 1
        elif not comparator(arr[right_index-1], pivot):
            right_index -= 1
        else:
            arr[left_index], arr[right_index -
                                 1] = arr[right_index-1], arr[left_index]
    return right_index


def main():
    qty = int(input())
    participants = [None] * qty
    for i in range(qty):
        in_data = sys.stdin.readline().rstrip().split()
        participants[i] = Participant(name=in_data[0],
                                      points=int(in_data[1]),
                                      falls=int(in_data[2]))
    in_place_quick_sort(participants, 0, qty, first_participant_is_higher)
    print('\n'.join([x.name for x in participants]))


if __name__ == '__main__':
    main()
