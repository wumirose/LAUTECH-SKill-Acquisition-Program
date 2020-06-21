"""Module docstrings.

This module demonstrates how to create a python module that can be imported into python code for reusability

Available Functions: This module harbours 5 functions which are:

func1() :It takes one no parameter but 'Hello Stranger'
greet(name) :It takes one parameter which is name and return 'Hello + name_specified
greet2(name, gender): takes 2 parameter ie. name and gender of users
greet3(*names): Accepts arbitrary umber of parameters
calc(num): Returns the square of a number
student_age(dictionary): Accepts dictionary to return the age of students in the dictionary

Importing the module:
        1. Make sure this module is saved in the same directory / folder with your currently running program
        2. type import myMod
"""

# A function without parameters/variable/arguments
def func1():
    print('Hello Stranger')
    
    
# A function with parameters/variable/arguments

#Function to greet someone whose name will be specified
def greet(name):
    print('Hello, ', name)
    
    
#Function to greet someone whose based on his or her gender   
def greet2(name, gender):
    if gender in ['Male', 'MALE', 'M', 'm', 'male']:
        print('Hi', name, 'we welcome you brother')
    else:
        print('Hi', name, 'we welcome you Sister')


# A function with arbitrary number of parameters with *
def greet3(*names):
    for name in names:
        print('Hello', name, 'Welcome to Python Class')
        import time
        time.sleep(1)
        

def calc(num):
    global square
    square = num**2
    print('the square of {} is {}'.format(num, square))


def student_age(dictionary):
    for student, age in dictionary.items():
        print('The Age of', student, 'is', age)
