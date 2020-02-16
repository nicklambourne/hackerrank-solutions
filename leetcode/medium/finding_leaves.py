from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def find_leaves(root: TreeNode) -> List[List[int]]:
        def check_children(node: TreeNode, removed_: List[int]):
            if node.left and not (node.left.right or node.left.left):
                removed_.append(node.left.val)
                node.left = None
            elif node.left:
                check_children(node.left, removed_)
            if node.right and not (node.right.right or node.right.left):
                removed_.append(node.right.val)
                node.right = None
            elif node.right:
                check_children(node.right, removed_)

        output = list()

        while root:
            removed = list()
            if not root.left and not root.right:
                removed.append(root.val)
                root = None
            else:
                check_children(root, removed)
            output.append(removed)

        print(output)

        return output


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    assert Solution.find_leaves(tree) == [[4, 5, 3], [2], [1]]
