class Stack:
    """
        class to represent Stack(LIFO Data Structure) using linked list.
        stack top is linked list head.
        attributes:
        -----------
                    _top: Node
                          stack top node
                    _size: int
                          stack size

        methods:
        --------
                push(item):
                          push the item to the head of the stack (linked list prepend)
                pop():
                      removes the last element that was pushed into stack and returns it's value.
                peek():
                       shows the stack's top most element.
                is_empty():
                           returns true if the stack is empty and false otherwise.
                __len__():
                         returns stack's size.
                __str__():
                         returns string representation of the stack.

                Note: both peek and pop operation cannot be done on empty stack.

        """

    def __init__(self):
        """
        initializes stack which _top is None and _size is 0.
        """
        self._top = None
        self._size = 0

    def push(self, item):
        """
        pushes item to the top of the stack.
        makes new node and passes the current top node for it's next reference.
        updates top reference.

        parameters:
        ----------
                 item: item to be added to the stack if it is not empty
        returns None
        """
        assert item, 'item parameter is not provided.'
        # (
        self._top = _StackNode(item, self._top)
        self._size += 1

    def pop(self):
        """
        removes stack top most element and returns it if it is not empty.
        returns stack's top most element.
        """
        assert not self.is_empty(), 'stack is empty'
        item = self._top.data
        self._top = self._top.next
        self._size -= 1
        return item
    # ) )

    def peek(self):
        """
        returns stack top most element if the stack is not empty.
        """
        assert not self.is_empty(), 'stack is empty'
        return self._top.data

    def is_empty(self):
        """
        returns True if the stack is empty, False otherwise.
        """
        return self._size == 0

    def __len__(self):
        """
        overloading len function.

        returns the len of the given stack.
        """
        return self._size

    def __str__(self):
        items = ''
        current_node = self._top
        while current_node:
            items += f" {self._top.data} "
            current_node = current_node.next
        return items.strip()


class _StackNode:
    """
    class to represent Stack Nodes

    attributes:
    -----------
    data: int
        node's data.
    next: _StackNode
        node's next node reference.
    """

    def __init__(self, data, link):
        self.data = data
        self.next = link
