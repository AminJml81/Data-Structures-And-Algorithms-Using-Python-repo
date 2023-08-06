import numpy as np


class CircularQueue:
    """
    Array Queue
    class to represent circular queue(FIFO) Data Structure using python numpy array.

    attributes:
    -----------
                _qarray: numpy array
                        items are stored in a numpy array.

                _count: int
                       saves number of items in the queue.
                       initially set to 0.

                _front:
                       queue's front index. The index to remove item.
                       initially set to queue's given size.

                _back: int
                      queue's back index. The index to add new item.
    methods:
    --------

                enqueue(item):
                              adds new item to the end of the queue.

                dequeue():
                          removes first element from the queue and returns the element.

                is_empty():
                           returns True if the queue is empty.

                __len()--:
                          returns queue's size.

                # Note: dequeue cannot be done from an empty queue.

    # by using numpy array, adding two markers for queue's front and back , enqueue() and dequeue() operations are done
    in O(1). but the queue size now is limited.
    """

    def __init__(self, maxsize, queue_items_type=int):
        """
        initializes queue with numpy array with the given size.

        parameters:
        -----------
                    maxsize: int
                            array size
                    queue_items_type:
                                     determines the type of array.
                                     default int.
        """
        self._qarray = np.zeros(maxsize, dtype=queue_items_type)
        self._front = 0
        self._back = maxsize-1
        self._count = 0

    def enqueue(self, item):
        """
        if the queue is not full, it adds new item to the queue.
        updates _back index, then adds the item.
        parameters:
        ---------
                  item: obj
                       item to be added to the queue.

        returns None
        """
        assert not self.is_full(), 'Cannot Enqueue to a full queue.'
        self._back = (self._back + 1) % len(self._qarray)
        self._qarray[self._back] = item
        self._count += 1

    def dequeue(self):
        """
        if the queue is not empty ,it removes the item from the front of the queue then it updates the front index.

        returns item that was removed from the queue.
        """
        assert not self.is_empty(), 'Cannot Dequeue from an empty queue.'
        item = self._qarray[self._front]
        self._front = (self._front + 1) % len(self._qarray)
        self._count -= 1
        return item

    def is_empty(self):
        """
        returns True if the queue is empty, False Otherwise.
        """
        return self._count == 0

    def is_full(self):
        """
        returns True if the queue is full, False Otherwise.
        """
        return self._count == len(self._qarray)

    def __len__(self):
        """
        overloads len() function.
        returns queue's size.
        """
        return self._count