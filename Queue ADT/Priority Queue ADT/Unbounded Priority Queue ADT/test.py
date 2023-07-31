# from pylistupqueue import PriorityQueue
from llupqueue import PriorityQueue
pq = PriorityQueue()

print(pq.is_empty())
print(len(pq))
# print(pq.dequeue())
pq.enqueue('red', 0)
pq.enqueue("purple", 5)
pq.enqueue("black", 1)
pq.enqueue("orange", 3)
pq.enqueue("white", 0)
pq.enqueue("green", 1)
pq.enqueue("yellow", 5)

print(pq.is_empty())
print(len(pq))


print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())
print(pq.dequeue())