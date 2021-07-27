import sys


def is_substring(s1, s2):
    if len(s1) == 0:
        return True
    if len(s2) == 0:
        return len(s1) == 0
    if s1[0] == s2[0]:
        return is_substring(s1[1:], s2[1:])
    return is_substring(s1, s2[1:])


def main():
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    print(is_substring(s1, s2))


if __name__ == '__main__':
    main()
