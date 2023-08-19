from Double_Linked_List import DoubleLinkedList
from Circular_Linked_List import CircularLinkedList
import random

ll = CircularLinkedList()
# ll = DoubleLinkedList()
if ll.__class__.__name__ == 'DoubleLinkedList':
    random.seed(5)
    for i in range(30):
        number = ll.insert(random.randint(1, 20))
    ll.front_traversal()
    print(ll.search(20))
    print(ll.search(10))
    print(ll.search(15))
    print(ll.search(18))
    ll.remove_item(12)
    ll.remove_item(1)
    ll.remove_item(20)
    ll.remove_item(1)
    ll.remove_item(6)
    ll.remove_item(5)
    ll.remove_item(17)
    ll.front_traversal()
    ll.tail_traversal()
    ll.insert(5)
    ll.front_traversal()
    print()
    ll.remove_item(5)
    print()
    ll.front_traversal()


if ll.__class__.__name__ == 'CircularLinkedList':
    random.seed(5)
    for i in range(30):
        number = ll.insert(random.randint(1, 20))
    ll.traverse()
    print(ll.search(20))
    print(ll.search(10))
    print(ll.search(15))
    print(ll.search(18))
    ll.remove_item(7)
    ll.remove_item(1)
    ll.remove_item(20)
    ll.remove_item(1)
    ll.remove_item(6)
    ll.remove_item(5)
    ll.remove_item(17)
