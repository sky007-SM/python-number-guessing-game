import random
def guessgame():
    print("\nGuess my number from 0 to 100, within 5 attempts")
    target = random.randint(0,100)
    attempts = 5
    lost = True
    while attempts > 0:
        try:
            answer = int(input("\nEnter your Guess:"))
        except ValueError:
            print("Enter a number as input")
            continue
        else:    
            if answer == target:
                print("Yes, " + str(target) + " is my number")
                print("You have Won\n")
                lost = False
                break

            elif (answer - target) <= 5 and (answer - target) >= -5 :
                print("That is not my number, but you are extremely close")
            elif answer > target:
                print("This number is higher than my number")
            elif answer < target:
                print("This number is lower than my number")    
            attempts -= 1
            print("Attempts Left: ", attempts)
    if lost:
        print("\nYou've Run Out of Attempts")
        print("My number was " + str(target) + "\n")



def main():
    print("| GUESS THE NUMBER | ")
    choice = input("\nPress 's' to Start\t\t Press q to Quit")
    while choice.lower() != "q":
        guessgame()
        choice = input("Play again or Quit : s/q")
        while choice.lower() not in ['s', 'q']:
            print("Invalid choice entry")
            choice = input("Play again or Quit : s/q")
main()