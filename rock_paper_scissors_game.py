import random

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

game_img = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))

if user_choice == 0:
  print("Your choice Rock: " + rock)
elif user_choice == 1:
  print("Your choice paper" + paper)
elif user_choice == 2:
  print("Your choice scissors" + scissors)

computer_chose = random.randint(0, 2)
print("computer_chose: " + game_img[computer_chose])

if user_choice >= 2 or user_choice <0 :
  print("You insert invalid number. you lose")
if user_choice == 0 and computer_chose == 2:
  print("You win")
if user_choice == 1 and computer_chose == 0:
  print("You win")
if user_choice == 2 and computer_chose == 1:
  print("You win")

if user_choice == 0 and computer_chose == 1:
  print("You lose")
if user_choice == 1 and computer_chose == 2:
  print("You lose")
if user_choice == 2 and computer_chose == 0:
  print("You lose")
  
if user_choice == computer_chose:
  print("Game draw")
