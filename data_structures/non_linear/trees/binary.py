from __future__ import annotations

from collections import deque
from typing import Tuple, Any


class BTNode:
    """Binary tree node."""

    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None


# TODO: IMPORTANT.
"""
1- `BinaryTree` methods were moved from class `BTNode` and made only the necessary
adjustments to compile, like renaming `self` -> `cls` and make the right method calls.
Most of the methods needs testing and in some cases tweaking.

2- We still have `BinarySearchTree` class which is meant to be a class that inherits from
'BinaryTree' class, so we need to move binary search trees-specific methods to that class.

3- We have `AVLTree` class, adjust it to utilize `BinaryTree` class methods where applicable
and make any necessary overrides.

4- Convert `classmethod`s to `staticmethod`s; our class is stateless.
"""


class BinaryTree:
    """Binary tree utility methods."""

    @classmethod
    def has_no_children(cls, root: BTNode) -> bool:
        return not (root.left or root.right)

    @classmethod
    def has_one_child_only(cls, root: BTNode) -> bool:
        return (root.left and not root.right) or (root.right and not root.left)

    @classmethod
    def has_two_children(cls, root: BTNode) -> bool:
        return root.left and root.right

    @classmethod
    def get_height(cls, root: BTNode) -> int:
        left_height = root.left.get_height() if root.left else -1
        right_height = root.right.get_height() if root.right else -1
        return 1 + max(left_height, right_height)

    # TODO: refactor.
    @classmethod
    def get_inorder_successor_and_parent(cls, root: BTNode) -> Tuple[BTNode, BTNode] | None:
        """
        A node's inorder successor is the node that comes right after it
        in the inorder traversal. In other words, it's the smallest node in
        the right subtree.

        Return the inorder successor and its parent.
        """

        if not root.right:
            return None

        parent = root
        successor: BTNode = root.right
        while successor.left:
            parent = successor
            successor = successor.left
        return successor, parent

    # TODO: study it.
    @classmethod
    def get_depth(cls, root: BTNode, target):
        """Returns depth of the `target` node down from `self`."""
        if root == target:
            return 0
        if root.left:
            left_depth = root.left.get_depth(target)
            if left_depth != -1:
                return 1 + left_depth
        if root.right:
            right_depth = root.right.get_depth(target)
            if right_depth != -1:
                return 1 + right_depth
        return -1  # target not found

    @classmethod
    def count_nodes(cls, root: BTNode) -> int:
        """Counts all linked nodes to this root."""
        count = 1
        left, right = root.left, root.right
        if left:
            count += left.count_nodes()
        if right:
            count += right.count_nodes()
        return count

    @classmethod
    def search(cls, root: BTNode, target: int) -> bool:
        # TODO
        raise NotImplementedError()

    @classmethod
    def is_full(cls, root: BTNode) -> bool:
        """
        A binary tree is considered full if all of its internal/parent
        nodes have 0 or 2 children.
        """
        if cls.has_one_child_only(root):
            return False

        # At this point, the tree has 0 or 2 children.
        if cls.has_two_children(root):
            return root.left.is_full() and root.right.is_full()

        return True

    @classmethod
    def is_perfect(cls, root: BTNode) -> bool:
        """
        A binary tree is considered `perfect` if:
        1- every internal/parent node has exactly two children.
        2- all leaf nodes are at the same level.

        Summary of the algorithm:
        1- find the depth of the leftmost leaf.
        2- every other leaf must have the same depth, otherwise not perfect.
        """

        def find_leftmost_leaf_depth(node: BTNode) -> int:
            d = 0
            while node:
                node = node.left
                d += 1
            return d

        def _is_perfect(node: BTNode, depth: int, level=0) -> bool:
            if node is None:
                return True

            # Leaf nodes' depths are the key to determine whether a tree
            # is perfect or not; they all must have the same depth.
            if node.left is None and node.right is None:
                return depth == level + 1

            # If it's an internal node with only one child
            if node.left is None or node.right is None:
                return False

            # Recur for left and right subtrees
            level += 1
            return (_is_perfect(node.left, depth, level) and
                    _is_perfect(node.right, depth, level))

        # All leaves must have the same depth, so compare them
        # with the depth of the leftmost leaf.
        tree_depth = find_leftmost_leaf_depth(root)
        return _is_perfect(root, tree_depth)

    @classmethod
    def is_perfect2(cls, root: BTNode) -> bool:
        """
        Another implementation but the first one is more efficient.
        """
        if cls.has_no_children(root):
            return True
        elif cls.has_one_child_only(root):
            return False

        left, right = root.left, root.right
        subtrees_perfect = cls.is_perfect2(left) and cls.is_perfect2(right)
        subtrees_equal_height = cls.get_height(left) == cls.get_height(right)
        return subtrees_perfect and subtrees_equal_height

    @classmethod
    def is_complete(cls, root: BTNode) -> bool:
        """
        A binary tree is considered complete if:
        1- all levels are full except possibly the last.
        2- all leaves are as far left as possible.

        Summary of the algorithm:
        1- traverse nodes level by level (BFS).
        2- if a node has a right child but no left child, it's not complete.
        3- after finding the first node that's missing a child, all subsequent
           nodes must be leaves, otherwise not complete.
        """
        nodes = deque([root])
        found_none_child = False
        while nodes:
            current = nodes.popleft()

            left = current.left
            if left:
                if found_none_child:
                    return False
                nodes.append(left)
            else:
                found_none_child = True

            right = current.right
            if right:
                if found_none_child:
                    return False
                nodes.append(right)
            else:
                found_none_child = True

        return True

    @classmethod
    def is_complete2(cls, root: BTNode) -> bool:
        """
        Determine whether a tree is complete using the relationship between array
        indexes and tree elements positions, i.e. since complete binary trees
        are filled from top to bottom and left to right, there is a predictable
        relationship between parent and child nodes based on array indexes.

        For a node of index i (root index is 0), we can calculate:
        - its parent = (i - 1) // 2
        - its left child = 2 * i + 1
        - its right child = 2 * i + 2

        Summary of the algorithm:
        1- find the total number of nodes starting from self.
        2- ensure each node's index is within the valid range [0, total_nodes - 1],
           confirming the tree is filled correctly without missing positions.
        """

        def _is_complete(node, index: int, max_index: int):
            # Is there any missing node/s? Starting from top to bottom,
            # left to right to this node.
            if index >= max_index:
                return False

            left, right = node.left, node.right
            left_complete = _is_complete(left, 2 * index + 1, max_index) if left else True
            right_complete = _is_complete(right, 2 * index + 2, max_index) if right else True

            return left_complete and right_complete

        nodes_count = cls.count_nodes(root)
        return _is_complete(root, 0, nodes_count)

    @classmethod
    def is_height_balanced(cls, root: BTNode) -> bool:
        """
        A binary tree is considered balanced if the height difference between its
        left and right subtrees is at most 1.
        """

        def check_balance(node: BTNode) -> Tuple[int, bool]:  # height, is_balanced
            if node is None:
                return 0, True

            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)

            current_height = 1 + max(left_height, right_height)
            balanced = (
                    left_balanced and
                    right_balanced and
                    abs(left_height - right_height) <= 1
            )

            return current_height, balanced

        height, is_balanced = check_balance(root)
        return is_balanced

    # TODO: study it.
    @classmethod
    def is_height_balanced2(cls, root: BTNode) -> bool:
        """This is faster than the above."""

        def helper(node: BTNode) -> Tuple[int, bool]:  # height, balanced
            if not node:
                return 0, True
            left_height, left_balanced = helper(node.left)
            if not left_balanced:
                return 0, False
            right_height, right_balanced = helper(node.right)
            if not right_balanced:
                return 0, False
            if abs(left_height - right_height) > 1:
                return 0, False
            return max(left_height, right_height) + 1, True

        height, balanced = helper(root)
        return balanced

    @classmethod
    def is_bst(cls, root: BTNode) -> bool:
        """
        Returns whether this binary tree is a binary search tree or not.

        A binary tree is considered a BST if all nodes on the left are
        smaller than the root and root is smaller from all nodes on the right
        for all possible subtrees.
        """
        if cls.has_no_children(root):
            return True

        root_key = root.key
        left, right = root.left, root.right
        if (
                (left and left.key >= root_key) or
                (right and right.key <= root_key)
        ):
            return False

        if left and right:
            return cls.is_bst(left) and cls.is_bst(right)
        elif left:
            return cls.is_bst(left)
        else:
            return cls.is_bst(right)

    @classmethod
    def is_bst2(cls, root: BTNode) -> bool:
        """
        Summary of the algorithm: define the allowed range for each node.
        """

        def _is_bst(node: BTNode, min_val: float | int, max_val: float | int) -> bool:
            if not node:
                return True
            if node.key <= min_val or node.key >= max_val:
                return False

            left_bst = _is_bst(node.left, min_val, node.key)
            right_bst = _is_bst(node.right, node.key, max_val)
            return left_bst and right_bst

        return _is_bst(root, float('-inf'), float('inf'))

    @classmethod
    def search_in_bst(cls, root: BTNode, target: int) -> bool:
        if not cls.is_bst(root):
            raise ValueError('Cannot perform search on a non-BST tree.')

        root_key = root.key
        left, right = root.left, root.right
        if root_key == target:
            return True
        elif left and target < root_key:
            return cls.search_in_bst(left, target)
        elif right and target > root_key:
            return cls.search_in_bst(right, target)
        else:
            return False

    @classmethod
    def insert(cls, root: BTNode, target: int) -> None:
        # TODO: moved from BTNode class to here; needs re-thinking.
        if target == root.key:
            return
        elif target < root.key:
            if root.left:
                cls.insert(root.left, target)
            else:
                root.left = BTNode(target)
        else:
            if root.right:
                cls.insert(root.right, target)
            else:
                root.right = BTNode(target)

    @classmethod
    def get_parent(cls, root: BTNode) -> BTNode | None:
        """Return the parent BTNode of `self`."""
        # TODO

    @classmethod
    def delete(cls, root: BTNode, target: int, parent: BTNode = None) -> None:
        if root.key == target:
            if cls.has_no_children(root):
                if not parent: return  # the root node
                if parent.key > root.key:
                    parent.left = None
                elif parent.key < root.key:
                    parent.right = None
            elif cls.has_one_child_only(root):
                child: BTNode = root.left or root.right
                root.key = child.key
                root.left = root.right = None
            elif cls.has_two_children(root):
                successor, parent = cls.get_inorder_successor_and_parent(root)
                root.key = successor.key
                # Draw the tree to understand it (or TODO: refactor :D).
                if successor.right:
                    successor.key = successor.right.key
                    successor.right = None
                else:
                    if parent.key > successor.key:
                        parent.left = None
                    else:
                        parent.right = None
            return
        elif root.key > target and root.left:
            cls.delete(root.left, target, root)
        elif root.key < target and root.right:
            cls.delete(root.right, target, root)
        else:
            raise ValueError(f'Key {target} is not found the tree.')

    @classmethod
    def print_dfs(cls, root: BTNode) -> None:
        print(root.key, end=', ')
        left, right = root.left, root.right
        if left:
            cls.print_dfs(left)
        if right:
            cls.print_dfs(right)

    @classmethod
    def print_bfs(cls, root: BTNode) -> None:
        nodes = deque([root])
        while nodes:
            current = nodes.popleft()
            print(current.key, end=', ')
            if current.left:
                nodes.append(current.left)
            if current.right:
                nodes.append(current.right)

    @classmethod
    def same_tree(cls, t1: BTNode, t2: BTNode) -> bool:
        # Two empty trees are equal.
        if not (t1 or t2):
            return True

        if (t1 is None) != (t2 is None):  # XOR
            return False

        if t1.key != t2.key:
            return False

        same_left = cls.same_tree(t1.left, t2.left)
        same_right = cls.same_tree(t1.right, t2.right)
        return same_left and same_right

    @staticmethod
    def get_levels(root: BTNode | None) -> list[list[int]]:
        """Return levels of a binary tree, each level in a subarray"""
        if not root:
            return []

        # Each level's keys in a subarray.
        levels: list[list[int]] = []

        queue = deque([root])
        while queue:
            current_level: list[int] = []

            # Walk the previously appended nodes, i.e. the last added level's keys.
            for _ in range(len(queue)):
                current_node = queue.popleft()
                current_level.append(current_node.key)

                left: BTNode = current_node.left
                if left:
                    queue.append(left)

                right: BTNode = current_node.right
                if right:
                    queue.append(right)

            levels.append(current_level)

        return levels
