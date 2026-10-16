#!/usr/bin/env python3

from typing import Any


class Node():
    def __init__(self, value: Any = None):
        self.value = value
        self.next: Node | None = None


class Stack():
    def __init__(self) -> None:
        self.stack: list[Any] = []

    def put(self, x: Any) -> None:
        self.stack.append(x)

    def pop(self) -> Any:
        assert self.stack, f"{type(self).__name__} is empty."
        return self.stack.pop()


class LinkedList():
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0


    def _put_start(self, node: Node) -> None:
        self.head = node
        self.tail = node


    def put(self, node: Node) -> None:
        self.size += 1

        if not self.head:
            self._put_start(node)
            return

        self.tail.next = node
        self.tail = self.tail.next


    def put_left(self, node: Node) -> None:
        self.size += 1

        if not self.head:
            self._put_start(node)
            return

        node.next = self.start
        self.start = node


    def pop_value(self) -> Any:
        assert self.start, f"{type(self).__name__} is empty."

        value: Any = self.start.value
        self.start = self.start.next

        return value


    def pop(self) -> Node:
        assert self.start, f"{type(self).__name__} is empty."

        node: Node = self.start
        self.start = self.start.next

        return node


class Queue(LinkedList):
    pass


class MaxHeap():
    def __int__(self):
        self.heap: list[] = []

    def put(self):
        # TODO
        pass

    def get(self):
        # TODO
        pass


class MinHeap():
    def __init__(self) -> None:
        pass


class FibonnaciHeap():
    def __init__(self):
        pass

    def put(self):
        # TODO
        pass

    def get(self):
        # TODO
        pass
