import random
choices = ["rock","paper","scissor"]
user_input = input("enter rock,paper,scissor: ")
computer_input = random.choice(choices)
if computer_input == user_input:
    print("tie")
elif computer_input == "rock" and user_input == "scissor":
    print("computer won the match")
elif computer_input == "paper" and user_input == "rock":
    print("computer won the match")
elif computer_input == "scissor" and user_input == "paper":
    print("computer won the match")
else:
    print("user won the match")
