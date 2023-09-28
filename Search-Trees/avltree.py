LEFT_HIGH = 1
EQUAL_HIGH = 0
RIGHT_HIGH = -1


class AVLMap:
    def __init__(self):
        self._root = None
        self._size = 0

    def search(self, item):
        """
        searches for given key in the AVL Tree. it starts from tree's root if the given key is larger than root's key
        it continues searching the right subtree, if it is smaller it continues searching the left subtree.
        it continues this process until it reaches None node or it finds the node.
        """
        assert item is not None, 'Key Parameter is not provided.'
        node = self._root
        while node:
            if node.key == item:
                return True

            elif node.key > item:
                node = node.left

            else:
                node = node.right

        return False

    def add(self, key, value):
        """
        it inserts new node to the AVL tree if the key is not in the tree, Otherwise it updates its value.
        if key is smaller than current node it goes to the left subtree, if it is larger it goes to the right subtree
        until it finds the proper location of the new node.
        parameters:
        -----------
                    key: any
                        node's key
                    value: any
                        node's key
        """
        # if node's key is already in the tree, it updates its value.
        node = self._find_node(key)
        if node:
            node.value = value
        else:
            self._root = self._insert(self._root, key, value)
            self._size += 1

    def get(self, key):
        """returns value of the given key if it is in the BST."""
        node = self._find_node(key)
        assert node is not None, 'Invalid Key'
        return node.value

    def remove(self, key):
        assert key in self, 'Invalid Key'
        self._root = self._avlremove(self._root, key)

    def _find_node(self, key):
        """returns the node with the given key."""
        assert key is not None, 'Key Parameter is not provided.'
        node = self._root
        while node:
            if node.key == key:
                return node

            elif node.key > key:
                node = node.left

            else:
                node = node.right

        return None

    def _insert(self, node, key, value):
        """
        helper method for adding new node to the AVL Tree.
        parameters:
        -----------
                    node: _BSTMapNode
                             node
                    key: any
                         node's key
                    value: any
                          node's value

        returns added Node and links it to tree.
        """
        if node is None:
            node = _BSTMapNode(key, value)
        elif key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)

        return node

    def __len__(self):
        """return number of items in the avl tree."""
        return self._size

    def __contains__(self, item):
        """returns True if the key is in the avl, False Otherwise."""
        return self.search(item) is not False

    def __iter__(self):
        return _AVLMapIterator(self._root, self._size)


class _AVLMapIterator:
    """
    class to represent Iterator for AVL Tree.
    it stores nodes in a python list.
    """

    def __init__(self, root, size):
        # stores trees key in a list.
        self._theKeys = [None] * size
        self._curItem = 0
        self._avl_traversal(root)
        self._curItem = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curItem < len(self._theKeys):
            node = self._theKeys[self._curItem]
            self._curItem += 1
            return node
        else:
            raise StopIteration

    def _avl_traversal(self, node):
        """
        Inorder Traversal to build list of nodes.
        parameters:
                    node: _BSTMapNode
        """
        if node:
            self._avl_traversal(node.left)
            self._theKeys[self._curItem] = node
            self._curItem += 1
            self._avl_traversal(node.right)


class _BSTMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.bf = EQUAL_HIGH
        self.left = None
        self.right = None
