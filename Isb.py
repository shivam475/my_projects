try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    d=a/b
except:
    print("Enter correct value of a and b")
    try:
        a=int(input("Enter first number"))
        b=int(input("Enter second number"))
        d=a/b
    except:
        print("Enter correct value of a and b")
    print(d)
print(d)