class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.data = []
        self.counter = 0

    def append(self, item):
        if self.length < self.capacity:
            self.data.append(item)
            self.length += 1
            self.counter += 1
            if self.counter == self.capacity: 
                self.counter = 0
        else:
            self.data[self.counter] = item
            self.counter += 1
            if self.counter == self.capacity: 
                self.counter = 0


    def get(self):
        return self.data


b = RingBuffer(5)
b.append('a')
b.append('b')
b.append('c')
print(b.get())
b.append('d')
print(b.get())
b.append('e')
print(b.get())
b.append('f')
print(b.get())
b.append('g')
print(b.get())
