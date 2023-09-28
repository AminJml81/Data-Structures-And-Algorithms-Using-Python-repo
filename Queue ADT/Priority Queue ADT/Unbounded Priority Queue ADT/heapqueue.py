class PriorityQueue:
    """
        <Min Heap Unbounded Priority Queue>
        class to represent unbounded priority queue(FIFO) Data Structure using Min Heap.

        attributes:
        -----------
                    _items: list
                            items are stored in python list.
                    _count: int
                            keeps record of the number of items in the tree.
        methods:
        --------

                    enqueue(item):
                                  adds new item to the end of the queue.

                    dequeue():
                              removes first Node from the queue and returns it's element.

                    _sift_up():
                                moves node upside until it's parent's item is smaller than it's item.

                    _sift_down():
                                moves node downside until it's item is smaller than both of it's children's items.


        """

    def __init__(self):
        """
        initializes heap with list.
        """
        self._items = list()
        self._count = 0

    def enqueue(self, value: any, priority: int):
        """
        adds the item to the tree.
        # Note: after insertion the heap order property and shape property of the heap must be maintained.
        it attaches the new item to the lowest level leftmost part of the tree. then it compares the item with it's
        parent. if the item is bigger than parent's item, it swaps it with parent's item and continues this action until
        the node's item is bigger than it's parent's node.

        # Note: this process is called sifting up.

        parameters:
        ------------
                    item: any

                    # Note: type of items must be the same in max heap.

        """
        new_entry = _QueueItem(value, priority)
        self._items.append(new_entry)
        self._count += 1
        self._sift_up()

    def dequeue(self):
        """
        removes heap's root which has the highest priority and returns its item.
        # Note: after extraction the heap order property and shape property of the heap must be maintained.
        it removes the tree's root and returns it and removes the rightmost leaf from the lowest level and replaces with
        the root and compares it's item with both of it's children. if it's value is smaller than it's children, it
        swaps it with the bigger one.

        # Note: this process is called sifting down.

        returns tree's root's item(first item in the list).
        """
        assert self._count != 0, 'The Heap Is Empty'
        item = self._items.pop(0)
        self._count -= 1
        if self._count > 0:
            # if there is only one item in the heap, sifting up is not required.
            self._items.insert(0, self._items.pop())
            self._sift_down()
        return item.value

    def _sift_up(self):
        """
        it calculates the indexes and compares each child with its parent.
        if it is smaller than it's parent it swaps it and continues comparing until the parent's priority is smaller.

        returns None
        """
        index = len(self._items) - 1
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self._items[index].priority < self._items[parent_index].priority:
            self._items[index], self._items[parent_index] = self._items[parent_index], self._items[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self):
        """
        it calculates the indexes and compares each node's priority with its children.
        if it is larger than it's children it swaps it with the smaller child and continues comparing until it reaches
        the leaf or node's item which it's priority is smaller than it's children.

        return None
        """
        index = 0
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        try:
            while self._items[index].priority > self._items[left_child].priority or\
                    self._items[index].priority > self._items[right_child].priority:
                if self._items[left_child].priority <= self._items[right_child].priority:
                    self._items[index], self._items[left_child] = self._items[left_child], self._items[index]
                    index = left_child
                else:
                    self._items[index], self._items[right_child] = self._items[right_child], self._items[index]
                    index = right_child

                left_child = 2 * index + 1
                right_child = 2 * index + 2

        except IndexError:
            return

    def traverse(self):
        for i in range(self._count):
            print(self._items[i].value, self._items[i].priority)


class _QueueItem:
    """
    class to represent queue's item.

    attributes:
    -----------
                priority: int
                          item's priority.
                value: int
                        item's value.
    """

    def __init__(self, value, priority):
        self.priority = priority
        self.value = value


if __name__ == '__main__':
    a = PriorityQueue()
    a.enqueue('white', 0)
    a.enqueue('black', 1)
    a.enqueue('green', 1)
    a.enqueue('orange', 3)
    a.enqueue('purple', 5)
    a.enqueue('yellow', 5)

    a.traverse()