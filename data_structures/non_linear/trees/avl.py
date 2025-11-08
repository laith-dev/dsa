from __future__ import annotations

import sys

from data_structures.non_linear.trees import BTNode, BinaryTree


class AVLNode(BTNode):
    def __init__(self, key: int):
        super().__init__(key)
        # In AVL trees, the height of a leaf node is 0 but
        # for convenience in balance calculations.
        self.height = 1


class AVLTree(BinaryTree):
    """
    AVL tree utility methods.
    """

    @classmethod
    def insert(cls, root: AVLNode | None, key: int) -> AVLNode:
        # Find the correct location and insert the node
        if not root:
            return AVLNode(key)
        elif key < root.key:
            root.left = cls.insert(root.left, key)
        else:
            root.right = cls.insert(root.right, key)

        root.height = 1 + max(
            cls.get_height(root.left),
            cls.get_height(root.right)
        )

        balance_factor = cls.get_balance(root)
        if balance_factor < -1:
            if key > root.right.key:
                return cls.left_rotate(root)
            else:
                root.right = cls.right_rotate(root.right)
                return cls.left_rotate(root)
        elif balance_factor > 1:
            if key < root.left.key:
                return cls.right_rotate(root)
            else:
                root.left = cls.left_rotate(root.left)
                return cls.right_rotate(root)

        return root

    @classmethod
    def delete(cls, root: AVLNode | None, key: int) -> AVLNode | None:
        # Find the node to be deleted and remove it
        left, right = root.left, root.right
        if root is None:
            return root
        elif key < root.key:
            root.left = cls.delete(left, key)
        elif key > root.key:
            root.right = cls.delete(right, key)
        else:
            if left is None:
                return right
            elif right is None:
                return left

            inorder_successor = cls.get_leftmost_node(right)
            root.key = inorder_successor.key
            root.right = cls.delete(right, inorder_successor.key)

        root.height = 1 + max(
            cls.get_height(left), cls.get_height(right)
        )

        balance_factor = cls.get_balance(root)
        if balance_factor < -1:
            if cls.get_balance(right) <= 0:
                return cls.left_rotate(root)
            else:
                root.right = cls.right_rotate(right)
                return cls.left_rotate(root)
        elif balance_factor > 1:
            if cls.get_balance(left) >= 0:
                return cls.right_rotate(root)
            else:
                root.left = cls.left_rotate(left)
                return cls.right_rotate(root)

        return root

    @classmethod
    def get_height(cls, root: AVLNode) -> int:
        return root.height if root else 0

    @classmethod
    def get_balance(cls, root: AVLNode) -> int:
        if root is None:
            return 0
        return cls.get_height(root.left) - cls.get_height(root.right)

    @classmethod
    def left_rotate(cls, root: AVLNode) -> AVLNode:
        """
        Left rotation will basically swap places of root and root.right.
        """

        right = root.right
        temp = right.left
        right.left = root
        root.right = temp

        root.height = 1 + max(
            cls.get_height(root.left), cls.get_height(root.right)
        )
        right.height = 1 + max(
            cls.get_height(right.left), cls.get_height(right.right)
        )
        return right

    @classmethod
    def right_rotate(cls, root: AVLNode) -> AVLNode:
        """
        Right rotation will basically swap places of root and root.left.
        """
        left = root.left
        temp = left.right
        left.right = root
        root.left = temp

        root.height = 1 + max(
            cls.get_height(root.left), cls.get_height(root.right)
        )
        left.height = 1 + max(
            cls.get_height(left.left), cls.get_height(left.right)
        )
        return left

    @classmethod
    def get_leftmost_node(cls, root: AVLNode) -> AVLNode | None:
        if root is None or root.left is None:
            return root
        return cls.get_leftmost_node(root.left)

    @classmethod
    def pre_order(cls, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        cls.pre_order(root.left)
        cls.pre_order(root.right)

    @classmethod
    def print_helper(cls, curr_ptr, indent, last=None):
        if curr_ptr is not None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(curr_ptr.key)
            cls.print_helper(curr_ptr.left, indent, False)
            cls.print_helper(curr_ptr.right, indent, True)
