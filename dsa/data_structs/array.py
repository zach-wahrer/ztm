class Array():
    def __init__(self):
        self.length = 0
        self.data = []

    def __iter__(self):
        for i in range(self.length - 1):
            yield self.get(i)

    def get(self, index):
        return self.data[index]

    def append(self, item):
        self.data = self.data + [item]
        self.length += 1

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)

    def shift_items(self, index):
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i + 1]
        del self.data[self.length - 1]
        self.length -= 1


my_array = Array()
for i in range(10):
    my_array.append(i)

print("Popped: " + str(my_array.pop()))

for i in range(my_array.length):
    print(my_array.get(i))

my_array.delete(2)

for i in my_array:
    print(i)

print("Length: " + str(my_array.length))
