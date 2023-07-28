class LinkedListIterator:

    def __init__(self, head_reference):
        self.current_node = head_reference

    def __next__(self):
        if self.current_node:
            item = self.current_node.data
            self.current_node = self.current_node.next
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self
