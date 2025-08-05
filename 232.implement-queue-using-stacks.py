# @leet start
class MyQueue:
    # a stack is last-in last-out
    # a queue is first-in first-out
    # therefore we can have a stack for input filled when appending and
    # a stack that reverses the input stack whenever an output is necessary
    def __init__(self):
        self.input = []
        self.output = []

    # pushes element x to back of queue (enqueue)
    def push(self, x: int) -> None:
        self.input.append(x)

    # removes and returns element at front of queue
    def pop(self) -> int:
        # reuse peek as it populates output stack when necessary
        self.peek()
        return self.output.pop()
        
    # returns element at front of queue
    def peek(self) -> int:
        # only moves inputs to output when we need more output 
        # to be efficient due to nature of queue
        if len(self.output) == 0:
            while len(self.input) != 0:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self) -> bool:
        return len(self.input) == len(self.output) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @leet end
