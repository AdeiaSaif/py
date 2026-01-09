# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads
count=0
for i in result:
    if i=="heads":
        count+=1
print(count)
# 2. Print square of all numbers between 1 to 10 except even numbers
for i in range(1,11):
    print(i**2)
# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
user=eval(input("Enter: "))
for i in range(len(expense_list)):
    if user in expense_list:
        if expense_list[i]==user:
            print(f"Month {i}")
    else:
        print("Not found")
        break
        
# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
for i in range(1,6):
    if i!=5:
        user=input("Are you tired? ")
        if user=="yes":
            print("you didn't finish the race")
            break
    elif i==5:
        print("You won")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```
for i in range(1,6):
    print("*"*i)


# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/9_for/9_for_exercise.py)