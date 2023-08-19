class DoubleLinkedList:
    """
    class to represent sorted doubly linked list using both head and tail references.
    Doubly Linked List contains previous and next references.

    Attributes:
    ----------
    _head : Node
         corresponds to the head of list.
    _tail: Node
          corresponds to the tail of list.
    _probe: Node
          corresponds to the last searched node(usable for searching or deleting item from linked list).

    Methods:
    -------
    front_traversal():
                      traverses linked list from head to the tail.
    tail_traversal():
                     traverses Linked List from tail to the head.
    search(item):
                     searches linked list for the given item.
    insert(item):
                    inserts item into the linked list.
    remove_item(item):
                    removes the item from the linked list.
    _initialize_list(new_node):
                                adds the first new node to the linked list.
    _prepend_item(new_node):
                                adds the new node to the head of the linked list.
    _append_item(new_node):
                                adds the new node to the tail of the linked list.
    _insert_in_the_middle(new_node):
                                inserts the new node into the middle of the linked list.

    # Note: Type of the data of each node must be same.
    """

    def __init__(self):
        """
        initializes linked list with all parameters set to None.
        """
        self._head = None
        self._tail = None
        self._probe = None

    def front_traversal(self):
        """
        traverse the linked list from head to the tail of the linked list.

        return None
        """
        current_node = self._head
        if current_node is None:
            return None
        while current_node:
            print(current_node, end=' ')
            current_node = current_node.next
        print()

    def tail_traversal(self):
        """
        traverse the linked list from tail to the head of the linked list.

        returns None
        """
        current_node = self._tail
        if current_node is None:
            return None
        while current_node:
            print(current_node, end=' ')
            current_node = current_node.prev
        print()

    def search(self, item):
        """
        searches the linked list for the given item.

        since the linked list is sorted by using _probe reference which corresponds to the last item that was searched,
        if the probe is not None(we used search method before):
            if the item is smaller than the probe item, it searches backward
            if it is larger, it searches forward
            otherwise it is the item so ir return True

        else it assigns it to the _head reference.

        parameters:
        ----------
                  item: int
                        item to search for in the list.

        returns True if the item is in the list False Otherwise.
        """
        assert item is not None, 'item parameter is not provided.'

        if self._head is None:
            return False

        if item < self._head.data or item > self._tail.data:
            return False

        if self._probe:
            if self._probe.data > item:
                return self._search_backward(item)

            elif self._probe.data < item:
                return self._search_forward(item)

            else:
                return True
        else:
            if self._head:
                self._probe = self._head
                return self.search(item)
            else:
                return False

    def _search_backward(self, item):
        """
        searches from probe reference to the head reference.

        parameters:
        ----------
                    item: int
                          item to search for in the list.

        return True if it finds the item, False otherwise.
        """
        while self._probe and self._probe.data > item:
            self._probe = self._probe.prev
        return self._probe.data == item

    def _search_forward(self, item):
        """
            searches from probe reference to the tail reference.

            parameters:
            ----------
                        item: int
                              item to search for in the list.

            return True if it finds the item, False otherwise.
        """
        while self._probe and self._probe.data < item:
            self._probe = self._probe.next
        return self._probe.data == item

    def insert(self, item):
        """
            inserts item in the linked list.

            parameters:
            ----------
                        item: int
                              item to insert into the list.

            return None.
            """
        assert item is not None, 'item parameter is not provided.'
        new_node = _Node(item)
        if self._head is None:
            self._initialize_list(new_node)

        elif item <= self._head.data:
            self._prepend_item(new_node)

        elif item >= self._tail.data:
            self._append_item(new_node)

        else:
            self._insert_in_the_middle(new_node)

    def _initialize_list(self, new_node):
        """
        adds the new node to the head of the linked list.(the linked list was empty before.)
        parameters:
                   new_node: Node

        returns None
        """
        self._head = new_node
        self._tail = new_node

    def _prepend_item(self, new_node):
        """
        adds the new node the front side of the linked list.

        parameters:
        -----------
                    new_node: node

        returns None
        """
        new_node.next = self._head
        self._head.prev = new_node
        self._head = new_node

    def _append_item(self, new_node):
        """
        adds the new node the tail side of the linked list.

        parameters:
        -----------
                    new_node: node

        returns None
        """
        new_node.prev = self._tail
        self._tail.next = new_node
        self._tail = new_node

    def _insert_in_the_middle(self, new_node):
        """
        adds the new node in the middle of the linked list (regarding to it's correct position).

        parameters:
        -----------
                    new_node: node

        returns None
        """
        current_node = self._head
        while current_node and current_node.data < new_node.data:
            current_node = current_node.next
        new_node.prev = current_node.prev
        new_node.next = current_node
        current_node.prev.next = new_node
        current_node.prev = new_node

    def remove_item(self, item):
        """
        removes the item from the linked list.
        parameters:
        -----------
                    item: int
                        item to remove from the the list.

        returns None
        """
        assert item is not None, 'item parameter is not provided.'
        assert self.search(item) is True, 'item is not in the list.'
        if self._head.data == item:
            # if the list contains only one item and that item is going to remove from the list.
            if self._head == self._tail:
                self._tail = None
            self._head = self._head.next
            if self._head:
                self._head.prev = None

        else:
            current_node = self._head
            while current_node != self._probe:
                current_node = current_node.next
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            current_node = None
        self._probe = None


class _Node:
    """
    class To Represent a Node in a doubly linked list which has both next and previous references.

    attributes:
    -----------
    data: any
            node's data.
    next: Node
            node's next reference.
    prev: Node
            node's previous reference.
    """
    def __init__(self, data):
        """
        initializes Node.

        parameters:
        -----------
                    data: any
                        node's data.
                    prev: reference
                         previous reference
                    next: reference
                         next reference
        """
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        """return data part of the node."""
        return f'{self.data}'
