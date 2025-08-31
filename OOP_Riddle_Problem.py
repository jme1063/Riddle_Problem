"""
Jacqueline Ebel

    This is a simple project to demonstrate a riddle game in Python, but now using
    Object Oriented Programming (OOP).

"""
class RiddleGame:
    # Initialize object with attributes
    def __init__(self, riddle, correct_answers):
        self.riddle = riddle
        self.correct_answers = correct_answers

    # Method to ask the riddle
    def ask_riddle(self):
        print("Here's your riddle:")
        answer = input(self.riddle)
        self.check_answer(answer)

    # Method to check the answer
    def check_answer(self, answer):
        if answer in self.correct_answers:
            print("That is correct!")
        else:
            print("Incorrect!")

def main():
    # Define riddles and their answers
    riddle1 = ("What can run but has no legs? ", ["river", "a river", "A River", "A river", "River"])
    riddle2 = ("What has a head and a tail but no body? ", ["a coin", "coin", "Coin" "coins", "A coin", "Coins"])
    riddle3 = ("What has to be broken before you can use it? ", ["egg", "an egg", "eggs", "Egg", "An egg", "Eggs"])

    # Ask each riddle
    for riddle, answers in [riddle1, riddle2, riddle3]:
        game = RiddleGame(riddle, answers)
        game.ask_riddle()
        print()  # Blank line between riddles

# Start the game
if __name__ == "__main__":
    main()
