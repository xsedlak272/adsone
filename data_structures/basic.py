#!/usr/bin/env python3

from typing import Any, overload
from _collections_abc import Iterator
from math import inf


class Node():
    """
    Auxillary class implementing a standard Node.

    Attributes:
    -----------
    self.value: Any
        Holds the value of the node

    self.next: Node | None
        Points to the succesor of the node.

    self.prev: Node | None
        Points to the predecessor of the node.
    """
    def __init__(self, value: Any = None):
        self.value: Any = value
        self.next: Node | None = None
        self.prev: Node | None = None


class Stack():
    """
    An implementation of the data structure stack using a standard
    Python list.

    Attributes:
    -----------
    self.stack: list[Any]
        Represents stack with elements of any type.

    self.size: int
        Keeps the size of the stack.
    """
    def __init__(self) -> None:
        self.stack: list[Any] = []
        self.size: int = 0

    def push(self, x: Any) -> None:
        """
        Puts the value to stack (appends to the list).
        """
        self.size += 1
        self.stack.append(x)

    def pop(self) -> Any:
        """
        Removes the elements at the top of the stack (pops from the list).
        """
        assert self.stack, f"{type(self).__name__} is empty."

        self.size -= 1
        return self.stack.pop()


class LinkedList():
    """
    An implementation of LinkedList using class Node. Every
    operation runs in O(1) time, except for self.contains,
    which runs in O(n).

    Attributes:
    -----------
    self.head: Node | None
        Represents the first node of the linked list.

    self.tail: Node | None
        Represents the last node of the linked list.

    self.size: int
        Keeps the size of the linked list.
    """
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self.size: int = 0

    def __len__(self) -> int:
        return self.size

    def __iter__(self) -> Iterator:
        node = self.head
        while node is not None:
            yield node.value
            node = node.next

    def _put_start(self, node: Node) -> None:
        """
        Auxillary method which is called when we are putting a node
        to an empty linked list.
        """
        self.head = node
        self.tail = node

    def put(self, value: Any) -> None:
        """
        Appends the given value <value> at the end of linked list.
        """
        node = Node(value)
        self.put_node(node)

    def put_left(self, value: Any) -> None:
        """
        Prefixes the given value <value> at the start of linked list.
        """
        node = Node(value)
        self.put_node_left(node)

    def put_node(self, node: Node) -> None:
        """
        Appends the given node <node> at the end of linked list.
        """
        self.size += 1

        if not self.head:
            self._put_start(node)
            return

        assert self.tail
        self.tail.next = node
        node.prev = self.tail
        self.tail = self.tail.next

    def put_node_left(self, node: Node) -> None:
        """
        Prefixes the given node <node> at the end of linked list.
        """
        self.size += 1

        if not self.head:
            self._put_start(node)
            return

        node.next = self.head
        self.head.prev = node
        self.head = self.head.prev

    def pop(self) -> Any:
        """
        Deletes a node from the end of the linked list and returns the value.
        """
        assert self.head, f"{type(self).__name__} is empty."

        assert self.tail
        value: Any = self.tail.value
        self.tail = self.tail.prev
        self.size -= 1

        return value

    def pop_left(self) -> Any:
        """
        Deletes a node from the start of the linked list and returns the value.
        """
        assert self.head, f"{type(self).__name__} is empty."

        value: Any = self.head.value
        self.head = self.head.next
        self.size -= 1

        return value

    def pop_node(self) -> Node:
        """
        Deletes a node from the end of the linked list and returns the node.
        """
        assert self.head, f"{type(self).__name__} is empty."

        assert self.tail
        node: Node = self.tail
        self.tail = self.tail.prev
        self.size -= 1

        return node

    def pop_left_node(self) -> Node:
        """
        Deletes a node from the start of the linked list and returns the node.
        """
        assert self.head, f"{type(self).__name__} is empty."

        node: Node = self.head
        self.start = self.head.next
        self.size -= 1

        return node

    def contains(self, value: Any) -> bool:
        """
        Searches the linked list for a given value, returns True if found,
        else False.
        """
        node = self.head

        while node is not None:
            if node.value == value:
                return True
            node = node.next

        return False


class Queue(LinkedList):
    """
    An implementation of Queue as a LinkedList.
    """


class Heap():
    def __init__(self):
        self._heap = []
        self.size: int = 0


class MaxHeap():
    def __int__(self):
        self._heap = []
        self.size: int = 0

    @overload
    def insert(self, value: str) -> None:
        ...

    @overload
    def insert(self, value: tuple[int, Any]) -> None:
        ...

    @overload
    def insert(self, value: list[int]) -> None:
        ...

    def insert(self, value: int):
        self._heap.append(-inf)
        self.increase_key(self.size, value)
        self.size += 1

    def extract_max(self) -> int | None:
        if self.size == 0:
            return None

        ret_val = self.maximum()
        self.__swap(0, self.size - 1)
        self.size -= 1
        self.__heapify(0)

        return ret_val

    def increase_key(self, index: int, key: int) -> None:
        assert self.size > index, f"{type(self).__name__} is\
            shorther then {index} elements."

        self._heap[index] = key
        while index > 0:
            self.__swap(index, self.__parent(index))
            index = self.__parent(index)

    def maximum(self):
        assert self.size > 0, f"{type(self).__name__} is empty."

        return self.heap[0]

    def __parent(self, i: int) -> int | None:
        return (i - 1) // 2 if i > 0 else None

    def __swap(self, i1: int, i2: int) -> None:
        assert self.size > max(i1, i2)

        self._heap[i1], self._heap[i2] = self._heap[i2], self._heap(i1)

    def __left(self, i: int) -> int:
        return 2*i + 1

    def __right(self, i: int) -> int:
        return 2*i + 2

    def __heapify(self, i: int) -> None:
        largest: int = i
        left_child: int = self.__left(i)
        right_child: int = self.__right(i)

        if left_child < self.size and self._heap[left_child] > largest:
            largest = left_child

        if right_child < self.size and self._heap[right_child] > largest:
            largest = right_child

        if largest != i:
            self.__swap(i, largest)
            self.__heapify(largest)


class MinHeap():
    def __init__(self) -> None:
        self._heap: list[int] = []
        self.size: int = 0

    @overload
    def insert(self, value: str) -> None:
        ...

    @overload
    def insert(self, value: tuple[int, Any]) -> None:
        ...

    @overload
    def insert(self, value: list[int]) -> None:
        ...

    def insert(self, value: int):
        self._heap.append(-inf)
        self.decrease_key(self.size, value)
        self.size += 1

    def extract_min(self) -> int | None:
        if self.size == 0:
            return None

        ret_val = self.minimum()
        self.__swap(0, self.size - 1)
        self.size -= 1
        self.__heapify(0)

        return ret_val

    def decrease_key(self, index: int, key: int) -> None:
        assert self.size > index, f"{type(self).__name__} is\
            shorther then {index} elements."

        self._heap[index] = key
        while index > 0:
            self.__swap(index, self.__parent(index))
            index = self.__parent(index)

    def minimum(self):
        assert self.size > 0, f"{type(self).__name__} is empty."

        return self.heap[0]

    def __parent(self, i: int) -> int | None:
        return (i - 1) // 2 if i > 0 else None

    def __swap(self, i1: int, i2: int) -> None:
        assert self.size > max(i1, i2)

        self._heap[i1], self._heap[i2] = self._heap[i2], self._heap[i1]

    def __left(self, i: int) -> int:
        return 2*i + 1

    def __right(self, i: int) -> int:
        return 2*i + 2

    def __heapify(self, i: int) -> None:
        largest: int = i
        left_child: int = self.__left(i)
        right_child: int = self.__right(i)

        if left_child > self.size and self._heap[left_child] > largest:
            largest = left_child

        if right_child > self.size and self._heap[right_child] > largest:
            largest = right_child

        if largest != i:
            self.__swap(i, largest)
            self.__heapify(largest)


class PriorityQueue():
    def __init__(self, typeHeap: bool = True) -> None:
        if typeHeap:  # MaxHeap
            self._heap: MaxHeap = MaxHeap()
            self.insert = self._heap.insert
            self.extract = self._heap.extract_max
            self.improvekey = self._heap.increase_key
            self.peek = self._heap.maximum
        else:  # MinHeap
            self._heap: MinHeap = MinHeap()
            self.insert = self._heap.insert
            self.extract = self._heap.extract_max
            self.improvekey = self._heap.increase_key
            self.peek = self._heap.maximum


class FibonnaciHeap():
    def __init__(self):
        pass

    def insert(self):
        # TODO
        pass

    def get(self):
        # TODO
        pass
