# ID правильного решения 52165963
import sys


class TwoSideDeque:

    def __init__(self, size):
        self.head_index = 0
        self.tail_index = size - 1
        self.size = 0
        self.max_size = size
        self.deque = [None] * size

    def push_front(self, value):
        if self.is_full():
            return False
        self.deque[self.head_index] = value
        self.head_index = (self.head_index + 1) % self.max_size
        self.size += 1
        return True

    def push_back(self, value):
        if self.is_full():
            return False
        self.deque[self.tail_index] = value
        self.tail_index = (self.tail_index - 1) % self.max_size
        self.size += 1
        return True

    def pop_front(self):
        if self.is_empty():
            return None
        self.head_index = (self.head_index - 1) % self.max_size
        self.size -= 1
        value = self.deque[self.head_index]
        self.deque[self.head_index] = None
        return value

    def pop_back(self):
        if self.is_empty():
            return None
        self.tail_index = (self.tail_index + 1) % self.max_size
        self.size -= 1
        value = self.deque[self.tail_index]
        self.deque[self.tail_index] = None
        return value

    def is_full(self):
        return self.size == self.max_size

    def is_empty(self):
        return self.size == 0


if __name__ == '__main__':
    cmd_count = int(input())
    deque_size = int(input())
    two_side_deque = TwoSideDeque(deque_size)
    command = {
        'push_back': two_side_deque.push_back,
        'push_front': two_side_deque.push_front,
        'pop_front': two_side_deque.pop_front,
        'pop_back': two_side_deque.pop_back,
    }
    for _ in range(cmd_count):
        line = sys.stdin.readline().rstrip().split()
        if len(line) == 1:
            value = command[line[0]]()
            if value is None:
                print('error')
            else:
                print(value)
        else:
            if command[line[0]](line[1]) is False:
                print('error')
