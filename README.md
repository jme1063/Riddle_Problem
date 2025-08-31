----------Overview----------

This project is a Python-based riddle game. It includes two implementations:
- A simple procedural version using print statements and a list of acceptable answers.
- An Object-Oriented Programming (OOP) version, where riddles are represented as objects with attributes and methods.

Both versions allow the user to answer riddles and check correctness.

----------Features----------

Version 1: Simple Approach

- Uses `print()` statements and `input()` to interact with the user.
- Accepts multiple correct answers, accounting for:
    - Case differences (e.g., Egg vs. egg)
    - Singular and plural forms (e.g., egg, eggs)
    - Checks the user’s input against a list of acceptable answers and displays whether it is correct.

Version 2: Object-Oriented Approach

- Defines a Riddle class with:
    - question and answers as attributes
    - `ask_riddle()` and `check_answer()` as methods to interact with the user
- Creates multiple riddle objects and asks them to the user in sequence.
- Demonstrates the benefits of OOP:
    - Encapsulation (data + behavior in one object)
    - Reusability (easy to create new riddles)

----------Usage----------

- Simple Version
    - The program asks a riddle and waits for user input.
    - Displays whether the answer is correct.

- OOP Version
    - The program asks each riddle in order.
    - Checks the user’s answer against the list of acceptable answers stored in the object.

----------Requirements----------

- Python 3.x
- No additional packages required