def factorial(n1, n, k):
    if k < 2:
        return n
    if k == 2:
        return n1 + n
    return factorial(n, n1 + n, k - 1)


if __name__ == '__main__':
    n = int(input())
    print(factorial(1, 1, n))
