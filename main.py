import random    
def guessgame():
    print("\nGuess my number from 0 to 100, within 5 attempts")
    target = random.randint(0,100) #To set the range of numbers
    attempts = 5 # To adjust difficulty change attempts
    lost = True #To track state of game
    while attempts > 0: 
        try:
            answer = int(input("\nEnter your Guess:")) #Handles Invalid Input 
        except ValueError:
            print("Enter a number as input")   
            continue
        else:    
            if answer == target: #Triggers diaolgue for winning a game
                print("Yes, " + str(target) + " is my number") 
                print("You have Won\n")
                lost = False
                break
            #Hints for the player
            elif (answer - target) <= 5 and (answer - target) >= -5 :
                print("That is not my number, but you are extremely close")
            elif answer > target:
                print("This number is higher than my number")
            elif answer < target:
                print("This number is lower than my number")    
            #Reduces attempts after every turn
            attempts -= 1
            print("Attempts Left: ", attempts)
    #Triggers dialogue for a lost game
    if lost: 
        print("\nYou've Run Out of Attempts")
        print("My number was " + str(target) + "\n")



def main():
    #Displays game 
    print("| GUESS THE NUMBER | ")
    choice = input("\nPress 's' to Start\t\t Press q to Quit") 
    while choice.lower() != "q":
        guessgame() #Function that runs the game 
        choice = input("Play again or Quit : s/q") #Allows player to replay
        while choice.lower() not in ['s', 'q']: # Handles Invalid choice input
            print("Invalid choice entry") 
            choice = input("Play again or Quit : s/q")
main()