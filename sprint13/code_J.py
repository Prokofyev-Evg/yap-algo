import sys


class MyQueueNode:
    def __init__(self, value, node=None):
        self.value = value
        if node:
            self.next_node = node
        else:
            self.next_node = self


class MyQueue:

    def __init__(self):
        self.node = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, x):
        if self.node:
            self.node.next_node = MyQueueNode(x, self.node.next_node)
            self.node = self.node.next_node
        else:
            self.node = MyQueueNode(x)
        self.size += 1

    def get(self):
        if self.is_empty():
            return None
        x = self.node.next_node.value
        self.size -= 1
        if self.size == 0:
            self.node = None
        else:
            self.node.next_node = self.node.next_node.next_node
        return x

    def get_size(self):
        return self.size


def main():
    cmd_count = int(input())
    queue = MyQueue()
    for _ in range(cmd_count):
        line = sys.stdin.readline().rstrip().split(' ')
        if line[0] == 'put':
            queue.put(int(line[1]))
        elif line[0] == 'get':
            value = queue.get()
            if value == None:
                print("error")
            else:
                print(value)
        elif line[0] == 'size':
            print(queue.get_size())


if __name__ == '__main__':
    main()
