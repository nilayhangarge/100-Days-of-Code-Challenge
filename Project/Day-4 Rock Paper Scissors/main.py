rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
game = [rock, paper, scissors]
game_in = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor\n"))
if game_in >= 3 or game_in < 0:  #0 > game_in >= 3
  print("You typed an invalid Number. You lose")
else:
  user = game[game_in]
  print(user)
  # game_out = random.choice(game)
  game_out = random.randint(0,2)
  
  print(f"\nComputer Choose: {game[game_out]}")
  
  if game_in == 0 and game_out == 2:
    print("You win!")
  elif game_in == 2 and game_out == 0:
    print("You lose")
  elif game_in > game_out:
    print("You win!")
  elif game_in < game_out:
    print("You lose")
  elif game_in == game_out:
    print("Draw")
  elif game_in == 0 and game_out == 2:
    print("You win!")

# if game_in == rock and game_out == rock:
#   print("Draw")
# elif game_in == paper and game_out == paper:
#   print("Draw")
# elif game_in == scissors and game_out == scissors:
#   print("Draw")
# elif game_in == rock and game_out == paper:
#   print("You lose")
# elif game_in == paper and game_out == scissors:
#   print("You lose")
# elif game_in == scissors and game_out == rock:
#   print("You lose")
# elif game_in == rock and game_out == scissors:
#   print("You win!")
# elif game_in == paper and game_out == rock:
#   print("You win!")
# elif game_in == scissors and game_out == paper:
#   print("You win!")