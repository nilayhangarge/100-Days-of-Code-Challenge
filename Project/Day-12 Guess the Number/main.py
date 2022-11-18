#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

def stage():
  if level == "easy":
    # count = 10
    return 10
  elif level == "hard":
    # count = 5
    return 5
  else:
    print("Enter a valid level, please.")
    return 0
  
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 & 100.")
level = input("Choose a difficulty. Type 'Easy' or 'Hard': ").lower()
count = stage()

number = random.randint(1,100)
while count != 0:
  print(f"\nYou have {count} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  # print(f"The answer is {number}.")
  if guess == number:
    print(f"You got it! The answer was {number}.")
    break
  elif count != 0:
    count = count - 1
    if guess < number:
      print("Low.")
    # elif abs(guess-number) < 50:
    #   print("Too Low")
    # elif abs(guess-number) > 50:
    #   print("Too High")
    elif guess > number:
      print("High.")
  if count == 0:
    print("\nYou've run out of guesses, you lose.")
    print(f"The answer was {number}")
  elif count != 0:
    print("Guess again.")


    


    