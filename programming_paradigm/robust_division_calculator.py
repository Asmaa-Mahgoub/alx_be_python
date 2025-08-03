

def safe_divide(numerator, denominator):
    try:
        numerator= float(numerator)
        denominator= float(denominator)
        result = numerator/denominator
       
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except ValueError as e:
        print("Error: Please enter numeric values only.")

    else:
        print(f"The result of the division is {result}")

    finally:
        pass




    








