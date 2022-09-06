from queue import Queue
# Queue.get() -> 앞에서 값을 가져옴
# Queue.put() -> list에서의 append
# Queue.empty() -> 비어있으면 True 아니면 False를 반환

class MyStack(object):

    def __init__(self):
        self.q = Queue()
        self.temp_q = Queue()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.temp_q.put(x)
        while self.q.empty() == False:
            self.temp_q.put(self.q.get())
        dummy = self.q
        self.q = self.temp_q
        self.temp_q = dummy

    def pop(self):
        """
        :rtype: int
        """
        # q가 비어있다면 None 반환
        if self.q.empty():
            return
        return self.q.get()

    def top(self):
        """
        :rtype: int
        """
        if self.q.empty():
            return
        return self.q.queue[0]          # 큐는 인덱스 접근을 하려면 .queue[0] 이런식으루.. q[0] 안된대요

    def empty(self):
        """
        :rtype: bool
        """
        if self.q.empty() == True:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()