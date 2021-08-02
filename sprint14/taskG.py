import sys


def main():
    input()
    cloth = sys.stdin.readline().rstrip().split()
    res = {'0': 0, '1': 0, '2': 0}
    for item in cloth:
        res[item] += 1
    answer = ""
    for key in res:
        answer += key * res[key]
    print(' '.join(list(answer)))

if __name__ == '__main__':
    main()
