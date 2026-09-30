class animal():

    def sound(self):
        print("Animal makes a sound")

class dog(animal):

    def sound(self):
        print("Dog Barks")


class bird(animal):

    def sound(self):
        print("Bird sings")

obj1= dog()
obj1.sound()
        

