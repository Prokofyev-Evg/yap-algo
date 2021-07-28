import sys


def is_substring(sub_str, str):
    s, ss = 0, 0
    while s < len(str):
        if ss < len(sub_str) and str[s] == sub_str[ss]:
            ss += 1
        s += 1
    return len(sub_str) == ss


def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    print(is_substring(s1, s2))


if __name__ == '__main__':
    main()
