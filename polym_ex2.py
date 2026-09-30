class shape:

    def area(self):
        return 0

class rectangle(shape):

    def area(self, a, b):
        print(a*b)


input1=rectangle()
input1.area(10, 20)
