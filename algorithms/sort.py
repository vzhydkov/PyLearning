"""
A bubble sort, a selection sort, and an insertion sort are O(n**2) algorithms.
A shell sort improves on the insertion sort by sorting incremental sublists.
    It falls between O(n) and O(n**2).
A merge sort is O(n log n), but requires additional space for the merging process.
A quick sort is O(n log n), but may degrade to O(n**2)
    if the split points are not near the middle of the list. It does not require additional space.
Links:
http://interactivepython.org/runestone/static/pythonds/SortSearch/sorting.html
http://bigocheatsheet.com/
"""


def bubble_sort(lst):
    """Return the sorted list
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> bubble_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    l = len(lst)
    for a in range(1, l):
        for b in range(l-1):
            if lst[a] < lst[b]:
                lst[a], lst[b] = lst[b], lst[a]


def selection_sort(lst):
    """Return the sorted list
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> selection_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    for i in range(len(lst)-1, 0, -1):
        max_val = 0
        for k in range(1, i+1):
            if lst[k] > lst[max_val]:
                max_val = k
        lst[i], lst[max_val] = lst[max_val], lst[i]


def insertion_sort(lst):
    """Return the sorted list
    >>> lst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    >>> insertion_sort(lst)
    >>> lst == [17, 20, 26, 31, 44, 54, 55, 77, 93]
    True
    """
    for i in range(1, len(lst)):
        val = lst[i]
        pos = i
        while pos > 0 and lst[pos-1] > val:
            lst[pos] = lst[pos-1]
            pos = pos-1
        lst[pos] = val


if __name__ == "__main__":
    import doctest
    doctest.testmod()