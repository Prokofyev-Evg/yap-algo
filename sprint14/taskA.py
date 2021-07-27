
def gen_brackets(n, k, prefix):
    if n == 0:
        print(prefix)
    else:
        if n - k > 0:
            gen_brackets(n - 1, k + 1, prefix + '(')
        if k > 0:
            gen_brackets(n - 1, k - 1, prefix + ')')


def main():
    qty = int(input())
    gen_brackets(qty * 2, 0, "")


if __name__ == '__main__':
    main()
