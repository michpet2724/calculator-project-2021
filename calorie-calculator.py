print("welcome to the calorie calculator!")

# Ask if they are m/f 

gender = input("Are you male or female? ")

if gender == ("male"):
    msg = "The reccomended calorie intake for your group is 2,500. This may vary based on height/weight/age."

elif gender == ("female"):
    msg = "The recommended calorie intake for your group is 2,000. This may vary based on height/weight/age."

print(msg)

# Figure out amount of calories for each food group: fruits, vegetables, grains, meats, and dairy

# food_groups_fruits = [
#     {"name": "orange", "calories": "45"}
#     #{"name": "apple", "calories": "130"}
#     {"name": "pear", "calories": "102"}
# ]

food_groups = input("Woud you like to know the calories in different foods? ")

if food_groups == "yes":
    ans = "Great let's continue."
    # print(food_groups_fruits)

elif food_groups == "no":
    ans = "That's fine then. Thank you for using the calorie calculator!"


# food_groups_vegetables = [

# ]

# ]

# print("")