
import random

# introduce audience to the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
level = input(("Choose a difficulty. Type 'easy' or 'hard': "))
attempts = 5
print(f"You have {attempts} attempts remaining to guess the number.")
guess = int(input("Make a guess: "))
random_num = random.randint(1, 10)
print(random_num)

if level == 'hard':
    while guess > random_num or guess < random_num:
        if guess > random_num:
            print("Too High!")
        elif guess < random_num:
            print("Too Low!!")
        attempts -= 1
        print(f"you have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
    
print(f"You got it! The answer was {random_num}")   
