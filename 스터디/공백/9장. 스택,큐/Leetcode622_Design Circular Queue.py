from collections import deque
class MyCircularQueue:

    def __init__(self, k):
        self.dq = deque()
        self.size = k

        
    def enQueue(self, value):
        if len(self.dq) < self.size:
            self.dq.append(value)
            return True
        return False

    
    def deQueue(self):
        if len(self.dq) > 0:
            self.dq.popleft()
            return True
        return False

    
    def Front(self):
        if len(self.dq) > 0:
            return self.dq[0]
        return -1

    
    def Rear(self):
        if len(self.dq) > 0:
            return self.dq[-1]
        return -1

    
    def isEmpty(self):
        return len(self.dq) == 0

    
    def isFull(self):
        return len(self.dq) == self.size