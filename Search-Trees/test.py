from BST import BSTMap

tree = BSTMap()
tree.add(60, '60')
tree.add(12, '12')
tree.add(90, '90')
tree.add(4, '4')
tree.add(41, '41')
tree.add(71, '71')
tree.add(100, '100')
tree.add(1, '1')
tree.add(29, '29')
tree.add(84, '84')
tree.add(23, '23')
tree.add(37, '37')
# tree.inorder()

tree.remove(1)
print()
# tree.inorder()

for node in tree:
    print(node.key, node.value)
