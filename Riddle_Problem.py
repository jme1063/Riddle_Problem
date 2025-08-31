"""
Jacqueline Ebel

    This is a simple project to demonstrate a riddle game in Python.

"""


print("Here's your riddle:")

answer = input("What has to be broken before you can use it? ")
correct_answers = ["egg", "an egg", "eggs", "Egg", "An egg", "Eggs"]

if answer in correct_answers:
    print("That is correct!")
else:
    print("Incorrect!")