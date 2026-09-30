a = []

for i in range(1, 8):
    num =int(input("number "+str(i)))
    a.append(num)

print(a)

sum=0
for i in a:
    sum = sum + i
print(sum)
