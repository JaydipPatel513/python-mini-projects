def add(num1,num2):
    result=num1+num2
    print(num1 ,"+", num2, "=",result)

def sub(num1,num2):
    result=num1-num2
    print(num1 ,"-", num2, "=",result)

def mul(num1,num2):
    result=num1*num2
    print(num1 ,"*", num2, "=",result)

def div(num1,num2):
    result=num1/num2
    print(num1 ,"/", num2, "=",result)

choice = input("Enter Operator: +,-,*,/")
firstnum=int(input("Enter your first number"))
secondnum=int(input("Enter your second number"))

if choice=="+":
    add(firstnum,secondnum)
if choice=="-":
    sub(firstnum,secondnum)
if choice=="*":
    mul(firstnum,secondnum)
if choice=="/":
    div(firstnum,secondnum)