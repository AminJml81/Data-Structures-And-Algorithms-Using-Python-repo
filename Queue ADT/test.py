# from pylistqueue import Queue
from arrayqueue import Queue
# from llistqueue import Queue

# queue  = Queue()
queue = Queue(maxsize=5,queue_items_type=str)
# queue = Queue()

print(queue.is_empty())
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
#print(len(queue))
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
print(queue.is_empty())
print(queue.dequeue())
#print(len(queue))
print(queue.dequeue())
#print(len(queue))
#print(queue.dequeue())
