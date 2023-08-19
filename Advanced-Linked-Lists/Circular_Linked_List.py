class CircularLinkedList:
    """
    class to represent sorted doubly circular linked list using both head and tail references.

    Circular Linked List is like other linked lists but the only difference is that the next field of the last node
    points to the first node and the previous field of the first node points to the last node.

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
    traverse():
                traverses linked list from head to the tail(head again :) ).

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

    def traverse(self):
        """
        traverse the linked list from head to the tail of the linked list.

        condition checks if it traverses the list once or not.

        return None
        """
        current_node = self._head
        condition = self._head is not None
        if condition is False:
            return None
        # if the list is empty, the loop doesn't execute.
        while condition:
            print(current_node, end=' ')
            current_node = current_node.next
            condition = current_node is not None and current_node != self._head
        print()

    def search(self, item):
        """
        searches the entire list for the given item.

        parameters:
        -----------
                    item: int

        returns None
        """
        assert item is not None, 'item parameter is not provided.'

        if self._head is None or self._tail is None:
            return False

        if item < self._head.data or item > self._tail.data:
            return False

        if self._probe is None:
            self._probe = self._head

        if item < self._probe.data:
            return self._search_backward(item)

        if item > self._probe.data:
            return self._search_forward(item)
        # probe reference links to the item.
        return True

    def _search_backward(self, item):
        """
        searches from probe reference to the head reference.

        parameters:
        ----------
                    item: int
                          item to search for in the list.

        return True if it finds the item, False otherwise.
        """
        condition = self._head is not None
        while self._probe and self._probe.data > item and condition:
            self._probe = self._probe.prev
            condition = self._probe is not self._head
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
        condition = self._head is not None
        while self._probe and self._probe.data < item and condition:
            self._probe = self._probe.next
            condition = self._probe is not self._tail
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
        new_node.prev = self._tail
        self._head.prev = new_node
        self._tail.next = new_node
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
        new_node.next = self._head
        self._tail.next = new_node
        self._head.prev = new_node
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
            # if the item is the first item in the list.
            if self._head == self._tail:
                # if the list contains only one item.
                self._head, self._tail = None, None

            else:
                self._head = self._head.next
                self._head.prev = self._tail
                self._tail.next = self._head

        elif self._tail.data == item:
            # if the item is the last item in the list.
            self._tail = self._tail.prev
            self._tail.next = self._head
            self._head.prev = self._tail

        else:
            current_node = self._head
            while current_node != self._probe:
                # this method calls search method first so the probe reference is pointing to the item.
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
