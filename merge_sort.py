""" Implementation of the merge sort algorithm

    Assume there is no duplicates for now
"""

def _assert(x, y):
    try:
        assert x == y
    except AssertionError:
        print(x, y)
        raise


def merge_sort(l):
    """ merge sort implementation """
    length = len(l)
    if length in [0, 1]:  # base cases
        return l
    middle = length // 2
    left, right = l[:middle], l[middle:] 
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    merged = []
    i = j = 0
    while i != len(left_sorted) and j != len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            merged.append(left_sorted[i])
            i += 1
        elif left_sorted[i] > right_sorted[j]:
            merged.append(right_sorted[j])
            j += 1
        else:
            raise NotImplementedError
    if i != len(left_sorted):
        merged.extend(left_sorted[i:])
    if j != len(right_sorted):
        merged.extend(right_sorted[j:])
    return merged


if __name__ == '__main__':
    _assert(merge_sort([5, 4, 1, 8, 7, 2, 6, 3]), list(range(1, 9)))
    _assert(merge_sort([]), [])
    _assert(merge_sort(list(range(1, 9))), list(range(1, 9)))
    _assert(merge_sort(list(reversed(range(1, 9)))), list(range(1, 9)))
    _assert(merge_sort([5, 4, 1, 8, 7, 2, 6, 3, 9]), list(range(1, 10)))
    # TODO: Handle duplicates
    #_assert(merge_sort([5, 4, 1, 8, 7, 2, 1, 6, 3, 9]), list(range(1, 10)))

