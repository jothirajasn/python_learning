class calculator :
    def __init__(self, val1, val2):
        self.val1= val1
        self.val2= val2
    def add(self):
        v_add = self.val1 + self.val2
        print(v_add)

addition = calculator(1, 2)

addition.add()
        
        
