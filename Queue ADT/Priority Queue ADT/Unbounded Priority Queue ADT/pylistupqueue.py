class PriorityQueue:
    """
    <Python List Unbounded Priority Queue>
    class to represent Unbounded Priority Queue using python list.

    Priority Queues are FIFO Data Structure same as Queue with a main difference which items in the queue
    have priorities and items with higher priorities(which have lower priority number) will dequeue first and
    if multiple items have the same priority, the item that was enqueued first will get dequeued first.

    In Unbounded Priority Queues items can get any priority number in the range [0, +inf).

    attributes:
    -----------
              _qlist: python list
                     items are stored in a python list.

    methods:
    --------

                enqueue(item):
                              makes new entry, appends it to the end of the list.

                dequeue():
                          searches for the item with highest priority, removes its entry from the queue and returns it's
                          item.

                is_empty():
                           returns True if the queue is empty.

                __len()--:
                          returns queue's size.
    """

    def __init__(self):
        """
        initializes priority queue with python list.
        """
        self._qlist = list()

    def enqueue(self, item, priority):
        """
        making new entry with given parameters and append it to the end of the queue.
        parameters
        ----------
                    item: obj
                         entry's item to be added to the queue.
                    priority: int
                             entry's priority to be added to the queue.
        returns None

        # Note: enqueue operation have worst time complexity of O(n) (list expansion) and amortized O(1).

        """
        new_entry = _PriorityQEntry(item, priority)
        self._qlist.append(new_entry)

    def dequeue(self):
        """
        if the queue is not empty it finds the item with highest priority and removes it.

        returns item with highest priority.

        # Note: dequeue have wost time complexity of O(n) which is the case that the item with highest priority
        #       is the last queue's element.

        """
        assert not self.is_empty(), 'Cannot dequeue from an empty queue.'
        max_priority = self._qlist[0].priority
        max_index = 0
        for index, entry in enumerate(self._qlist):
            if entry.priority < max_priority:
                max_priority = entry.priority
                max_index = index
        highest_priority_entry = self._qlist.pop(max_index)
        return highest_priority_entry.item

    def is_empty(self):
        """
        returns True if the queue is empty, False otherwise.
        """
        return len(self) == 0

    def __len__(self):
        """
        returns size of the queue.:
        """
        return len(self._qlist)


class _PriorityQEntry:
    """
    storage class for associating queue items with their priorities.

    attributes:
    ----------
              item: obj
                   object to be added to the queue.
              priority: int
                    object priority.
    """
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority