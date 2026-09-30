class fruit:
    def __init__(self):
        color=""
        
    def display(self):
        print("color of the fruit : ",self.color)

apple=fruit()

apple.color="Red"

banana=fruit()

banana.color="Yellow"

apple.display()
banana.display()
