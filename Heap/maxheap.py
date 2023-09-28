class MaxHeap:
    """
    class to represent Max Heap using python list.
    in this implementation if node's index is i:
                                                (i-1)//2 is it's parent index.
                                                2*i + 1 is it's left child.
                                                2*i + 2 is it's right child.

    attributes:
    -----------
                _items: list
                        items are stored in python list.
                _count: int
                        keeps record of the number of items in the tree.
    methods:
    --------
                insert(item):
                            inserts item to the max heap.

                extract():
                            removes max heap root and returns it's item.

                _sift_up():
                            moves node upside until it's parent's item is bigger than it's item.

                _sift_down():
                            moves node downside until it's item is bigger than both of it's children's items.

                traverse():
                            traverses the whole heap in a Breath First way(level by level).

                search(item):
                         searches for the given item in the heap.

                __len__():
                          return number of items in the heap.

                __contains__(item):
                                returns True if the item is in the Heap, False otherwise.
    """

    def __init__(self):
        """
        initializes heap with list.
        """
        self._items = list()
        self._count = 0

    def insert(self, item: any):
        """
        adds the item to the tree.
        # Note after insertion the heap order property and shape property of the heap must be maintained.
        it attaches the new item to the lowest level leftmost part of the tree. then it compares the item with it's
        parent. if the item is bigger than parent's item, it swaps it with parent's item and continues this action until
        the node's item is bigger than it's parent's node.

        # Note: this process is called sifting up.

        parameters:
        ------------
                    item: any

                    # Note: type of items must be the same in max heap.

        """
        self._items.append(item)
        self._count += 1
        self._sift_up()

    def extract(self):
        """
        removes heap's root's item and returns it's item.
        # Note after extraction the heap order property and shape property of the heap must be maintained.
        it removes the tree's root and returns it and removes the rightmost leaf from the lowest level and replaces with
        the root and compares it's item with both of it's children. if it's value is smaller than it's children, it
        swaps it with the bigger one.

        # Note: this process is called sifting down.

        returns tree's root(first item in the list).
        """
        assert self._count != 0, 'The Heap Is Empty'
        item = self._items.pop(0)
        self._count -= 1
        if self._count > 0:
            # if there is only one item in the heap, sifting up is not required.
            self._items.insert(0, self._items.pop())
            self._sift_down()
        return item

    def _sift_up(self):
        """
        it calculates the indexes and compares each child with its parent.
        if it is bigger than it's parent it swaps it and continues comparing until the parent's item is larger.
        returns None
        """
        index = len(self._items) - 1
        parent_index = (index - 1) // 2
        while parent_index >= 0 and self._items[index] > self._items[parent_index]:
            self._items[index], self._items[parent_index] = self._items[parent_index], self._items[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _sift_down(self):
        """
        it calculates the indexes and compares each node with its children.
        if it is smaller than it's children it swaps it with the larger child and continues comparing until it reaches
        the leaf or node's item is larger than it's children.
        return None
        """
        index = 0
        left_child = 2 * index + 1
        right_child = 2 * index + 2
        try:
            while self._items[index] < self._items[left_child] or self._items[index] < self._items[right_child]:
                if right_child >= self._count or self._items[left_child] >= self._items[right_child]:
                    # if right child doesnt exist or it exists but it's value is larger than it's left sibling
                    # swap item with it's left child.
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
        """
        prints all items of the tree level by level(Breadth First Traverse).
        returns None
        """
        for i in range(self._count):
            print(self._items[i])

    def search(self, item):
        """
        searches for item in min heap.
        parameters:
        -----------
                    item: any
                          item to search for
        returns True if item is in the heap False otherwise.
        """
        if self._count > 0 and item > self._items[0]:
            return False
        return item in self._items

    def __len__(self):
        """ returns number of items in the heap."""
        return self._count

    def __contains__(self, item):
        """ returns True if item is in the heap False otherwise. """
        return item in self._items
