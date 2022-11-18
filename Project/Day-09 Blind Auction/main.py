from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
print("Welcome to the Secret Auction Program.")
repeat = "yes"
bidding = {}
while repeat == "yes":
  key = input("\nWhat is your name? ")
  value = int(input("What's your bid? $"))
  bidding[key] = value
  repeat = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  # clear()

max = 0
for unit in bidding:
  compare = bidding[unit]
  if compare > max:
    max = compare

print(f"\nThe winner is {unit} with a bid of ${max}.")