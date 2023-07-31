from llistqueue import Queue
import numpy as np


class BPriorityQueue:
    """
    <Bounded Priority Queue>
    class to represent bounded priority queue(FIFO) Data Structure using numpy array which each index of it refers
    to a priority and each index contains Linked list Based Queue.

    In Bounded Queue each item can have priority in the range [0, p(numlevels))

    attributes:
    -----------
                _qlevels: numpy array
                           items with the given priority are stored in the corresponding numpy array indexes.

                _count: int
                       saves number of items in the queue.
                       initially set to 0.
    methods:
    --------

                enqueue(item):
                              adds new item to the end of the queue.

                dequeue():
                          removes first Node from the queue and returns it's element.

                is_empty():
                           returns True if the queue is empty.
        """

    def __init__(self, num_levels):
        """
        initializes queue with the size of num_levels.
        parameters:
        ---------
                  num_levels: int
                             total number of levels in the queue(queue's size).
                             each index contains Queue and corresponds to that priority.

        """
        self._count = 0
        self._qlevels = np.array([Queue() for i in range(num_levels)])

    def enqueue(self, item, priority):
        """
        parameters:
        -----------
                    item: obj
                         object to be added to the queue.
                    priority: int
                             priority number of the given item.

        returns None
        """
        assert priority < len(self._qlevels), 'given priority is not in the proper range.'
        self._qlevels[priority].enqueue(item)
        self._count += 1

    def dequeue(self):
        """
        it searches each array index and until it finds an item and it return the item.
        returns the highest priority item in the queue.
        """
        assert self._count != 0, 'Cannot Dequeue from an empty queue.'
        max_index = 0
        for i in range(len(self._qlevels)):
            if not self._qlevels[i].is_empty():
                max_index = i
                break
        item = self._qlevels[max_index].dequeue()
        self._count -= 1
        return item

    def is_empty(self):
        """
        returns True if the queue is Empty, False Otherwise.
        """
        return len(self) == 0

    def __len__(self):
        """
        returns total number of items in the queue.
        """
        return self._count

