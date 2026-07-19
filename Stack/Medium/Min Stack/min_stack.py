class MinStack:

    def __init__(self):
        self.min_stack = [] # Indexes for which are "min_values" (biggest to smallest) in self.stack
        self.stack = []
        
    def push(self, value: int) -> None:
        if len(self.min_stack) == 0: # Empty stack, always smallest
            self.min_stack.append(len(self.stack))
        elif value <= self.stack[self.min_stack[-1]]:
            self.min_stack.append(len(self.stack))
        self.stack.append(value)
        

    def pop(self) -> None:
        if (len(self.stack) - 1 == self.min_stack[-1]):
            # Current min value being removed, move to next
            self.min_stack.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.min_stack[-1]]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()