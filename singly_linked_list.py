class node:
    def __init__(self, data):
        self.data = data
        self.next = None
class singly_linked:
    def __init__(self, data):
        self.data = data
        self.head = node(data)
        self.tail = self.head
    def append(self, data):
        self.data = data
        self.new_node = node(data)
        self.tail.next = self.new_node
        self.tail = self.new_node
    def accumulate(self):
        self.accumulator = self.head
        x = []
        while self.accumulator is not None:
            x.append(self.accumulator.data)
            self.accumulator = self.accumulator.next
        return x
    def replace(self, old_val, new_val):
        to_replace = []
        self.iterator = self.head
        while self.iterator is not None:
            if self.iterator.data == old_val:
                to_replace.append(self.iterator)
            self.iterator = self.iterator.next
        for item in to_replace:
            item.data = new_val



n = singly_linked(2)
n.append(3)
n.append(4)
n.append(4)
x = n.accumulate()
print(x)
old = int(input('enter value to be replace: '))
new = int(input('enter new value: '))
n.replace(old, new)
x = n.accumulate()
print(x)


