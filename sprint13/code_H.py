import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


allowed_brackets = {
    '{': '}',
    '[': ']',
    '(': ')',
}


def main(brackets):
    stack = Stack()
    for bracket in brackets:
        if bracket in allowed_brackets.keys():
            stack.push(bracket)
        else:
            if stack.size() == 0:
                return False
            expect = stack.pop()
            if bracket != allowed_brackets[expect]:
                return False
    return stack.size() == 0


if __name__ == '__main__':
    brackets = list(sys.stdin.readline().rstrip())
    print(main(brackets))
