#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"

    else :
        return "Access denied"

admin_login("admin","145")
admin_login("admin","12345")
admin_login("adn","12345")

    

def hows_the_weather(temperature):
    # your code here
    if temperature < 40 :
        return "It's brisk out there!"
    if temperature >= 40 and temperature < 65 :
        return "It's a little chilly out there!"
    if temperature > 85 :
        return "It's too dang hot out there!"
    else :
        return "It's perfect out there!"

hows_the_weather(70)

  

def fizzbuzz(num):
    # your code here
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"


    elif num % 5 == 0 :
        return "Buzz"

    elif num % 3 == 0 :
        return "Fizz"

    #  elif num % 5 == 0 and num % 3 == 0:
    #     return ("FizzBuzz")
        
    else :
        return num

fizzbuzz(33)
fizzbuzz(50)
fizzbuzz(15)
fizzbuzz(34)
 

def calculator(operation, num1, num2):
    # your code here
    
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 / num2
    else:
        print("Invalid operation!")
        return None
      

    return result

calculator("+", 1, 1)

