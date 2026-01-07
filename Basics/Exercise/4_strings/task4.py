# ## Exercise: String in Python

# 1. Create 3 variables to store street, city and country, now create address variable to
# store entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
street="xyz street,"
city="karachi"
country="Pakistan"
address1=street+" "+city+" "+country
address2=f"{street} {city} {country}"
print("Address 1=>",address1)
print("Address 2=>",address2)
# Now Print the address in such a way that the street, city and country prints in a separate line
print(f"{street}\n{city}\n{country}")
# 2. Create a variable to store the string "Earth revolves around the sun"
#     1. Print "revolves" using slice operator
#     2. Print "sun" using negative index
text="Earth revolves around the sun"
print(text[6:14])
print(text[-3:])

# 3. Create two variables to store how many fruits and vegetables you eat in a day.
# Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
vegetables=2
fruits=3
print(f"I eat {vegetables} veggies and {fruits} fruits daily")
# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a
# wrong statement, the correct statement is 'maine 10 samosa khaye'.
# Replace incorrect words in original strong with new ones and print the new string.
# Also try to do this in one line.
s='maine 200 banana khaye'
s= s.replace("200","10")
print(s)
# [Solution](https://github.com/codebasics/py/blob/master/Basics/Exercise/4_strings/4_string_exercise_answer.py)
