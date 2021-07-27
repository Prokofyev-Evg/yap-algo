import sys


def binarySearch(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    can_buy_today = arr[mid] >= x
    if mid == 0:
        can_buy_yesterday = False
    else:
        can_buy_yesterday = arr[mid-1] >= x
    if can_buy_today and not can_buy_yesterday:
        return mid + 1
    elif can_buy_today and can_buy_yesterday:
        return binarySearch(arr, x, left, mid)
    else:
        return binarySearch(arr, x, mid + 1, right)


def main():
    input()
    balance = [int(x) for x in sys.stdin.readline().rstrip().split()]
    price = int(input())
    bike_index_1 = binarySearch(balance, price, left=0, right=len(balance))
    if bike_index_1 == -1:
        bike_index_2 = -1
    else:
        bike_index_2 = binarySearch(
            balance, price * 2, left=bike_index_1, right=len(balance))
    print(f"{bike_index_1} {bike_index_2}")


if __name__ == '__main__':
    main()
