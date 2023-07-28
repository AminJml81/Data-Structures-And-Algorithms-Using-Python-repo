class _LinearBagIterator:

    def __init__(self, items):
        self._elements = items
        self._cur_inx = 0

    def __next__(self):
        if self._cur_inx < len(self._elements):
            item = self._elements[self._cur_inx]
            self._cur_inx += 1
            return item
        else:
            raise StopIteration

    def __iter__(self):
        return self


class _CountingBagIterator(_LinearBagIterator):

    def __init__(self, items):
        super().__init__(items)
        self._elements_keys = list(items.keys())

    def __next__(self):
        if self._cur_inx < len(self._elements_keys):
            key = self._elements_keys[self._cur_inx]
            value = self._elements[key]
            self._cur_inx += 1
            return key, value
        else:
            raise StopIteration
