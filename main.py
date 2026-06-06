# Python Number Guessing Game
import random

# To select difficulty for the user
def choose_difficulty():
    print("Choose Difficulty\nEasy\nMedium\nHard\nImpossible")
    difficulty = input("\nEnter Your choice from above: ")
    while difficulty.lower() not in ["easy", "medium", "hard", "impossible"]: # Handles Invalid choice input
        print("That difficulty level doesn't exist")
        difficulty = input("\nEnter Your choice from above: ")
    # Difficulty level conditions
    if difficulty.lower() == "easy":
        return 50,10
    elif difficulty.lower() == "medium":
        return 100,7
    elif difficulty.lower() == "hard":
        return 200, 5
    elif difficulty.lower() == "impossible":
        return 1000, 3

def guessgame(ceiling, attempts, high_score):
    # To start game based on difficulty
    if ceiling == 50 :
        print("\nGuess my number from 0 to 50, within 10 attempts")
    elif ceiling == 100 :
        print("\nGuess my number from 0 to 100, within 7 attempts")
    elif ceiling == 200 :
        print("\nGuess my number from 0 to 200, within 5 attempts")
    elif ceiling == 1000 :
        print("\n💀 IMPOSSIBLE!!!  \nSure, go ahead. guess number between 1 and 1000 in 3 tries. (You will need a miracle)")
    target = random.randint(0,ceiling) # To set the range of numbers
    lost = True # To track state of game
    count = 0
    while attempts > 0: 
        try:
            answer = int(input("\nEnter your Guess: ")) # Handles Invalid Input 
        except ValueError:
            print("Enter a number as input")   
            continue
        else:    
            count += 1
            if answer == target: # Triggers diaolgue for winning a game
                print("Yes, " + str(target) + " is my number") 
                if ceiling == 1000:
                    print("Congratulations You have done the IMPOSSIBLE!!!")
                print("You have Won in " + str(count) + " attempts\n")
                lost = False
                break
            hint_system(answer,target)
            # Reduces attempts after every turn
            attempts -= 1
            print("Attempts Left: ", attempts)
    # Triggers dialogue for a lost game
    if lost: 
        print("\nYou've Run Out of Attempts")
        print("My number was " + str(target) + "\n")
    score = score_system(ceiling,attempts)
    if score > high_score: # Handles the high score every round
        high_score = score
    print("\n Your Score: ", score)
    return high_score

def hint_system(answer, target):
    # Hints for the player based on different cases
        if abs(answer -target) <= 1:
            print("This is as close to my number as possible")
        elif abs(answer - target) <= 5:
            print("That is not my number, but you are extremely close")
        elif abs(answer - target) >= 500:
            print("This number is miles away from my number, you have no chance at this rate")
        elif abs(answer - target) >= 100:
            print("This number is far from my number")
        elif answer > target:
            print("This number is higher than my number")
        elif answer < target:
            print("This number is lower than my number")

def score_system(ceiling, attempts):
    # Handles score multipliers
    if ceiling == 50:
        score = attempts * 11.12
    elif ceiling == 100:
        score = attempts * 16.7
    elif ceiling == 200:
        score = attempts * 25
    elif ceiling == 1000:
        score = attempts * 100
    return int(score) # Ensures integer score value

def main():
    # Displays game 
    print("| GUESS THE NUMBER | ")
    print("\nPress 's' to Start\t\t Press q to Quit")
    choice = input("Enter choice: ") 
    high_score = 0
    while choice.lower() != "q":
        ceiling,attempts = choose_difficulty() # Function that allows users to set difficulty
        high_score=guessgame(ceiling,attempts,high_score) # Function that runs the game 
        print("\n Highest Score: ", high_score)
        choice = input("Play again or Quit (s/q): ") # Allows player to replay
        while choice.lower() not in ['s', 'q']: # Handles Invalid choice input
            print("Invalid choice entry") 
            choice = input("Play again or Quit (s/q): ")
main()

