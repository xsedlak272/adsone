#!/usr/bin/env python3

from basic import Node, Stack, LinkedList, Queue  # noqa F403


def main():

    # ----------------- Node -----------------

    node1: Node = Node(1)
    node2: Node = Node(2)
    node3: Node = Node(3)
    node4: Node = Node("4")
    node5: Node = Node(node1)

    node1.next = node2
    node2.next = node3
    node2.prev = node1
    node1.next.next.next = node4
    node4.next = node5
    node1.prev = node5

    assert node4.next.value == node1

    # ----------------- Stack -----------------

    stack: Stack = Stack()

    assert stack.size == 0

    stack.put(3)
    stack.put(2)
    stack.put(stack.size)

    assert stack.size == 3
    assert stack.pop() == 2
    assert stack.pop() == 2

    for i in range(1, 21, 2):
        stack.put(i)

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
    assert llist.tail.value == 3
    assert llist.pop() == 3
    assert llist.pop_node() == node1
    assert llist.size == 3

    del llist


main()
