
# snake beats water, water beats gun, and gun beats snake.

''''
    1 for snake
    -1 for water
    0 for gun
'''
import random

def game_result(computer, you):
    if computer == you:
        return "Draw"
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        return "You Win!"
    else:
        return "You Lose!"


youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

computer = random.choice([1, -1, 0])

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

if youstr not in youDict:
    print("Invalid input! Please enter s, w, or g.")
else:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}")
    print(f"Computer chose {reverseDict[computer]}")
    print(game_result(computer, you))
