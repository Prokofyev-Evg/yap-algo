import sys

keybord = {2: 'abc',
           3: 'def',
           4: 'ghi',
           5: 'jkl',
           6: 'mno',
           7: 'pqrs',
           8: 'tuv',
           9: 'wxyz'}


def gen_combos(n, prefix):
    if len(n) == 0:
        print(prefix)
    else:
        for letter in keybord[n[0]]:
            gen_combos(n[1:], prefix + letter)


def main():
    numbers = [int(x) for x in list(sys.stdin.readline().rstrip())]
    gen_combos(numbers, "")


if __name__ == '__main__':
    main()
