from maxheap import MaxHeap
from minheap import MinHeap

a = MinHeap()
# a = MaxHeap

a.insert(100)
a.insert(84)
a.insert(71)
a.insert(60)
a.insert(23)
a.insert(12)
a.insert(29)
a.insert(1)
a.insert(37)
a.insert(4)
a.insert(90)
a.insert(41)

print(a.extract())
print(a.extract())
print(a.extract())
print(a.extract())

# a.insert(20)
# a.traverse()
# print(a.search(41))
# print(a.search(29))
# print(len(a))
