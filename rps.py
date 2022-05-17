import random

# define variables
rock = "rock" 
paper = "paper"
scissors = "scissors"

# print game initializing montra
print("Rock,")
print("Paper,")
print("Scissors,")
print("SHOOT!")

# organize the choices in an array
choices = [rock, paper, scissors]

# make AI chose a random object within the array
ai = random.choice(choices) 

# take user input
user = input()

# print AI choice 
print("AI chooses:")
print(ai)

# calculating winner, loser, and tie
if user == ai:
    print("Tie, ReThrow")
elif user == rock and ai == scissors:
    print("User wins!")
elif user == rock and ai == paper:
    print("AI wins!")
elif user == paper and ai == scissors:
    print("AI wins!")
elif user == paper and ai == rock:
    print("User wins!")
elif user == scissors and ai == rock:
    print("AI wins!")
elif user == scissors and ai == paper:
    print("User wins!")