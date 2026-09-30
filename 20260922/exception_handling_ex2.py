try:
    a=int(input())
    b=int(input())
    c=input()
    print(a/c)
except ValueError as e:
    print("Value Error",e)
except TypeError as e:
    print("Type Error",e)
finally:
    print("Done")

#if i will Hi instead of 10, it will throw ValueError
#10/Hi - if we are trying divide number with string, it will throw TypeError

#finally - it works all times you have error or no error
