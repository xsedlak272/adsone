#!/usr/bin/env python3

from algorithms.sorting import insertion_sort, selection_sort, \
      quicksort, tail_quicksort, iterative_quicksort, \
      merge_sort, heapsort


def main() -> None:
    test_list1: list[int] = [1, 2, 3, 4, 5, 6, 7]
    test_list2: list[int] = [1, 5, 6, 7, 2, 4, 3]
    test_list3: list[int] = [5, 3, 0, -1, 12, 300]
    test_list4: list[int] = [-5, 0, 1, -1, 15, 7, 13, -2]

    sorted_list1: list[int] = sorted(test_list1)
    sorted_list2: list[int] = sorted(test_list2)
    sorted_list3: list[int] = sorted(test_list3)
    sorted_list4: list[int] = sorted(test_list4)

    # ----------------- insertion sort -----------------

    aux1 = test_list1.copy()
    aux2 = test_list2.copy()
    aux3 = test_list3.copy()
    aux4 = test_list4.copy()

    insertion_sort(aux1)
    insertion_sort(aux2)
    insertion_sort(aux3)
    insertion_sort(aux4)

    assert sorted_list1 == aux1, f"Should have been {sorted_list1}, but actually {aux1}"  # noqa E501
    assert sorted_list2 == aux2, f"Should have been {sorted_list2}, but actually {aux2}"  # noqa E501
    assert sorted_list3 == aux3, f"Should have been {sorted_list3}, but actually {aux3}"  # noqa E501
    assert sorted_list4 == aux4, f"Should have been {sorted_list4}, but actually {aux4}"  # noqa E501

    # ----------------- selection sort -----------------

    aux1 = test_list1.copy()
    aux2 = test_list2.copy()
    aux3 = test_list3.copy()
    aux4 = test_list4.copy()

    selection_sort(aux1)
    selection_sort(aux2)
    selection_sort(aux3)
    selection_sort(aux4)

    assert sorted_list1 == aux1, f"Should have been {sorted_list1}, but actually {aux1}"  # noqa E501
    assert sorted_list2 == aux2, f"Should have been {sorted_list2}, but actually {aux2}"  # noqa E501
    assert sorted_list3 == aux3, f"Should have been {sorted_list3}, but actually {aux3}"  # noqa E501
    assert sorted_list4 == aux4, f"Should have been {sorted_list4}, but actually {aux4}"  # noqa E501

    # ----------------- quicksort -----------------

    aux1 = test_list1.copy()
    aux2 = test_list2.copy()
    aux3 = test_list3.copy()
    aux4 = test_list4.copy()

    quicksort(aux1, 0, len(aux1) - 1)
    quicksort(aux2, 0, len(aux2) - 1)
    quicksort(aux3, 0, len(aux3) - 1)
    quicksort(aux4, 0, len(aux4) - 1)

    assert sorted_list1 == aux1, f"Should have been {sorted_list1}, but actually {aux1}"  # noqa E501
    assert sorted_list2 == aux2, f"Should have been {sorted_list2}, but actually {aux2}"  # noqa E501
    assert sorted_list3 == aux3, f"Should have been {sorted_list3}, but actually {aux3}"  # noqa E501
    assert sorted_list4 == aux4, f"Should have been {sorted_list4}, but actually {aux4}"  # noqa E501

    # ----------------- tail_quicksort -----------------

    aux1 = test_list1.copy()
    aux2 = test_list2.copy()
    aux3 = test_list3.copy()
    aux4 = test_list4.copy()

    tail_quicksort(aux1, 0, len(aux1) - 1)
    tail_quicksort(aux2, 0, len(aux2) - 1)
    tail_quicksort(aux3, 0, len(aux3) - 1)
    tail_quicksort(aux4, 0, len(aux4) - 1)

    assert sorted_list1 == aux1, f"Should have been {sorted_list1}, but actually {aux1}"  # noqa E501
    assert sorted_list2 == aux2, f"Should have been {sorted_list2}, but actually {aux2}"  # noqa E501
    assert sorted_list3 == aux3, f"Should have been {sorted_list3}, but actually {aux3}"  # noqa E501
    assert sorted_list4 == aux4, f"Should have been {sorted_list4}, but actually {aux4}"  # noqa E501

    # ----------------- quicksort -----------------

    aux1 = test_list1.copy()
    aux2 = test_list2.copy()
    aux3 = test_list3.copy()
    aux4 = test_list4.copy()

    iterative_quicksort(aux1, 0, len(aux1) - 1)
    iterative_quicksort(aux2, 0, len(aux2) - 1)
    iterative_quicksort(aux3, 0, len(aux3) - 1)
    iterative_quicksort(aux4, 0, len(aux4) - 1)

    assert sorted_list1 == aux1, f"Should have been {sorted_list1}, but actually {aux1}"  # noqa E501
    assert sorted_list2 == aux2, f"Should have been {sorted_list2}, but actually {aux2}"  # noqa E501
    assert sorted_list3 == aux3, f"Should have been {sorted_list3}, but actually {aux3}"  # noqa E501
    assert sorted_list4 == aux4, f"Should have been {sorted_list4}, but actually {aux4}"  # noqa E501

    # ----------------- mergesort -----------------

    aux1 = test_list1.copy()
    aux2 = test_list2.copy()
    aux3 = test_list3.copy()
    aux4 = test_list4.copy()

    merge_sort(aux1, 0, len(aux1) - 1)
    merge_sort(aux2, 0, len(aux2) - 1)
    merge_sort(aux3, 0, len(aux3) - 1)
    merge_sort(aux4, 0, len(aux4) - 1)

    assert sorted_list1 == aux1, f"Should have been {sorted_list1}, but actually {aux1}"  # noqa E501
    assert sorted_list2 == aux2, f"Should have been {sorted_list2}, but actually {aux2}"  # noqa E501
    assert sorted_list3 == aux3, f"Should have been {sorted_list3}, but actually {aux3}"  # noqa E501
    assert sorted_list4 == aux4, f"Should have been {sorted_list4}, but actually {aux4}"  # noqa E501

    # ----------------- heapsort -----------------

    aux1 = test_list1.copy()
    aux2 = test_list2.copy()
    aux3 = test_list3.copy()
    aux4 = test_list4.copy()

    heapsort(aux1)
    heapsort(aux2)
    heapsort(aux3)
    heapsort(aux4)

    assert sorted_list1 == aux1, f"Should have been {sorted_list1}, but actually {aux1}"  # noqa E501
    assert sorted_list2 == aux2, f"Should have been {sorted_list2}, but actually {aux2}"  # noqa E501
    assert sorted_list3 == aux3, f"Should have been {sorted_list3}, but actually {aux3}"  # noqa E501
    assert sorted_list4 == aux4, f"Should have been {sorted_list4}, but actually {aux4}"  # noqa E501


main()
