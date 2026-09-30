class calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print("Addition :", self.a+self.b)
    def sub(self):
        print("Subraction :",self.a-self.b)
    def mul(self):
        print("Multiplication :",self.a*self.b)
    def div(self):
        print("Division :",self.a/self.b)

a=calculator(2,4)

a.add()
a.sub()
a.mul()
a.div()

