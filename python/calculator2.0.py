print("enter a value")
x = int(input())
print("enter another value")
y = int(input())
print("enter the operation: ex: +,-,*,/")
o = input()
if (o == '+'):
    print("your answer is:", x+y)
elif(o == '-'):
    print("your answer is:", x-y)
elif(o == '*'):
    print("your answer is:", x*y)
elif(o == '/'):
    if (y == 0):
        print("We cannot divide by zero")
        exit (1)
    print("your answer is:", x/y)
else: 
    print("It seems that you have not used the following symbols:+,-,*,/, please try again with these symbols.")
