num1 = float(input("Enter First Number:"))
op = input("Enter Operator (+, -, *, /):")
num2 = float(input("Enter Second Number:"))

if op == "+":
    print("result:", num1 + num2)
elif op == "-":
    print("result:", num1 - num2)
elif op == "*":
    print("result:", num1 * num2)
elif op == "/":
    if num2 == 0:
        print("Error Cannot divide by zero")
    else:
        print("result:", num1 / num2)
else:
    print("Invalid Operator")