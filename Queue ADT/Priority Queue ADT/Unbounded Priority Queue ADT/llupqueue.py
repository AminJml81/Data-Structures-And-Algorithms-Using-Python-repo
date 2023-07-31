class PriorityQueue:
    """
    <Linked List Unbounded Priority Queue>
    class to represent unbounded priority queue(FIFO) Data Structure using Linked list with head and tail references.

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

                _find_highest_priority_node():
                                              helper method to find the highest priority.

                is_empty():
                           returns True if the queue is empty.

                __len__():
                         returns the size of the queue.
    """

    def __init__(self):
        """
        initializes queue by making head and tail references which both of them are initially None.
        """
        self._head = None
        self._tail = None
        self._count = 0

    def enqueue(self, item, priority):
        """
        if the queue is not full, it creates new node and add the new item to the end of the queue
        and updates tail reference.

        parameters:
        ---------
                  item: obj
                       item to be added to the queue.
                  priority: int
                            item's priority number.

        returns None

        worst time complexity of O(1).

        """
        new_node = _QueueNode(item, priority)
        if self.is_empty():
            self._head = new_node
        else:
            self._tail.next = new_node

        self._tail = new_node
        self._count += 1

    def dequeue(self):
        """
        if the queue is not empty ,by help of_find_highest_priority_node() method it finds the highest priority number
        in the queue and then it traverse the queue until it finds that priority then it gets it's item and removes
        it from the queue.

        returns item with highest priority.

        worst time complexity of O(n).(worst case is when the item with highest priority is the last item in the queue).
        """
        assert not self.is_empty(), 'Cannot Dequeue from an empty queue.'
        max_priority = self._find_highest_priority_node()
        previous_node = None
        current_node = self._head
        while current_node and current_node.priority != max_priority:
            previous_node = current_node
            current_node = current_node.next

        if previous_node is None:
            item = current_node.item
            self._head = current_node.next
        else:
            item = current_node.item
            previous_node.next = current_node.next
        self._count -= 1
        return item

    def _find_highest_priority_node(self):
        """
        returns the highest priority in the queue.
        """
        max_priority = self._head.priority
        current_node = self._head.next

        while current_node:
            if current_node.priority < max_priority:
                max_priority = current_node.priority
            current_node = current_node.next

        return max_priority

    def is_empty(self):
        """
        returns True if the queue is empty, False otherwise.
        """
        return self._head is None

    def __len__(self):
        """
        returns size of the queue.
        """
        return self._count


class _QueueNode:
    """
    class to represent queue's node.

    attributes:
    -----------
                item: obj
                     item to be added to the queue.
                priority: int
                         item's priority.
                next: Node
                     next's Node reference.
    """
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None
