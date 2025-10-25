try :
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    print(x/y)
except ZeroDivisionError :
    print("Can't divide with zero.")
except ValueError :
    print("Please provide int value only.")
