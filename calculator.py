kdef calculator():
    number1= float(input("first number"))
    operator= input("enter ur operator")
    number2= float(input("second number"))
    if operator == "-":
        print(number1 - number2)
    elif operator == "+":
        print(number1 + number2 )
    elif operator =="×":
        print(number1 * number2 )
    elif operator =="÷":
        print(number1 / number2 )
    else:
        print("Wrong operator")  

calculator()























