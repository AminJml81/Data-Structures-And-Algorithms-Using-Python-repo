# A simple or linear bag is a container which you can add the elements to it
# but it does not keep orders and also the duplicates are allowed.
from _Bagiterator import _LinearBagIterator


class Bag:
    # implementing bag using python list.
    def __init__(self):
        self._items = list()

    def add(self, item):
        self._items.append(item)

    def remove(self, item):
        assert item in self._items, f"{item} Is Not In The Bag. "
        inx = self._items.index(item)
        self._items.pop(inx)

    def __contains__(self, item):
        return item in self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return _LinearBagIterator(self._items)

