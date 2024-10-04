print("---------")
print("Task #1")

place = input("Choose a place: forest or cave?\n").lower()

if place == "forest":
    action = input("climb a tree or cross a river?\n").lower()
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("---------")
    print("Task #2")
    cave_option = input("Would you like to light a torch or proceed in the dark?\n").lower()
    if cave_option == "light a torch":
        print("You've woken up a bear! You're dead!")
    elif cave_option == "proceed in the dark":
        print("You find a hidden treasure!")
    else:
        pass
else:
    pass

