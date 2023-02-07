from dynamic_array import DynamicArray
import argparse

class Stack(DynamicArray):
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
         return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self._data [-1]

    def pop(self):
        if self.is_empty():
            raise Exception("stack is empty")
        return self._data.pop()

class queue(DynamicArray):
    default_capacity = 10

    def __init__ (self):
        self._data = [None] * queue.default_capacity
        self._size = 0
        self._front = 0
    def __len__ (self):
        return self._size

    def is_empty(self):
        return self._size == 0
    def _resize(self , cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
            self._front = 0

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1


    def dequeue(self):
        if self.is_empty( ):
            raise Exception( "Queue is empty" )
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def front(self):
        if self.is_empty( ):
            raise Exception( "Queue is empty ")
        return self._data[self._front]

if __name__ == '__main__':
    x = Stack()
    print(x.__len__())
    x.push(4)
    print(x.top())
    print(x.pop())

    y = queue()
    print(t.__len__())
    print(t.is_empty())
    y.enqueue(1)
    print(y.dequeue())
    print(y.front())
