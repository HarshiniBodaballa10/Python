def calculator():
    num1=float(input("Enter the num1 value:"))
    num2=float(input("Enter the num2 value:"))
    operator=input("Enter the operator('+','-','*','/','%'):")
    if operator=='+':
        print(f"Result:{num1+num2}")
    elif operator=='-':
        print(f"Result:{num1-num2}")
    elif operator=='*':
        print(f"Result:{num1*num2}")
    elif operator=='/':
        print(f"Result:{num1/num2}")
    elif operator=='%':
        print(f"Result:{num1%num2}")
    else:
        print("Invalid Operator...")
calculator()
