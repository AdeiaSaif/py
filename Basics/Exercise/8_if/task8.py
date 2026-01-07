# ## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
#     1. Write a program that asks user to enter a city name and it should tell which country the city belongs to
user=input("city: ")
print("india" if user in india else "pakistan" if user in pakistan else "bangladesh")
#     2. Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"
city1=input("city1: ")
city2=input("city2: ")
print("both cites are in same India" if (city1 in india) and (city2 in india) else "Both cites are in same Pakistan" if (city1 in pakistan) and (city2 in pakistan) else "Both cites are in same Bangladesh" if (city1 in bangladesh) and (city2 in bangladesh) else "Both cites are not in same Country" )
# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
#     1. Ask user to enter his fasting sugar level
#     2. If it is below 80 to 100 range then print that sugar is low
#     3. If it is above 100 then print that it is high otherwise print that it is normal
user=eval(input("sugar level: "))
if user<80:
    print("Low")
elif user>100:
    print("High")
else:
    print("Normal")
# [Solution - Exercise 1.i](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_1.py)

# [Solution - Exercise 1.ii](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise1_2.py)

# [Solution - Exercise 2](https://github.com/codebasics/py/blob/master/Basics/Exercise/8_if/8_exercise2.py)