import random

# introduce audience to the game
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input(("Choose a difficulty. Type 'easy' or 'hard': "))

# Number Of Lives
if level == 'hard':
    attempts = 5
elif level == 'easy':
    attempts = 10

# Pick a random number to store
random_num = random.randint(1, 100)

# Hard Level
if level == 'hard':
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_num:
            print("Too High!")
            attempts -= 1
            if attempts == 0: 
                print(f"You've run out of guesses, you lose! The answer was {random_num}")
        elif guess < random_num:
            print("Too Low!!")
            attempts -= 1
            if attempts == 0: 
                print(f"You've run out of guesses, you lose! The answer was {random_num}")
        else:
            print("You won!")
            attempts = 0
        
elif level == 'easy':
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > random_num:
            print("Too High!")
            attempts -= 1
            if attempts == 0: 
                print(f"You've run out of guesses, you lose! The answer was {random_num}")
        elif guess < random_num:
            print("Too Low!!")
            attempts -= 1
            if attempts == 0: 
                print(f"You've run out of guesses, you lose! The answer was {random_num}")
        else:
            print("You won!")
            attempts = 0
        

 
