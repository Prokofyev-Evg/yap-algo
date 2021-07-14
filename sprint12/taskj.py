from math import sqrt
in_val = int(input())

arr = []


def factorization(mults, val):
    if val > 2:
        for i in range(2, int(sqrt(val)) + 1):
            if val % i == 0:
                mults.append(i)
                return factorization(mults, val // i)
    mults.append(val)
    return mults


print(' '.join([str(x) for x in factorization(arr, in_val)]))
