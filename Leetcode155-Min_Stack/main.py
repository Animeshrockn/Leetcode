# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# ========================================================

#  1. Naive Approach with getMin in O(n):

class MinStack1:

    def __init__(self):
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return min(self.arr)




# ========================================================

#  1. O(1) Approach :

class MinStack2:

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, val: int) -> None:
        
        self.arr.append(val)
        if self.minarr:
            val = min(val,self.minarr[-1])
        self.minarr.append(val)


    def pop(self) -> None:
        self.arr.pop()
        self.minarr.pop()


    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]


# ============================================================


obj = MinStack1()
obj.push(10)
obj.push(60)
obj.push(90)
obj.push(20)
obj.push(30)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)
