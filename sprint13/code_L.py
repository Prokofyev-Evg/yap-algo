import sys


def factorial(f, k):
    n1 = 1
    n = 1
    val = 1
    modul = 10 ** k
    while(f > 1):
        val = (n1 + n) % modul
        n1 = n
        n = val
        f -= 1
    return val


if __name__ == '__main__':
    f, k = [int(x) for x in sys.stdin.readline().rstrip().split()]
    print(str(factorial(f, k)))
