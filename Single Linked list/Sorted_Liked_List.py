from Linked_List_Iterator import LinkedListIterator


class SortedLinkedList:
    """
    a class to represent a sorted linked list.
    it is similar to linked list but it has only insert method istead of append and prepend methods
    and there is a little difference in the remove method.

    Attributes
    ---------
    _head : Node
         corresponds to the head of list
    _tail: Node
          corresponds to the tail of list
    _size : int
         corresponds to the size of list

    Methods
    -------
    insert(item):
                 inserting element to it's right position
    print_elements():
                     prints All elements
    remove(item):
                 removing item from list
    is_empty():
               checks if the list is empty or not
    _prepend(item):
                   adding the item to the head of list
    _append(item):
                 adding the item to the tail of list
    __contain__(item):
                      overloads in operator which checks if item is in the list
    __len__():
             returns the size of the list.
    __iter__():
        returns iterator


    """
    def __init__(self):
        """
        initializes a linked list which head and tail attributes are None and size is zero
            at the beginning of the initialization.
        """
        self._head = None
        self._tail = None
        self._size = 0

    def insert(self, item):
        """
        inserting item to it's right position in the list.
        conditions:
                  0) item might not be provided
                  1) list might be empty
                  2) item is smaller than all of the list elements
                   which means it is smaller or equal than data in the head node
                   which we pass the item to the _append method

                  3) item is larger than all of the list elements
                   which means it is larger or equal than data in the tail node
                   which we pass the item to the _prepend method

                  4) item must be inserted somewhere in the middle
        the algorithm for the first three condition is straightforward
        but for the fourth condition we need to find the correct position

        parameter
        ---------
         item:  int
          item that must be inserted in the list
        returns None:
        """
        assert item is not None, "there's no item to append it"
        # this assert statement checks for condition 0
        if self.is_empty():
            # condition 1
            new_node = _Node(item)
            self._head, self._tail = new_node, new_node

        elif item <= self._head.data:
            # condition 2
            self._prepend(item)

        elif item >= self._tail.data:
            # condition 3
            self._append(item)

        else:
            new_node = _Node(item)
            current_node = self._head.next
            previous_node = self._head
            while current_node.data < item:
                previous_node = current_node
                current_node = current_node.next
            new_node.next = current_node
            previous_node.next = new_node
        self._size += 1

    def _prepend(self, item):
        """
        adding the item to the head of list
        parameters
        ----------
        item : int
             item to be appended at the head of linked list

        returns None:
        """
        new_node = _Node(item)
        new_node.next = self._head
        self._head = new_node

    def _append(self, item):
        """
        adding item to the tail of the list.
        parameters
        ----------
        item : int
             item to be appended at the tail of linked list

        returns None:
        """
        new_node = _Node(item)
        self._tail.next = new_node
        self._tail = new_node

    def print_elements(self):
        """
        prints All elements

        returns None:
        """
        assert not self.is_empty(), f'list is empty!!!'
        tmp_node = self._head
        while tmp_node:
            print(tmp_node.data)
            tmp_node = tmp_node.next

    def remove(self, item):
        """
        removing the given item from linked list
        one of the following conditions might happen:
            0) item might not be provided
            1) the linked list might be empty
            2) the item might be the first element in the list
            3) the item might be the last element in the list
            4) the item might be somewhere else in the list
            5) the item might not even be in the list

        since the list is sorted we can realize faster, if the item is in the list or not.
        if the item is less than head data or larger than he tail data it is guaranteed that it's not in the list.

        # Note: if the item is the last item we must traverse
         from the list head to find the previous node next reference (same as other positions)
         but we must update the tail reference.

        parameters
                item (int):
        returns None:
        """
        assert item is not None, "there's no item to append it"
        # this assert statement checks for condition 0
        assert not self.is_empty(), f'list is empty!!!'
        # this assert statement checks for condition 1.

        assert not (item < self._head.data or item > self._tail.data), f'{item} is not in the list'
        # this assert statement checks some part of condition 5

        if item == self._head.data:
            # condition 2
            self._head = self._head.next

        else:
            # we need to traverse the list to find out whether the item is in the list or not.
            current_node = self._head.next
            previous_node = self._head

            while current_node and current_node.data < item:
                previous_node = current_node
                current_node = current_node.next

            assert current_node is not None, f"{item} must be in the list"
            # this assert statement checks for condition 5.

            if current_node == self._tail:
                # condition 3
                self._tail = previous_node
                previous_node.next = None

            else:
                # condition 4
                previous_node.next = current_node.next
                current_node = None

        self._size -= 1

    def is_empty(self):
        """
        returns True if the list is empty:
        """
        return self._size == 0

    def __contains__(self, item):
        """
        overloading in operator
        if item is smaller than the head data or larger than tail data it is not in the list.
        since we have head and tail reference, we check their data without traversing.
        if item is in the list the tmp node must not be None and also it's data is equal to the item.
        parameters
        ----------
        item : int
            item to be searched in the list
        returns True if the item is in the list, False Otherwise. :
        """
        if item < self._head.data or item > self._tail.data:
            # it is not in the list
            return False

        if self._head.data == item or self._tail.data == item:
            # it is tail or head
            return True

        tmp_node = self._head.next
        while tmp_node and tmp_node.data < item:
            # traversing the list to find the item
            tmp_node = tmp_node.next
        # if tmp is None it is not in the list and also
        # if the tmp.data is not equal to the item it is not in the list
        # so it return False otherwise it return True
        return tmp_node is not None and tmp_node.data == item

    def __len__(self):
        """
        overloading len() function
        returns the size of the linked list:
        """
        return self._size

    def __iter__(self):
        return LinkedListIterator(self._head)


class _Node:
    """
    a class to represent a Node

    Attributes
    ---------
    data : int
        data part of the node.
    next :Node
        a reference to the next node
    """
    def __init__(self, data):
        """
        initializes a node

        parameters
        ----------
        data: int
            data part of the node
        """
        self.data = data
        self.next = None
