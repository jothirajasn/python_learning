class teacher:
    def __init__(self,name,reg_no):
        self.name=name
        self.reg_no=reg_no
    def display(self):
        print("Name : ",self.name)
        print("Reg_no : ",self.reg_no )

t1=teacher("Guna", 1)
t2=teacher("Veera", 2)
t1.display()
t2.display()
