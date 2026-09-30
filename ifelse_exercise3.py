a=int(input("number a :"))
b=int(input("number b :"))
c=input("add/sub/multiply :")
if (c=="add"):
    print("Addition value :", a+b)
elif (c=="sub"):
    print("Subtraction value :", a-b)
elif (c=="multiply"):
    print("Multiplication vaue :", a*b)
else:
    print("Division value", a/b)
