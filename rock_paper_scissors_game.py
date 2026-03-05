import random

def get_choices():
 player_choice = input("Select your reason(rock, paper, scissors):  ")
 game = ["rock","paper","scissors"]
 computer_choice = random.choice(game)

 dict = {"player" : player_choice, "computer" : computer_choice}
 return dict

def check_win(player, computer):
  
  print(f"Your chose: {player}, computer chose: {computer} " )
 
  if player == computer: 
   return "It's a tie"
  elif player == "rock":
    if computer == "scissors":
      return "Player smashed computer! Player Win!"
    else:
     return "Paper cover rock! Computer Win!"
  elif player == "paper":
    if computer == "rock":
      return "Player cover computer! Player Win!"
    else:
     return "scissors cuts the player! Computer Win!"
  elif player == "scissors":
    if computer == "paper":
      return "Player cuts the computer! Player Win!"
    else:
     return "rock crush the player! Computer Win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)