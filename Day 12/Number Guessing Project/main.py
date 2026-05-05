import art
import random

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1, 100)

# Choose difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5
else:
    print("Invalid choice.")
    attempts = 0

# Game loop
while attempts > 0:
    guess = int(input(f"You have {attempts} attempts remaining.\nMake a guess: "))

    if guess > random_number:
        print("Too high. Guess again.")
        attempts -= 1

    elif guess < random_number:
        print("Too low. Guess again.")
        attempts -= 1

    else:
        print("You got it! 🎉")
        break

if attempts == 0:
    print(f"You lose! The number was {random_number}.")