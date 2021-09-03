# ITP Week 1 Day 4 Exercise

#Write a basic calculator using the input function to complete the following tasks.  Be sure to call your functions at the end, using the correct arguments.

# Easy:
#     - A function that subtracts one integer from another
def sub(num1, num2):
    return num1 - num2

#     - A function that multiplies three integers
def mult(num1, num2, num3):
    return num1 * num2 * num3

#     - A function that adds four integers
def add(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4

# Medium: 
#     - Create a calculator function using THREE input parameters (two float, one string[hint: it will be a math symbol]) to allow the user to add, substract, multiply and divide.
def calculator():
    first_number = float(input("first number:"))
    operation = input("please choose: +, -, *, /: ")
    second_number = float(input("second number: "))

    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        if second_number != 0:
            return first_number / second_number
        else:
            print("can't devide by 0")
    else:
        print("invalid operation")

#print(calculator())


# Hard: 
#     - You're at a restaurant with some friends and the server didn't split up the check.  
# Create a function that takes a bill amount, multiplies it by a global variable called tax_rate, adds the tax, and then divides the total bill by the number of people input by the user.  
# BONUS:  Include an option for adding tip through either a percentage amount assigned to a global varible, or through a specific amount input by the user.  
# You may use the math module from the Python standard library.

#Remember to first write in comments an outline of what you want to code (using regular words, no computer-speak) BEFORE you begin to code.  
#Break each part down to the smallest problem you can, and then address them individually.  CONSULT THE RESOURCES if you get stuck, and don't be afraid to Google.

import math
sales_tax_rate = 0.1075

def bill_divider():
    # get bill amount
    bill_amount = float(input("Please enter bill amount: "))
    # get diner number
    num_of_diners = int(input("Please enter number of diners: "))
    # get tip percentage
    percent_of_tips = int((input("Please enter percentage for tips: ")))
    #amount with sales tax and user specified tip rate
    total_amount = (bill_amount * (1 + sales_tax_rate)) * (1 + (percent_of_tips) /100)
    #diner amount to whole dollar
    each_diner_amount = math.ceil(total_amount / num_of_diners)

    print("Each diner need to pay $" + str(each_diner_amount))

bill_divider()
    


    

    



