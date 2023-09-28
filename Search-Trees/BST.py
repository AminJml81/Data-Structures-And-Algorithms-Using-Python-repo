class BSTMap:
    """
    BST(Binary Search Tree) is a binary tree in which for each node V,
                            all keys less than the key are stored in the left subtree of V
                            and all keys greater than the key are stored in the right subtree of V.

    # Note: in this implementation each node contains key, value so it is called BST MAP.

    attributes:
    -----------


    methods:
    --------


    """

    def __init__(self):
        self._root = None
        self._size = 0

    def add(self, key, value):
        """
        it inserts new node to the BST if the key is not in the tree, Otherwise it updates its value.
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

    def _insert(self, node, key, value):
        """
        helper method for adding new node to the BST.
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

    def search(self, key):
        """
        searches for given key in the BST. it starts from tree's root if the given key is larger than root's key
        it continues searching the right subtree, if it is smaller it continues searching the left subtree.
        it continues this process until it reaches None node or it finds the node.
        """
        assert key is not None, 'Key Parameter is not provided.'
        node = self._root
        while node:
            if node.key == key:
                return True

            elif node.key > key:
                node = node.left

            else:
                node = node.right

        return False

    def remove(self, key):
        """
        removes key from bst.
        parameters:
        -----------
                    key: any

        links the modifications to the root of bst.
        """
        assert key in self, "Invalid Key."
        self._root = self._remove(self._root, key)
        self._size -= 1

    def _remove(self, node, key):
        """helper method for removing key from bst which first finds the node with the given node and then
        checks it's children.
        if node is a leaf, it simply modify the corresponding node to None.
        if node has only one child, it swaps the node with it's child.
        if node has 2 children, it swaps the node with it's successor which is the minimum item larger than the node.

        parameters:
        -----------
                        node: _BSTMapNode
                        key: any

        """
        if node is None:
            return node
        elif key < node.key:
            node.left = self._remove(node.left, key)
            return node
        elif key > node.key:
            node.right = self._remove(node.right, key)
            return node

        else:
            if node.left is None and node.right is None:
                # if node is leaf.
                return None
            if node.left is None:
                # if node has one child(in it's right subtree)
                return node.right
            if node.right is None:
                # if node has one child(in it's left subtree)
                return node.left

            else:
                # if node has 2 children.
                successor = self._bst_minimum_node(node.right)
                node.key, node.value = successor.key, successor.value
                node.right = self._remove(node.right, node.key)
                return node

    def _bst_minimum_node(self, node):
        """returns minimum node in the tree."""
        while node.left:
            node = node.left
        return node

    def get(self, key):
        """returns value of the given key if it is in the BST."""
        node = self._find_node(key)
        assert node is not None, 'Invalid Key'
        return node.value

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

    def min(self):
        """returns minimum key in the BST."""
        node = self._root
        if node is None:
            return None
        while node.left:
            node = node.left
        return node.key

    def max(self):
        """returns maximum key in the BST."""
        node = self._root
        if node is None:
            return None
        while node.right:
            node = node.right
        return node.key

    def inorder(self):
        """inorder traversal which in the BST is keys sorted in a ascending order."""
        self._inorder(self._root)

    def _inorder(self, node):
        """
        helper method for inorder traversal.
        parameter:
        ----------
                    node: _BSTMapNode
                          initially tree's root.
        """
        if node:
            self._inorder(node.left)
            print(node.key, node.value)
            self._inorder(node.right)

    def __getitem__(self, key):
        """returns value of the given key(bst[key])"""
        node = self._find_node(key)
        assert node is not None, 'Invalid Key'
        return node.value

    def __contains__(self, key):
        """returns True if the key is in the bst, False Otherwise."""
        return self.search(key) is not False

    def __len__(self):
        """return number of items in the bst."""
        return self._size

    def __iter__(self):
        return _BSTMapIterator(self._root, self._size)


class _BSTMapIterator:
    """
    class to represent Iterator for BST.
    it stores nodes in a python list.
    """
    def __init__(self, root, size):
        # stores trees key in a list.
        self._theKeys = [None] * size
        self._curItem = 0
        self._bst_traversal(root)
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

    def _bst_traversal(self, node):
        """
        Inorder Traversal to build list of nodes.
        parameters:
                    node: _BSTMapNode
        """
        if node:
            self._bst_traversal(node.left)
            self._theKeys[self._curItem] = node
            self._curItem += 1
            self._bst_traversal(node.right)


class _BSTMapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.balance_factor = None
        self.left = None
        self.right = None
