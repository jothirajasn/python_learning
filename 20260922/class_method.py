class laptop:
    chargertype="C-type"

    def __init__(self):
        self.brand=""
        self.price=56
    def setprice(self,price):
        self.price=price
    def getprice(self):
        print(self.price)

    @classmethod
    def changechargertype(cls):
        cls.chargertype="B-type"
        print("Charger type changed")

    @staticmethod
    def info():
        print("This is laptop class")
        

hp=laptop()
hp.setprice(1400)
hp.getprice()

hp.changechargertype()
hp.info()
