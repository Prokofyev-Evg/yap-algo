import sys


class StackItem:

    def __init__(self, value, node):
        self.value = value
        self.prev_node = node
        self.max_value = value
        if node:
            if node.max_value > self.max_value:
                self.max_value = node.max_value


class Stack:

    def __init__(self):
        self.node = None

    def push(self, value):
        self.node = StackItem(value, self.node)

    def pop(self):
        temp_node = self.node
        if self.node is None:
            return None
        self.node = self.node.prev_node
        return temp_node.value

    def get_max(self):
        if self.node is None:
            return None
        return self.node.max_value


def main():
    cmd_count = int(input())
    stack = Stack()
    for _ in range(cmd_count):
        line = sys.stdin.readline().rstrip().split(' ')
        if line[0] == 'push':
            stack.push(int(line[1]))
        elif line[0] == 'pop':
            value = stack.pop()
            if value is None:
                print("error")
        elif line[0] == 'get_max':
            maximum = stack.get_max()
            if maximum is None:
                print("None")
            else:
                print(maximum)


if __name__ == '__main__':
    main()
