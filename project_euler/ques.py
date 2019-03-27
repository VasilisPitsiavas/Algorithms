
class stack:
    def __init__(self):
        self.stack = []
        self.top = 0

    def push(self, data):
       self.stack.insert(self.top, data)
       self.top += 1

    def pop(self):
         self.top -= 1
         lastpoped = self.stack[self.top]
         del self.stack[self.top]
         return lastpoped
    def printstack(self):
        for x in self.stack:
            print x

stack = stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.pop()


stack.printstack()



