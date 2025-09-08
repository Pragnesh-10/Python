import random

print("Welcome to Number Guessing Game!")
number = random.randint(1, 100)
guess = True
attempts = 0

while guess != number:
    guess = int(input("Enter your guess (1-100): "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Correct! The number was {number}.")
        print(f"You guessed it in {attempts} attempts.")
