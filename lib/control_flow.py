#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    # Grant access only of username is "admin or ADMIN" and password is 12345
    # username='admin'
    # if(username==username or username==username.upper()) and password=='12345':
    if(username=='admin' or username=='ADMIN') and password=='12345':
        return 'Access granted'
    else:
        return 'Access denied'
print(admin_login('admin', '12345'))
print(admin_login('admiMM', '12345'))
print(admin_login('ADMIN', '12345'))


def hows_the_weather(temperature):
    # return a message based on the temperature value
    if temperature<40:
        return "It's brisk out there!"
    elif temperature>=40 and temperature<=65:
        return "It's a little chilly out there!"
    elif temperature >85 and temperature<100:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

print(hows_the_weather(40))
print(hows_the_weather(50))
print(hows_the_weather(60))
print(hows_the_weather(70))
print(hows_the_weather(90))

def fizzbuzz(num):
#   return fizz if num is divisible by 3
# return buzz if divisible by5
# return fissbuzz if divisible by both
    if num%5==0 and num%3==0:
        return 'FizzBuzz'
    elif num%3==0:
        return 'Fizz'
    elif num%5 ==0:
        return 'Buzz'
    else:
        return num
   
print(fizzbuzz(9))
print(fizzbuzz(10))
print(fizzbuzz(15))
print(fizzbuzz(7))

def calculator(operation, num1, num2):
    operations={
        "+": lambda a, b: a+b,
        "-": lambda a, b: a-b,
        "*": lambda a, b: a*b,
        "/": lambda a, b: a/b,
    }
    if operation in operations:
        return operations[operation](num1, num2)
    else:
        print("Invalid operation!")
        return None

  
print (calculator("-", 3, 1))
print (calculator("+", 3, 1))
print (calculator("*", 3, 2))
print (calculator("/", 3, 2))
