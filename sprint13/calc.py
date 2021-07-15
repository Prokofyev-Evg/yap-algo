# ID правильного решения 52166090
import sys
import operator

COMMANDS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()


def calc(line):
    stack = Stack()
    for item in line:
        if item in COMMANDS.keys():
            right_operand = stack.pop()
            left_operand = stack.pop()
            stack.push(COMMANDS[item](left_operand, right_operand))
        else:
            stack.push(int(item))
    return stack.pop()


if __name__ == '__main__':
    line = sys.stdin.readline().rstrip().split()
    print(calc(line))
