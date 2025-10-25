def fib(n) :
    a=0
    b=1
    if (n==0) :
        print(a)
    if (n==1) :
        print(b)
    else :
        c=a+b
        print(c)
        a=b
        b=c
num=int(input("Enter a number: "))
fib(num)
