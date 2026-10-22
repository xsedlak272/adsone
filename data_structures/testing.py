#!/usr/bin/env python3

from data_structures.basic import Node, Stack, LinkedList, \
    Queue, MaxHeap, MinHeap, PriorityQueue  # noqa F403


def main() -> None:

    # ----------------- Node -----------------

    node1: Node = Node(1)
    node2: Node = Node(2)
    node3: Node = Node(3)
    node4: Node = Node("4")
    node5: Node = Node(node1)

    node1.next = node2
    node2.next = node3
    node2.prev = node1
    assert node1.next.next
    node1.next.next.next = node4
    node4.next = node5
    node1.prev = node5

    assert node4.next.value == node1

    # ----------------- Stack -----------------

    stack: Stack = Stack()

    assert stack.size == 0

    stack.push(3)
    stack.push(2)
    stack.push(stack.size)

    assert stack.size == 3
    assert stack.pop() == 2
    assert stack.pop() == 2

    for i in range(1, 21, 2):
        stack.push(i)

    for j in range(19, 0, -2):
        assert stack.pop() == j

    assert stack.size == 1

    # ----------------- LinkedList/Queue -----------------

    llist: LinkedList = LinkedList()
    llist.put_node(node1)
    llist.put_node_left(node2)
    llist.put(3)
    llist.put_left(4)
    llist.put_node_left(node2)

    assert llist.size == 5
    assert llist.head == node2
    assert llist.tail
    assert llist.tail.value == 3
    assert llist.pop() == 3
    assert llist.pop_node() == node1
    assert llist.size == 3

    del llist

    # ----------------- MaxHeap -----------------

    max_heap: MaxHeap = MaxHeap()
    max_heap.insert(3)
    max_heap.insert(1)
    max_heap.insert(5)
    assert max_heap.maximum() == 5
    max_heap.increase_key(2, 10)
    assert max_heap.maximum() == 10
    assert max_heap.extract_max() == 10
    assert max_heap.extract_max() == 5
    assert max_heap.maximum() == 3

    # ----------------- MinHeap -----------------

    min_heap: MinHeap = MinHeap()
    min_heap.insert(1)
    min_heap.insert(5)
    min_heap.insert(-3)
    assert min_heap.minimum()
    min_heap.decrease_key(1, -5)
    assert min_heap.minimum() == -5
    assert min_heap.extract_min() == -5
    assert min_heap.extract_min() == -3
    assert min_heap.minimum() == 5

    # ----------------- PriorityQueue -----------------

    max_queue: PriorityQueue = PriorityQueue()
    max_queue.insert(3)
    max_queue.insert(1)
    max_queue.insert(5)
    assert max_queue.peek() == 5
    max_queue.improve_key(2, 10)
    assert max_queue.peek() == 10
    assert max_queue.extract() == 10
    assert max_queue.extract() == 5
    assert max_queue.peek() == 3

    # ----------------- MinHeap -----------------

    min_queue: PriorityQueue = PriorityQueue(False)
    min_queue.insert(1)
    min_queue.insert(5)
    min_queue.insert(-3)
    assert min_queue.peek()
    min_queue.improve_key(1, -5)
    assert min_queue.peek() == -5
    assert min_queue.extract() == -5
    assert min_queue.extract() == -3
    assert min_queue.peek() == 5


main()
