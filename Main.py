import os
class Stack:
    def __init__(self, A):
        self.items = [None]*A
        self.A = A
        self.top = -1

    def is_empty(self):
        if (self.top ==A -1):
            return True
        else:
            return False

    def is_full(self):
        if (self.top == self.A-1):
            return True
        else:
            return False

    def push(self, data):
        if not self.is_full():
            self.top += 1
            self.items[self.top] = data
    
    def pop(self):
        if not self.is_empty():
            data = self.items[self.top]
            self.top -= 1
            return data

    def status(self):
        for i in range(self.top+1):
            print(self.items[i])

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(A)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
