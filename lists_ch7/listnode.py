class ListNode:
    def __init__(self, data = 0, next_node = None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return '{}(data={}, next_node={})'.format(self.__class__.__name__, self.data,
                self.next.data)
