class Stack:
    """
    class to represent Stack(LIFO Data Structure) using python list.

    attributes:
    -----------
                items: python list
                      items are stored in the python list.

    methods:
    --------
            push(item):
                      pushes the item to the head of the stack.
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
        initializing stack using python list.
        """
        self.items = list()

    def push(self, item):
        """
        adds the item to the top of stack if item is not empty.

        parameters:
        ----------
                 item: int
                     item to be added to the stack.
        returns None
        """
        assert item, 'item parameter is not provided.'
        self.items.append(item)

    def pop(self):
        """
        removes top most element from the stack and returns it's value.

        returns the top most element of the stack.
        """
        assert not self.is_empty(), 'Stack is Empty!'
        return self.items.pop()

    def peek(self):
        """
        returns the stack's top most element if the stack is not empty:
        """
        assert not self.is_empty(), 'Stack is Empty!'
        return self.items[-1]

    def is_empty(self):
        """
        returns True if the stack is empty, False Otherwise.
        """
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(list(reversed(self.items)))
