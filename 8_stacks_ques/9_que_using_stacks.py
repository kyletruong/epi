# Implement a queue using only stack operations
# Need enque() and deque()

class Queue:
    def __init__(self):
        self._eq, self._dq = [], []

    def enque(self, x):
        self._eq.append(x)

    def deque(self):
        if not self._dq:
            if not self._eq:
                raise IndexError('Queue is empty')
            while self._eq:
                self._dq.append(self._eq.pop())

        return self._dq.pop()

if __name__ == '__main__':
    q = Queue()
    q.enque(1)
    q.enque(2)
    q.enque(3)
    print(q.deque())
    print(q.deque())
    print(q.deque())
    try:
        q.deque()
    except IndexError:
        print('here')
