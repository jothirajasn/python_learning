amount = 1200
tax = amount * 0.18
total = amount + tax 

print("Amount :",amount)
print("Amount with tax :",total)

if amount > 1000 :
    discount =  total * 0.10
    total -= discount

print("total amount after discount if total is above 1000", total)