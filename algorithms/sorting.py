#!/usr/bin/env python


def insertion_sort(lst: list[int]) -> None:
    """
    Insertion sorting algorithm

    How it works: 
    -------------

    The algorithm sorts by iterating through elements. 
    If lst[i+1] > lst[i], it swtiches the two elements 
    and checks again for i - 1 until it no longer holds true

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


def selection_sort(lst: list[int]) -> None:
    """
    Selection sorting algorithm

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
            Average: O(n^2)

        Space complexity: 0(1)
    """


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


def merge_sort(lst: list[int]) -> None:
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
