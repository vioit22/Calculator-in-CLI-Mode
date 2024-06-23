from logging import root
import math
root = input("Calculator with maximum 10 numbers, Click Enter to continue")
operator = input("Enter an operator- (+ - * /):")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
num4 = float(input("Enter the 4th number: "))
num5 = float(input("Enter the 5th number: "))
num6 = float(input("Enter the 6th number: "))
num7 = float(input("Enter the 7th number: "))
num8 = float(input("Enter the 8th number: "))
num9 = float(input("Enter the 9th number: "))
num10= float(input("Enter the 10th number:"))
if operator == "+":
    result = num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10
    print(round(result, 10))
elif operator == "-":
    result = num1 - num2 - num3 - num4 - num5 - num6 - num7 - num8 - num9 - num10
    print(round(result, 10))
elif operator == "*":
    result = num1 * num2 * num3 * num4 * num5 * num6 * num7 * num8 * num9 * num10
    print(round(result, 10))
elif operator == "/":
    result = num1 / num2 / num3 / num4 / num5 / num6 / num7 / num8 / num9 / num10
    print(round(result, 10))
else:
    print(f"{operator}  Error caused by missing operator in the code, please try again or contact a developer to fix a problem vioit@hotmail.com! Thank You for advice!")

input("Run Again the Code to calculate other something! Click Enter to exit!")