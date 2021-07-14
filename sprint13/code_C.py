# Comment it before submitting
# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item

    head = node
    i = 0
    while i != idx:
        prev_node = node
        node = node.next_item
        i += 1
    prev_node.next_item = node.next_item
    return head


def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    print_list(node0)
    new_head = solution(node0, 3)
    # result is node0 -> node2 -> node3
