from __future__ import annotations
from typing import List


class Node:
    def __init__(self, value: int):
        self.value = value
        self.connections: List[Node] = []

    def add_node(self, node: Node):
        self.connections.append(node)

    def __str__(self):
        return f"Node<{self.value}>"

    def __repr__(self):
        return str(self)


def depth_first_search(root: Node, value: int) -> bool:
    stack = [root]
    while stack:
        current = stack.pop()
        if current.value == value:
            return True
        else:
            stack.extend(current.connections)
    return False


if __name__ == "__main__":
    root_node = Node(0)
    root_node.add_node(Node(1))
    node2 = Node(2)
    node2.add_node(Node(3))
    root_node.add_node(node2)
    node4 = Node(4)
    root_node.add_node(node4)
    node5 = Node(5)
    node5.add_node(Node(7))
    node4.add_node(node5)
    assert depth_first_search(root_node, 5) is True
