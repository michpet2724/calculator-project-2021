print("welcome to the calorie calculator!")

# Ask if they are m/f 

gender = input("Are you male or female? ")

if gender == ("male"):
    msg = "The reccomended calorie intake for your group is 2,500. This may vary based on height/weight/age."

elif gender == ("female"):
    msg = "The recommended calorie intake for your group is 2,000. This may vary based on height/weight/age."

#return msg
print(msg)

# Figure out amount of calories for each food group: fruits, vegetables, grains, meats, and dairy

