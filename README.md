<h1>Lesson 2: Assignments: Nested If</h1>

<h3>1. Nested Decisions: The Adventure Game 🏰</h3>

<h6>Objective:</h6> To practice the use of nested if statements.

<h5>Task 1: Code Correction</h5> You are provided with a Python script that is supposed to guide a user through an adventure game, but it has some errors. Identify and fix them.

<h5>Buggy Code:</h5>

```
place = input("Choose a place: forest or cave? ")

if place = "forest":
    action = input("climb a tree or cross a river?")
    if action = "climb a tree":
        print("You found a bird's nest!")
    else action = "cross a river":
        print("You found a boat!")
elif place = "cave":
    print("You find a hidden treasure!")
```
<h5>Task 2: Setting the Scene</h5>

Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.

<h5>Task 3: Default Path</h5>

If the user makes an invalid choice at any point, incorporate a pass statement to handle it. HINT: How can an else statement be of use here?
<hr>

<h3>2. Quick Decisions: The Event Planner 🎉</h3>

<h6>Objective:</h6> To practice the use of shorthand if statements.

<h5>Task 1: Code Correction</h5> You are provided with a Python script that is supposed to help in event planning, but it has errors. Identify and fix them.

<h5>Buggy Code</h5>

```
attendees = input("Enter number of attendees: ")
venue = "large hall" if attendees > 100 else "conference room"
print(venue)
```
<h5>Task 2: Venue Selection</h5>

Based on the corrected code from Task 1, further enhance your code to recommend additional things like "audio system" or "projector" based on the number of attendees.

<h5>Task 3: Catering Choices</h5>

Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".

<h6>NOTE:</h6> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements or print statements, they should function correctly and display output in the console as expected.
<br><br>

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.