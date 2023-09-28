class HashMap:
    """
    class to represent hashmap using python list.

    attributes:
    -----------
                _table: python list
                        hashtable
                _count: int
                        number of keys in the hashtable
                _max_count: int
                            maximum number of item which is 2/3 of table size.
    methods:
    --------
            add(key, value):
                            finds the slot for given key, and it either updates or add the given value to the
                            calculated slot.

            get(key):
                     returns value of the given key, if it is in the hashtable.

            remove(key):
                        removes the value of given key if it is in the hashtable and replaces $ with it.

            find_slot(self, key, for_insert):
                        finds slot for given key.

            _search(key):
                        searches if the key is in the hashmap or not.
            _rehash():
                        rehash the entire hashtable if the _max_count is reached.
            _hash1(key):
                        hashes key for finding slot.
            _hash2(key):
                        hashes key for finding step
            __len__():
                        overloads len() function.
            __contains__(key):
                        overloads key in hashmap.
            __getitem__(key):
                        overloads hashmap[key].
            __setitem__(key, value):
                        overloads hashmap[key] = value.
            __iter__():
                        returns iterator for hashmap.


    """
    def __init__(self):
        """
        initializes HashMap with the size of the 7 and load factor of 2/3.
        """
        self._table = [None for i in range(7)]
        self._count = 0
        self._max_count = len(self._table) - (len(self._table)//3)

    def add(self, key, value):
        """
        if the key is already in the hashtable, it updates it's value with the new value.
        otherwise it adds new entry with the given key, value.
        parameters:
        ----------
                    key: any
                         data key
                    value: any
                          data value

        returns None
        """
        if key in self:
            slot = self.find_slot(key, False)
            self._table[slot].value = value
        else:
            slot = self.find_slot(key, True)
            self._table[slot] = _MapEntry(key, value)
            self._count += 1
            if self._count == self._max_count:
                self._rehash()

    def get(self, key: any):
        """
        parameters:
        ----------
                    key: any
                         data key
        returns value of the given key.
        """
        slot = self.find_slot(key, False)
        assert slot is not None, "Invalid key"
        return self._table[slot].value

    def remove(self, key: any):
        """
        removes the given key and it's value from hashmap and add $ symbol.
        parameters
        ----------
                    key: any
                         data key
        returns None
        """
        assert self._search(key) is True, "Invalid key."
        slot = self.find_slot(key, False)
        self._table[slot] = '$'

    def find_slot(self, key: any, for_insert: bool):
        """
        Finding Slot is the main operation in HashMap Abstract Data Type.
        if for_insert is False, it is for updating or removing operation.(the key must be in the hashtable)
        if it is True, it is for inserting operation.(the key is new)

        parameters:
        -----------
                    key: any
                        data key
                   for_insert: bool
                               insertion flag which if it is True it return the first None or $ slot.
                               otherwise it returns the given key's slot.
        returns slot
        """
        slot = self._hash1(key)
        step = self._hash2(key)
        M = len(self._table)

        if for_insert:
            # the key is not in the hashmap.(the first slot which is None or $ is the right one).
            while self._table[slot]:
                if self._table[slot] is None or self._table[slot] == '$':
                    break
                else:
                    slot = (slot + step) % M
        else:
            # the key is in the hashmap.
            while self._table[slot]:
                if self._table[slot].key == key:
                    break
                slot = (slot + step) % M

        return slot

    def _search(self, key: any):
        """
        searches if the key is in the hashmap or not.
        parameters:
        -----------
                    key: any
                         data key

        returns True if the key is in the hashmap, False otherwise.
        """
        slot = self._hash1(key)
        step = self._hash2(key)
        M = len(self._table)
        while self._table[slot] is not None:
            if self._table[slot].key == key:
                return True
            slot = (slot + step) % M
        return False

    def _rehash(self):
        """
        if the _count reaches _max_count it rehash the whole table with new size and add every entry from previous table
        to the new table.
        returns None
        """
        orig_table = self._table
        new_size = len(self._table) * 2 + 1

        self._table = [None for i in range(new_size)]
        self._count = 0
        self._max_count = len(self._table) - ((len(self._table))//3)

        for entry in orig_table:
            # adding every entry from previous table to the new table.
            if entry:
                slot = self.find_slot(entry.key, True)
                self._table[slot] = entry
                self._count += 1

    def _hash1(self, key: any):
        """
        main hash function which hashes the key for calculating slot.
        parameters:
        ----------
                    key: any
                         data key
        returns slot index.
        """
        return abs(hash(key)) % len(self._table)

    def _hash2(self, key: any):
        """
        second hash function which hashes the key for calculating step.
        parameters:
        ----------
                    key: any
                         data key
        returns step index.
        """
        return 1 + abs(hash(key)) % (len(self._table) - 2)

    def __len__(self):
        """returns the number of entries in the map.(overloads len(hashtable))"""
        return self._count

    def __contains__(self, key: any):
        """returns True if the key is in the hashmap or not.(overloads key in hashtable)"""
        return self._search(key)

    def __getitem__(self, key: any):
        """return key's value if the key is already in the hashmap. (overloads hashtable[key])"""
        assert self._search(key) is True, 'Invalid Key.'
        return self.get(key)

    def __setitem__(self, key: any, value: any):
        """update or add the key,value to the hashtable.(overloads hashtable[key] = value)"""
        return self.add(key, value)

    def __iter__(self):
        """return iterator for hashtable."""
        return _HashMapIterator(self._table)


class _MapEntry:
    """
    class to represent HashMap Entries.

    attributes:
    ----------
              key: any
                   data key
              value: any
                     data value

    """
    def __init__(self, key, value):
        """
        initializes table entry with the given key,value.

        parameters:
        ----------
                    key: any
                         data key
                    value: any
                           data value
        """
        self.key = key
        self.value = value


class _HashMapIterator:
    """
    class to represent hashmap iterator.
    """
    def __init__(self, hashtable):
        self._items = hashtable
        self._cur_inx = 0

    def __next__(self):
        """
        checks each table slot which is not none and return it's key,value.
        returns key,value
        """
        if self._cur_inx < len(self._items):
            while self._items[self._cur_inx] is None or self._items[self._cur_inx] == '$':
                self._cur_inx += 1
                if self._cur_inx == len(self._items):
                    raise StopIteration
            key, value = self._items[self._cur_inx].key, self._items[self._cur_inx].value
            self._cur_inx += 1
            return key, value
        else:
            raise StopIteration

    def __iter__(self):
        return self
