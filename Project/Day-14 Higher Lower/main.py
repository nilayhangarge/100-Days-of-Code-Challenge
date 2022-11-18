import random
from art import logo, vs
from game_data import data
from replit import clear

end_of_game = False
score = 0

# Generate a random choice
def random_choice(data):
  return random.choice(data)
  # return (f'{choice["name"]}, a {choice["description"]}, from {choice["country"]}.')

#Calculate the correct answer
def correct_answer():
  if choice1["follower_count"] > choice2["follower_count"]:
    return "a"
  else:
    return "b"

#Final processing for win/lose
def cal(correct, answer, score, end_of_game):
  print(logo)
  if answer != correct:
    print(f"Sorry, that's wrong. Final score: {score}")
    end_of_game = True
    return score, end_of_game
  else:
    score += 1
    end_of_game = False
    print(f"You're right! Current score: {score}\n")
    return score, end_of_game

#Display the art
print(logo)

#Main loop of the program
while end_of_game == False:
  #Select random key for compare A
  choice1 = random_choice(data)
  print(
      f'Compare A: {choice1["name"]}, a {choice1["description"]}, from {choice1["country"]}.'
  )

  print(vs)
  
  #Select random key for compare B
  same = True
  while same == True:
    choice2 = random_choice(data)
    if choice1 != choice2:
      same = False
  print(
      f'\nAgainst B: {choice2["name"]}, a {choice2["description"]}, from {choice2["country"]}.'
  )

  correct = correct_answer()
  # print(correct)

  #Ask user for a guess
  answer = input("\n\nWho has more followers? Type 'A' or 'B': ").lower()
  
  clear()
  score, end_of_game = cal(correct, answer, score, end_of_game)
