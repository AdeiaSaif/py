# # Exercise: Functions in python
# 1. Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,

def calculate_area(base,height):
    return (1/2)*base*height

base=eval(input("Enter base value: "))
height=eval(input("Enter height value: "))
print(calculate_area(base,height))
# 2. Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# ```
# rectangle area=length*width
def calculate_area(base,height,shape="triangle"):
    if shape=="triangle":
        return (1/2)*base*height
    else:
        return base*height

# If no shape is supplied then it should take triangle as a default shape
base=eval(input("Enter base value: "))
height=eval(input("Enter height value: "))
print(calculate_area(base,height,"triangle"))
print(calculate_area(base,height,"rectangle"))
print(calculate_area(base,height))
# ```

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
def print_pattern(n):
    for i in range(n+1):
        print("*"*i)
print_pattern(3)
print_pattern(4)
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/10_functions/10_functions_exercise.py)