from Linked_List_Iterator import LinkedListIterator


class LinkedList:
    """
    a class to represent a linked list.

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
    prepend(item):
                      adding the element to the head of list
    append(item):
                      adding the element to the tail of list
    print_elements():
                      prints All elements
    remove(item):
                     removing item from list
    is_empty():
              checks if the list is empty or not
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

    def prepend(self, item):
        """
        adding the item to the head of list
        parameters
        ----------
        item : int
             item to be appended at the head of linked list

        returns None:
        """
        assert item is not None, "there's no item to prepend it"
        new_node = _Node(item)
        new_node.next = self._head
        self._head = new_node
        if self._tail is None:
            self._tail = self._head
        self._size += 1

    def append(self, item):
        """
        adding item to the tail of the list.
        parameters
        ----------
        item : int
             item to be appended at the tail of linked list

        returns None:
        """
        assert item is not None, "there's no item to append it"
        new_node = _Node(item)
        if self._head is None:
            self._head = new_node

        if self._tail is None:
            self._tail = new_node

        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

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
        removing data from linked list
        one of the following conditions might happen:
            0) item is not provided
            1) the linked list might be empty
            2) the item might be the first element in the list
            3) the item might be the last element in the list
            4) the item might be somewhere else in the list
            5) the item might not even be in the list

        # Note: since if the item is in the list we need to modify it's previous node next reference
                besides current node we must keep track of previous node. so we need two variables.
        parameters
        ----------
        item: int
            item to be removed from the list
        returns None:
        """
        assert item is not None, "there's no item to remove it"
        # this assert statement checks for condition 0.
        assert not self.is_empty(), f'list is empty!!!'
        # this assert statement checks for condition 1.

        current_node = self._head
        previous_node = None

        while current_node and current_node.data != item:
            previous_node = current_node
            current_node = current_node.next

        assert current_node is not None, f"{item} must be in the list"
        # this assert statement checks for condition 5.

        if current_node == self._head:
            # condition 2
            self._head = current_node.next

        elif current_node == self._tail:
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
        parameters
        ----------
        item : int
            item to be searched in the list
        returns True if the item is in the list, False Otherwise. :
        """

        tmp_node = self._head
        while tmp_node and tmp_node.data != item:
            # traversing the list
            tmp_node = tmp_node.next
        return tmp_node is not None

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
