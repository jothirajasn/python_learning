class phone:
    def __init__(self,brand,price,chargertype):
        self.brand=brand
        self.price=price
        self.chargertype=chargertype

    def display(self):
        print("Brand name : ",self.brand)
        print("Price : ",self.price)
        print("charger type :",self.chargertype)


samsung=phone("samsung", "20000", "c-type")
samsung.display()


redmi=phone("Redmi", "24000", "c-type")
redmi.display()
