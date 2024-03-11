#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return(num1 + num2)

def halve(number):
    return(number / 2)

# def halve(number):
#     number = 100
#     return(f"{number:.2f} / 2")




##### MODULE CODE-ALONG BELOW FOR PR


def my_function(param):
    print("Running my_function")
    return param + 1

my_function_return_value = my_function(1)
print(my_function_return_value)

def stylish_painter():
    best_hairstyle = "Bob Ross"
    return "Jean-Michel Basquiat"
    return best_hairstyle
    print(best_hairstyle)

print(stylish_painter())