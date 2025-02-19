def cal():
    num1=float(input("enter the first number:"))
    num2=float(input("enter the second number:"))
    operators=(input("enter operator(+,-,*,/,%)"))
    if operators== "+":
        print(num1+num2)
    elif operators== "-":
        print(num1-num2)
    elif operators== "*":
        print(num1*num2)
    elif operators== "/":
        if num2!=0:
            print(num1/num2)
        else:
            print("error")
    elif operators== "%":
        if num2!=0:
            print(num1%num2)
        else:
            print("error")
cal()