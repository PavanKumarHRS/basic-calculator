# Author:
# Agyeya Mishra
# Department of Civil Engineering
# Delhi Technological University (formerly, Delhi College of Engineering)
# New Delhi, India


#Python program to create a simple calculator 
  
#Function to perform addition of two numbers
def add(number1, number2): 
    return (number1 + number2) 
  
#Function to perform subtraction of two numbers
def subtract(number1, number2): 
    return (number1 - number2)
  
#Function to perform multiplication of two numbers 
def multiply(number1, number2): 
    return (number1 * number2) 
  
#Function to perform division of two numbers 
def divide(number1, number2): 
    return (number1 / number2)
  
print("Operation Menu -\n" \ 
        "1. Addition of two numbers\n" \ 
        "2. Subtraction of two numbers\n" \ 
        "3. Multiplication of two numbers\n" \ 
        "4. Division of two numbers\n") 
  
  
#Taking input from the user  
select = input("Select operations form 1, 2, 3, 4 :") 
  
num1 = int(input("Enter first number: ")) 
num2 = int(input("Enter second number: ")) 
  
if select == '1': 
    print(num1, "+", numb2, "=", 
                    add(num1, num2)) 
  
elif select == '2': 
    print(num1, "-", num2, "=", 
                    subtract(num1, num2)) 
  
elif select == '3': 
    print(num1, "*", num2, "=", 
                    multiply(num1, num2)) 
  
elif select == '4': 
    print(num1, "/", num2, "=", 
                    divide(num1, num2)) 
else: 
    print("Invalid input!")
