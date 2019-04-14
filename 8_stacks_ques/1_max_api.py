# Create a stack API that supports a max operation
# max() should return the maximum value in the stack
# Tricky part here is updating the max when we potentially pop() max val

from collections import namedtuple

# namedtuple is a class factory function to create named tuples
# Can access parameters by name
# capitalized because it is a user-defined class
class Stack:
    CachedElement = namedtuple('CachedElement', ['element', 'max'])

    def __init__(self):
        # Stack consists of CachedElement instead of just the element
        self.stack = []

    def empty(self):
        return not self.stack

    def push(self, x):
        max_val = x if self.empty() else max(x, self.max())
        self.stack.append(self.CachedElement(x, max_val))

    def pop(self):
        if self.empty():
            raise IndexError('Stack is empty')
        return self.stack.pop().element

    # Simply returns max in the stack, doesn't remove anything
    def max(self):
        if self.empty():
            raise IndexError('Stack is empty')
        return self.stack[-1].max

if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(7)
    stack.push(13)

    print(stack.max())
    print(stack.pop())
    print(stack.max())
    print(stack.pop())
