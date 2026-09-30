class student:
    def __init__(self):
        name=""
        reg_no=0
    def display(self):
        print("Name :",self.name)
        print("Reg_no :",self.reg_no)

dinesh=student()
ganesh=student()

dinesh.name="Dinesh"
ganesh.name="Ganesh"

dinesh.reg_no=1
ganesh.reg_no=2

dinesh.display()
ganesh.display()
