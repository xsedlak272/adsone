#!/usr/bin/env python3

from typing import Any


class Node():
    """
    Auxillary class implementing a standard Node for Tree.

    Attributes:
    -----------
    self.value: Any
        Holds the value of the node

    self.next: Node | None
        Points to the succesor of the node.

    self.prev: Node | None
        Points to the predecessor of the node.
    """
    def __init__(self, value: Any = None, islist: bool = False) -> None:
        self.value: Any = value
        self.succs: list[Node] = []
        self.list: bool = islist

    def is_list(self) -> bool:
        return self.list


class Tree():
    """
    Class implementing a general tree.

    Attributes:
        -----------
        self.root: Node | None
            Root of the tree.

        self.arity: int | None
            Records the arity of a given tree. Default is unset (None).
    """
    def __int__(self, arity: int | None = None) -> None:
        self.root: Node | None = None
        self.arity: int | None = arity

    def preorder(self):
        # TODO
        pass

    def inorder(self):
        # TODO
        pass

    def postorder(self):
        # TODO
        pass

    def preorder_iter(self):
        # TODO
        pass

    def inorder_iter(self):
        # TODO
        pass

    def postorder_iter(self):
        # TODO
        pass

    def is_arity(self):
        # TODO
        pass

    def is_balanced(self):
        # TODO
        pass
