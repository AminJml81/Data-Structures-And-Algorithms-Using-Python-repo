from Linked_List import LinkedList
from Sorted_Liked_List import SortedLinkedList

sll = SortedLinkedList()
for i in range(10):
    sll.insert(10-i)

#sll.print_elements()
sll.insert(5)
sll.insert(54)
sll.insert(-100)
# print(len(sll))
# sll.remove(-100)
# sll.remove(54)
# sll.remove(5)
# print(len(sll))

# for elm in sll:
#     print(elm)

print(help(SortedLinkedList))