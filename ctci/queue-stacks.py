class Node(object):
    def __init__(self, data, nxt=None):
        self.data = data
        self.next = nxt


class MyQueue(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def peek(self):
        return self.head.data

    def pop(self):
        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def put(self, value):
        new = Node(value)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

    def __str__(self):
        out = '{'
        current = self.head
        while current is not None:
            out += '{},'.format(current.data)
            current = current.next
        out += '}'
        return out


queue = MyQueue()
t = int(input())
for line in range(t):

    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
