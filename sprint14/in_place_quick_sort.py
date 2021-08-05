# ID правильного решения 52295517
import sys


class Participant:
    def __init__(self, name, points, falls):
        self.name = name
        self.points = points
        self.falls = falls

    def __le__(self, other):
        if self.points != other.points:
            return self.points > other.points
        if self.falls != other.falls:
            return self.falls < other.falls
        return self.name <= other.name

    def __repr__(self):
        return self.name


def in_place_quick_sort(arr, left, right):
    if left < right:
        index = partition(arr, left, right)
        in_place_quick_sort(arr, left, index-1)
        in_place_quick_sort(arr, index+1, right)


def partition(arr, left, right):
    pivot = arr[right]
    less_pivot_idx = left - 1
    for idx in range(left, right+1):
        if arr[idx] <= pivot:
            less_pivot_idx += 1
            arr[idx], arr[less_pivot_idx] = arr[less_pivot_idx], arr[idx]
    return less_pivot_idx


def main():
    qty = int(input())
    participants = []
    for i in range(qty):
        in_data = sys.stdin.readline().rstrip().split()
        participants.append(Participant(name=in_data[0],
                                        points=int(in_data[1]),
                                        falls=int(in_data[2])))
    in_place_quick_sort(participants, 0, qty-1)
    [print(participant) for participant in participants]


if __name__ == '__main__':
    main()
