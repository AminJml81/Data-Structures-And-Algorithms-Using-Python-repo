# you can use this bag as a container besides it holds the number of each item repetition.

from _Bagiterator import _LinearBagIterator, _CountingBagIterator
from linearbag import Bag


class CountingBag(Bag):

    def __init__(self):
        self._items = dict()

    def add(self, element):
        if element in self._items.keys():
            self._items[element] += 1
        else:
            self._items[element] = 1

    def remove(self, item):
        assert item in self._items.keys(), f'{item} is not in the bag'
        count = self._items[item]
        if count == 1:
            del self._items[item]
        else:
            self._items[item] -= 1

    def __iter__(self):
        return _CountingBagIterator(self._items)

