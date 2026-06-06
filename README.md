# Number Guessing Game

A Python CLI game where the player tries to guess a randomly generated number within limited attempts. Game has difficulty levels, score system assigned based on difficulty, and improved hint system. Users can replay to get higher scores. New addition of an Impossible difficulty level.

## Features
- Random number generation
- Hint system
- Attempt tracking
- Input validation
- Loop for repeated play
- Reusable game function  
- Difficulty level
- Reusable Score system 
- Reusable Hint system
- An Impossible difficulty level

## Concepts Used
- Variables
- Input/output
- Conditionals
- Looping statements
- Exception handling
- Uses Functions
- State Tracking 
- Random values
- Arguments in Functions
- Game Design logic
- String Manipulation

## Run

```bash
python3 main.py
```

## Score Calculation

The game rewards players based on both the selected difficulty and the number of attempts remaining after a successful guess.

### Formula

```python
Easy       : remaining_attempts × 11.12
Medium     : remaining_attempts × 16.7
Hard       : remaining_attempts × 25
Impossible : remaining_attempts × 100
```

The final score is converted to an integer before being displayed.

### Score Multipliers

| Difficulty | Range    | Attempts | Multiplier |
|------------|----------|----------|------------|
| Easy       | 0 - 50   |    10    |     11.12  |
| Medium     | 0 - 100  |     7    |     16.7   |
| Hard       | 0 - 200  |     5    |     25     |
| Impossible | 0 - 1000 |     3    |    100     |

Higher difficulties provide larger score multipliers because the target number is harder to find with fewer guesses.

---

## Hint System

After every incorrect guess, the game provides a hint based on how close the player's guess is to the target number.

### Hint Conditions

| Difference from Target | Hint                                                                        |
|------------------------|-----------------------------------------------------------------------------|
|         ≤ 1            | "This is as close to my number as possible"                                 |
|         ≤ 5            | "That is not my number, but you are extremely close"                        |
|         ≥ 500          | "This number is miles away from my number, you have no chance at this rate" |
|         ≥ 100          | "This number is far from my number"                                         |
|     Guess > Target     | "This number is higher than my number"                                      |
|     Guess < Target     | "This number is lower than my number"                                       |

### Examples

Target Number: `75`

| Player Guess | Difference | Hint                  |
|--------------|------------|-----------------------|
|       74     |       1    | As close as possible  |
|       79     |       4    | Extremely close       |
|      180     |     105    | Far from my number    |
|      900     |     825    | Miles away            |
|       90     |      15    | Higher than my number |
|       60     |      15    | Lower than my number  |

The hint system helps guide players toward the correct number while preserving the challenge of each difficulty level.