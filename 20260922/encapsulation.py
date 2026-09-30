class company:
    def __init__(self):
        self._companyname="Google"

class b(company):
    pass

b1=b()
print(b1._companyname)

#_companyname - single underscore means protected varaible
#public protect and private access modifier
