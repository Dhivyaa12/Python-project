import random

print('''RULES OF THE GAME\
      ->"Stone vs Paper - Paper wins \"
      ->"Paper vs Scissor - Scissor wins\"
      ->"Scissor vs Stone - Stone wins"
      ''')

# User input

print("Enter your choice\
'a'-Stone\
'b'-Paper\
'c'-Scissor")
choice = str(input("Enter your choice: "))

if choice == 'a':
    choice_name = "Stone"
elif choice == 'b':
    choice_name = "Paper"
else:
    choice_name = "Scissor"

print('User choice is ', choice_name)
print("Now it's opponents turn..")

player2_choice = random.choice
while player2_choice == choice:
    player2_choice = random.choice

if player2_choice == 'a':
    player2_choice_name = "Stone"
elif player2_choice == 'b':
    player2_choice_name = "Paper"
else:
    player2_choice_name = "Scissor"

print('Player2 choice is', player2_choice_name)
print(choice_name, 'Vs', player2_choice_name)

if choice == player2_choice:
    print('its a Draw', end="")
    result = 'Draw'

if choice == 'a' and player2_choice == 'b':
    print('Paper wins', end="")
    result = 'Paper'

if choice == 'a' and player2_choice == 'c':
    print('Stone wins', end="")
    result = 'Stone'

if choice == 'b' and player2_choice == 'c':
    print('Scissor wins', end="")
    result = 'Scissor'

# printing either user or player2 or draw

    print("User wins")
else:
    print("Player2 wins")

print("THANKS FOR PLAYING")
