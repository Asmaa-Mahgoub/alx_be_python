"""
Enter the first number: 10
Enter the second number: 5
Choose the operation (+, -, *, /): *
The result is 50.
Or, for a division by zero scenario:

Enter the first number: 10
Enter the second number: 0
Choose the operation (+, -, *, /): /
Cannot divide by zero.
"""
num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
match operation:
    case "+"  :
        num1 + num2
        print(f"The result is {num1 + num2}")
    case "-" :
        num1 - num2
        print(f"The result is {num1 - num2}")
    case "*" :
        num1 * num2
        print(f"The result is {num1 * num2}")
    case "/" :
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            num1 / num2
            print(f"The result is {num1 / num2}") 
    
          