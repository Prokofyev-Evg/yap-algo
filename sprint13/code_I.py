import sys


class MyQueueSized:

    def __init__(self, n):
        self.queue = [None] * n
        self.max_n = n
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size != self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return True
        return False

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]

    def get_size(self):
        return self.size


def main():
    cmd_count = int(input())
    queue_size = int(input())
    queue = MyQueueSized(queue_size)
    for _ in range(cmd_count):
        line = sys.stdin.readline().rstrip().split(' ')
        if line[0] == 'push':
            if not queue.push(int(line[1])):
                print("error")
        elif line[0] == 'pop':
            value = queue.pop()
            print(value)
        elif line[0] == 'peek':
            print(queue.peek())
        elif line[0] == 'size':
            print(queue.get_size())


if __name__ == '__main__':
    main()
