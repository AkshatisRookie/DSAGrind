class MinStack:

    def __init__(self):
        self.stk=[]
        self.minstk=[]
        self.min1=0
        self.a=0
    def push(self, val: int) -> None:
        if len(self.minstk)==0 or val<=self.minstk[-1] :
            self.minstk.append(val)
        self.stk.append(val)
    def pop(self) -> None:
        self.a=self.stk[-1]
        self.stk.pop()
        if self.a==self.minstk[-1]:
            self.minstk.pop()
    def top(self) -> int:
        return self.stk[-1]
    def getMin(self) -> int:
        return self.minstk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()