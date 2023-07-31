class Queue:
    """
    Python List Queue
    class to represent queue(FIFO) Data Structure using python list.

    attributes:
    -----------
                _qlist: python list
                      items are stored in a python list.
    methods:
    --------

                enqueue(item):
                              adds new item to the end of the list.

                dequeue():
                          removes first element from the list and returns the element.

                is_empty():
                           returns True if the queue is empty.

                __len()--:
                          returns queue's size.

    """

    def __init__(self):
        """
        initializes queue with python list.
        """
        self._qlist = list()

    def enqueue(self, item):
        """
        parameters:
        -----------
                    item: obj
                        item to be added to the queue.
        returns None

        # Note worst time complexity of O(n) (python list resizing) and amortized  O(1).
        """
        self._qlist.append(item)

    def dequeue(self):
        """
        if the queue is not empty, it removes the first item of the list and returns its value.

        returns the item that was dequeued

        # Note worst time complexity of O(n) (python list resizing) and amortized  O(1).
        """
        assert not self.is_empty(), 'Cannot deque from an empty queue.'
        return self._qlist.pop(0)

    def is_empty(self):
        """
        return True if the queue is empty, False otherwise:
        """
        return len(self._qlist) == 0

    def __len__(self):
        """
        overloads len() function.
        returns queue's size.
        """
        return len(self._qlist)
