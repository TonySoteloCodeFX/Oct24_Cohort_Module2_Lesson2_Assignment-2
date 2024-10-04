print("----------")
print("Task #1")
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

print("----------")
print("Task #2")
food_choice = input("Would you like vegetarian, Yes or No? ").lower()
food = "Veggie Delight Caterers" if food_choice == "yes" else "Gourmet Meals Caterers"
print(food)