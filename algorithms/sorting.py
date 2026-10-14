#!/usr/bin/env python


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
    """
    for i in range(len(lst)):
        j: int = i - 1
        while j > 0 and lst[j] > lst[j + 1]:
            swap(lst, i, j)

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
    """
    for i in range(len(lst)):
        m: int = i
        for j in range(i, len(lst)):
            if lst[j] < lst[m]:
                m = j
        lst[i], lst[m] = lst[m], lst[i]

    return


def quicksort(lst: list[int]) -> None:
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
    """


def merge(lst: list[int], left: int, mid: int, right: int) -> None:
    """
    Auxillary function for the merge-sort algorithm. The function
    merges two already sorted parts of list lst.
    """
    aux: list[int] = [lst[x] for x in range(left, right + 1)]
    i: int = left
    j: int = mid + 1

    for k in range(left, right + 1):
        if i <= mid and (j > right or aux[i] <= aux[j]):
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

    The algorithm sorts by iterating through elements.
    In iteration i if lst[i+1] > lst[i], it swtiches the two elements
    and checks again for i - 1 until it no longer holds true. Then
    the algorithms proceeds to iteration i + 1.

    Properties:
    -----------
    Stable: Yes
    In-place: No

    Complexity:
    -----------
        Time complexity:
            Worst: O(n*log n)
            Average: O(n*log n)

        Space complexity: 0(1)
    """

    if left < right:
        mid: int = len(lst) // 2
        merge_sort(lst, left, mid)
        merge_sort(lst, mid + 1, right)
        merge(lst, left, mid, right)


def inplace_merge_sort(lst: list[int]) -> None:
    """
    Mergesort sorting algorithm

    How it works:
    -------------

    The algorithm sorts by iterating through elements.
    In iteration i if lst[i+1] > lst[i], it swtiches the two elements
    and checks again for i - 1 until it no longer holds true. Then
    the algorithms proceeds to iteration i + 1.

    Properties:
    -----------
    Stable: Yes
    In-place: Yes

    Complexity:
    -----------
        Time complexity:
            Worst: O(n*log n)
            Average: O(n*log n)

        Space complexity: 0(1)
    """


def heapsort():
    # TODO
    pass


def shellsort():
    # TODO
    pass
