class Queue:
    """
    Linked List Queue.
    class to represent queue(FIFO) Data Structure using Linked list with head and tail references.

    attributes:
    -----------
                _head: reference
                       queue's front Node. The Node to remove item.
                       initially set to None.

                _tail: reference
                      queue's back Node. The Node to add new item.
                      initially set to None.

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
                __len__():
                         returns queue's size.
    """

    def __init__(self):
        """
        initializes queue by making head and tail references which both of them are initially None.
        """
        self._head = None
        self._tail = None
        self._count = 0

    def enqueue(self, item):
        """
        it creates new node and add the new item to the queue and updates tail reference.
        parameters:
        ---------
                  item: obj
                       item to be added to the queue.

        returns None

        worst time complexity of O(1).
        """
        new_node = _QueueNode(item)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._count += 1

    def dequeue(self):
        """
        if the queue is not empty ,it gets the item from the head of the queue then it updates the head reference.

        returns item that was removed from the queue.

        worst time complexity of O(1).
        """
        assert not self.is_empty(), 'Cannot Dequeue from an empty queue.'
        item = self._head.item
        self._head = self._head.next
        return item

    def is_empty(self):
        """
        returns True if the queue is empty, False Otherwise.
        """
        return self._head is None

    def __len__(self):
        """
        returns total number of items in the queue.
        """
        return self._count


class _QueueNode:
    """
    class to represent queue's node.

    attributes:
    -----------
                item: obj
                        item to be added to the queue.
                next : Node
                        next's Node reference.
    """
    def __init__(self, item):
        self.item = item
        self.next = None
