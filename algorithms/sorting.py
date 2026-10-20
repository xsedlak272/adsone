#!/usr/bin/env python3

from data_structures.basic import Stack


def swap(lst: list[int], i: int, j: int) -> None:
    """
    Auxillary function for swaping elements of a list.
    """

    lst[i], lst[j] = lst[j], lst[i]


def insertion_sort(lst: list[int]) -> None:
    """
    Insertion sorting algorithm

    How it works:
    -------------

    The algorithm sorts by iterating through elements.
    If lst[i+1] > lst[i], it swtiches the two elements
    and checks again for i - 1 until it no longer holds true.

    Properties:
    -----------
    Stable: Yes
    In-place: Yes

    Complexity:
    -----------
        Time complexity:
            Worst: O(n^2)
            Average: O(n^2)

        Space complexity: 0(1)

    Parameters
    ----------
    lst: list[int]
        List of integers to be sorted
    """

    for i in range(len(lst)):
        j: int = i - 1
        while j >= 0 and lst[j] > lst[j + 1]:
            swap(lst, j, j + 1)
            j -= 1

    return


def selection_sort(lst: list[int]) -> None:
    """
    Selection sorting algorithm

    How it works:
    -------------

    The algorithm sorts by iterating through elements.
    In iteration i the algorithm find i-th smallest element
    and swtiches it with i-th element of the list. Therefore
    every index i contains the i-th smallest element and the
    list is sorted.

    Properties:
    -----------
    Stable: No
    In-place: Yes

    Complexity:
    -----------
        Time complexity:
            Worst: O(n^2)
            Average: O(n^2)

        Space complexity: 0(1)

    Parameters
    ----------
    lst: list[int]
        List of integers to be sorted
    """

    for i in range(len(lst)):
        m: int = i
        for j in range(i, len(lst)):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]

    return


def partition(lst: list[int], left: int, right: int) -> int:
    """
    Auxillary function for the quicksort algorithm.

    How it works:
    -------------

        The function picks a pivot (in this case the last element
        being sorted - right) and rearranges the list in the way
        that the pivot is index i which we return, for elements on
        indexes left <= l <= i, lst[l] <= pivot holds true, for elements
        on indexes right >= r > i, lst[r] > pivot holds true.

    Complexity:
    -----------
        Time complexity: O(n)
        Space complexity: 0(1)

        Where n = right - left + 1

    Parameters:
    -----------
    lst: list[int]
        List being sorted

    left: int
        Integer representing the leftmost element to be sorted

    right: int
        Integer representing the rightmost element to be sorted
    """

    pivot: int = lst[right]
    i: int = left - 1

    for j in range(left, right + 1):
        if lst[j] <= pivot:
            i += 1
            swap(lst, i, j)

    return i


def quicksort(lst: list[int], left: int, right: int) -> None:
    """
    Quicksort sorting algorithm

    How it works:
    -------------

        The algorithm sorts by iterating through elements.
        In iteration i if lst[i+1] > lst[i], it swtiches the two elements
        and checks again for i - 1 until it no longer holds true. Then
        the algorithms proceeds to iteration i + 1.

    Properties:
    -----------
        Stable: No
        In-place: Yes

    Complexity:
    -----------
        Time complexity:
            Worst: O(n^2)
            Average: O(n*log n)

        Space complexity: 0(1)

    Parameters:
    -----------
    lst: list[int]
        List being sorted

    left: int
        Integer representing the leftmost element to be sorted

    right: int
        Integer representing the rightmost element to be sorted
    """

    if left < right:
        mid = partition(lst, left, right)
        quicksort(lst, left, mid - 1)
        quicksort(lst, mid + 1, right)


def tail_quicksort(lst: list[int], left: int, right: int) -> None:
    """
    Quicksort algorithm with tail recursion
    """
    while left < right:
        mid: int = partition(lst, left, right)
        tail_quicksort(lst, left, mid - 1)
        left = mid + 1


def iterative_quicksort(lst: list[int], left: int, right: int) -> None:
    """
    Quicksort algorithm using stack (not recursive)
    """
    stack: Stack = Stack()
    stack.push((left, right))
    while stack:
        left, right = stack.pop()
        mid: int = partition(lst, left, right)

        if mid - 1 > left:
            stack.push((left, mid - 1))

        if mid + 1 < right:
            stack.push((mid + 1, right))


def merge(lst: list[int], left: int, mid: int, right: int) -> None:
    """
    Auxillary function for the mergesort algorithm. The function
    merges two already sorted parts of list lst.

    How it works:
    -------------

        The auxillary function merges two parts of the list
        - lst[left:mid] and lst[mid:right]. The merge is implemented
        using a simple for loop with variable k which indexes to k-th
        smallest element on k-th iteration of the for loop. The auxillary
        variables i and j are indexing the separately sorted parts of the
        list. After k iterations the list lst[left:left+k] is sorted.

    Complexity:
    -----------
        Time complexity: O(n)
        Space complexity: 0(n)

        Where n = right - left + 1

    Parameters:
    -----------
    lst: list[int]
        List being sorted

    left: int
        Integer representing the leftmost element to be merged

    mid: int
        Integer used to separate the two parts of the list to be merged

    right: int
        Integer representing the rightmost element to be merged
    """

    aux: list[int] = [lst[x] for x in range(left, right + 1)]
    i: int = 0
    j: int = mid + 1 - left

    for k in range(left, right + 1):
        if i <= mid - left and (j >= len(aux) or aux[i] <= aux[j]):
            lst[k] = aux[i]
            i += 1
        else:
            lst[k] = aux[j]
            j += 1


def merge_sort(lst: list[int], left: int, right: int) -> None:
    """
    Mergesort sorting algorithm

    How it works:
    -------------

    The algorithm sorts by splitting the list into two halfs
    until there is only one or no elemets. Then the algorithm
    uses the auxillary merge function to merge the two sorted
    lists (a list of one or no elements is sorted). The recursion
    depth is at most log n. The merge algorithm time complexity
    is O(n). Therefore the time complexity is O(n*log n).

    Properties:
    -----------
    Stable: Yes
    In-place: No

    Complexity:
    -----------
        Time complexity:
            Worst: O(n*log n)
            Average: O(n*log n)

        Space complexity: 0(n)

    Parameters:
    -----------
    lst: list[int]
        List of integers to be sorted

    left: int
        Integer indexing the leftmost element to be sorted

    right: int
        Integer indexing the rightmost element to be sorted
    """

    if left < right:
        mid: int = (left + right) // 2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
        merge(lst, left, mid, right)


def inplace_merge_sort(lst: list[int]) -> None:
    """
    Mergesort sorting algorithm

    How it works:
    -------------

    Properties:
    -----------
    Stable: Yes
    In-place: Yes

    Complexity:
    -----------
        Time complexity:
            Worst: O(n*(log n)^2)
            Average: O(n*(log n)^2))

        Space complexity: 0(1)
    """
    # TODO
    pass


def heapsort():
    # TODO
    pass


def shellsort():
    # TODO
    pass
