# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node, elem):
    i = 0
    while True:
        if node.value == elem:
            return i
        if node.next_item is None:
            return -1
        node = node.next_item
        i += 1
    return i


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    # result is idx == 2
