class MyQueue(object):

    def __init__(self):
        self.stack = []
        self.temp = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        n = len(self.stack) -1
        for _ in range(n):
            self.temp.append(self.stack.pop())
        top = self.stack.pop()
        for _ in range(n):
            self.stack.append(self.temp.pop())
        return top

    def peek(self):
        """
        :rtype: int
        """
        n = len(self.stack) -1
        for _ in range(n):
            self.temp.append(self.stack.pop())
        front = self.stack[0]
        for _ in range(n):
            self.stack.append(self.temp.pop())
        return front

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.stack) == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()