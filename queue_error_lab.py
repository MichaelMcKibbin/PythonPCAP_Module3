class QueueError(IndexError):  # Choose base class for the new exception.
    # raise exception when get() tries to operate on empty list
    pass

class Queue:
    def __init__(self):
        self.queue = [] # initialize an empty list to represent the queue

    def put(self, elem):
        self.queue.insert(0, elem) # insert at the front of the list

    def get(self):
        if not self.queue:
            raise QueueError("Queue is empty")
        elem = self.queue[-1]
        del self.queue[-1]
        return elem

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError:
    print("Queue error: empty queue")
