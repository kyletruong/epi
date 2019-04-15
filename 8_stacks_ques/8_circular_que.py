# Implement a circular queue API using arrays (lists)
# Need enque(), deque(), size()
# Circular que means could wrap around like this [3, 4, 1, 2]

class Queue:
    # Keep track of head, tail, and num elements
    def __init__(self, size):
        self._q = [None] * size
        self._head = self._tail = self._num_elements = 0

    def enque(self, x):
        # Que is full, double the capacity
        if self._num_elements == len(self._q):
            # Reorder so it's consecutive wihtout wrapping around
            self._q = self._q[self._head:] + self._q[:self._head]
            self._head, self._tail = 0, self._num_elements
            self._q += [None] * len(self._q)

        self._q[self._tail] = x
        self._tail = (self._tail + 1) % len(self._q) # Wrap back around arr
        self._num_elements += 1

    def deque(self):
        if not self._num_elements:
            raise IndexError('Queue is empty')
        ret = self._q[self._head]
        self._head = (self._head + 1) % len(self._q) # Wrap back around arr
        self._num_elements -= 1
        return ret

    def size(self):
        return self._num_elements

    def __str__(self):
        return ''.join(str(self._q))

if __name__ == '__main__':
    q = Queue(4)
    q.enque(1)
    q.enque(2)
    print(q)
    q.enque(3)
    q.enque(4)
    print(q)
    q.deque()
    q.enque(5)
    print(q)
    q.deque()
    q.enque(6)
    print(q)
    q.enque(7)
    print(q)
