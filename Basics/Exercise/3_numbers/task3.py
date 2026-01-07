# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
# area using python and print it.
l=92
w=48.8
print("Area: ", l*w)
# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
#  and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
packets=9
packets_price=1.49
gave=20
print(gave-(packets*packets_price)," dollars is the shopkeeper going to give me back")
# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
# is its length. If tiles cost 500 rs per square feet, how much will be the total
# cost to replace all tiles. Calculate and print the cost using python
# (Hint: Use power operator ** to find area of a square)
side = 5.5
cost_per_sqft = 500
area = side ** 2
total_cost = area * cost_per_sqft
print(total_cost, "rs is the total cost to replace all tiles")


# 4. Print binary representation of number 17
print("binary representation of number 17 ",bin(17))