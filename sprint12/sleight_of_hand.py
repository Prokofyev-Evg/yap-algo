# ID Правильного решения 52069659
import sys


def main():
    k = int(input())
    in_str = ''
    for _ in range(4):
        in_str += sys.stdin.readline().rstrip()
    print(calc_max_possible_score(list(in_str), 2 * k))


def calc_max_possible_score(cells, max_qty_press):
    numbers = set(cells)
    if '.' in numbers:
        numbers.remove('.')

    points = 0
    for number in numbers:
        if cells.count(number) <= max_qty_press:
            points += 1
    return points


if __name__ == '__main__':
    main()
