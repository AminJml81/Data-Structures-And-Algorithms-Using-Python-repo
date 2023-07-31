from bpriorityqueue import BPriorityQueue

queue = BPriorityQueue(10)

for i in range(5):
    queue.enqueue(i, i)

for j in range(5):
    queue.enqueue(j, 2*j)

for k in range(4):
    queue.enqueue(k, 3*k)

for l in range(5):
    queue.enqueue('*', 5)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
# print(queue.dequeue())