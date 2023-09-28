"""
    Most sorting algorithms can be divided into two categories: comparison sorts and distribution sorts.
    In a comparison sort, the data items can be arranged in either ascending or descending order by performing pairwise
    logical comparisons between the sort keys.
    A distribution sort, on the other hand, distributes or divides the sort keys into intermediate groups or
    collections based on the individual key values.
"""


def merge_sort(sequence):
    """
    The merge sort algorithm uses the divide and conquer strategy to sort the keys stored in a mutable sequence.
    The sequence of values is recursively divided into smaller and smaller subsequences until each value is contained
    within its own subsequences. The subsequences are then merged back together to create a sorted sequence.

    worst time complexity of O(nlogn)
    # note: this is wrapper function which calculates the required parameters and calls _merge_sort method.
    parameters:
    -----------
                sequence: any mutable object

    returns sequence in a sorted order.
    """

    n = len(sequence)
    temp_list = [0] * n
    _merge_sort(sequence, 0, n-1, temp_list)


def _merge_sort(sequence, first_index: int, last_index: int, temp_list: list):
    """
    Sorts a virtual subsequence in ascending order.
    parameters:
    -----------
                sequence: any mutable object

                first_index: int
                             start index of virtual subsequence.
                last_index: int
                            end index of virtual subsequence.
                temp_list: list
                           temporary storage used in the merging phase of the merge sort algorithm.
    """
    if first_index == last_index:
        return

    else:
        middle_index = (first_index + last_index) // 2
        # split the sequence.
        _merge_sort(sequence, first_index, middle_index, temp_list)
        _merge_sort(sequence, middle_index+1, last_index, temp_list)
        # merge two subsequences.
        _merge(sequence, first_index, middle_index+1, last_index+1, temp_list)


def _merge(sequence, left_first_index: int, right_first_index: int, right_last_index: int, temp_list: list):
    """
    Merges the two sorted virtual subsequences.
    using the tmpArray for intermediate storage.

    left virtual sub_array is [first_index .... right_first_index-1]
    right virtual sub_array is [right_first_index .... right_last_index]

    merges two virtual subsequences.

    parameters:
    -----------
                sequence: any mutable object
                first_index: int
                             start index of virtual subsequence.
                middle_index: int
                             middle index of virtual subsequence.
                last_index: int
                            end index of virtual subsequence.
                temp_list: list
                           temporary storage used in the merging phase of the merge sort algorithm.

    returns the merged sequence.
    """

    # initializes sub_arrays start indexes
    a = left_first_index
    b = right_first_index
    m = 0
    while a < right_first_index and b < right_last_index:
        if sequence[a] < sequence[b]:
            temp_list[m] = sequence[a]
            a += 1
        else:
            temp_list[m] = sequence[b]
            b += 1
        m += 1

    while a < right_first_index:
        temp_list[m] = sequence[a]
        a += 1
        m += 1

    while b < right_last_index:
        temp_list[m] = sequence[b]
        b += 1
        m += 1

    for i in range(right_last_index - left_first_index):
        sequence[i + left_first_index] = temp_list[i]


def heapsort(sequence):
    """
     The heapsort algorithm builds a heap from a sequence of unsorted values and then extracts the items from the heap
         to create a sorted sequence.

     by using max each time we call extract method we get the largest item in the heap.

    worst time complexity of O(nlogn)
    parameters:
    -----------
                 sequence: any mutable object

    returns sequence in a sorted order.
    """

    # simple implication of heap sort that needs another storage for heap.

    # heap = MinHeap()
    #
    # for item in sequence:
    #     heap.insert(item)

    # for i in range(len(sequence)):
    #     sequence[i] = heap.extract()

    # this implication makes max heap and stores it in the given sequence.
    _build_max_heap(sequence)
    _extract_heap(sequence)


def _build_max_heap(sequence):
    """
    begins iteration from the second element of sequence and compares it with it's parent.
    if it is larger than it's parents, it swaps it.

    parameters:
    ----------
                sequence: any mutable object

    returns max heap(in the given sequence)
    """
    for i in range(1, len(sequence)):
        node_index = i
        parent_index = (node_index-1)//2
        while parent_index >= 0:
            if sequence[parent_index] < sequence[node_index]:
                sequence[node_index], sequence[parent_index] = sequence[parent_index], sequence[node_index]
            node_index = parent_index
            parent_index = (node_index-1)//2


def _extract_heap(sequence):
    """
    extracts the heap's root and stores it in the last element of that iteration.

    parameters:
    ----------
                sequence: any mutable object

    return sequence in a sorted order.
    """
    n = len(sequence)
    for i in range(0, n):
        sequence[0], sequence[n-i-1] = sequence[n-i-1], sequence[0]
        node_index = 0
        left_index = 1
        right_index = 2
        max_limit = n - i - 1
        # sequence[max_limit :] are sorted.
        while left_index < max_limit or right_index < max_limit:
            # if node is smaller than it's left child and ( left child is larger than it's right sibling or
            # right child has reached max_limit.)
            if (sequence[node_index] < sequence[left_index]) and ((sequence[left_index] > sequence[right_index]) or
                                                                  right_index == max_limit):
                sequence[left_index], sequence[node_index] = sequence[node_index], sequence[left_index]
                node_index = left_index
                left_index = 2 * node_index + 1
                right_index = 2 * node_index + 2

            elif right_index < max_limit and sequence[node_index] < sequence[right_index]:
                # if node is smaller than it's right child and right child is larger than it's left sibling.
                sequence[right_index], sequence[node_index] = sequence[node_index], sequence[right_index]
                node_index = right_index
                left_index = 2 * node_index + 1
                right_index = 2 * node_index + 2

            else:
                break


def quick_sort(sequence):
    pass


import random
for _ in range(100):
    a = [random.randint(1, 300) for i in range(10)]
    heapsort(a)
    print(a == sorted(a))

