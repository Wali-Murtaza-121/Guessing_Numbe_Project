import random
from art import logo

print(logo)

number_arr = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21,
    22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59,
    60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78,
    79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97,
    98, 99, 100
]
EASY_level = 10
HARD_LEVEL = 5
random_picker = random.choice(number_arr)
difficulty = 0


def attempt_calculation():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        attempts = EASY_level
        return attempts
    else:
        attempts = HARD_LEVEL
        return attempts


def check_answer(guess, random_picker, attempts):
    if guess > random_picker:
        print("Too high!")
        return attempts - 1
    elif guess < random_picker:
        print("Too low!")
        return attempts - 1
    else:
        print(f"You got it! The answer was {random_picker} .")


def game():
    print("Welcome to the Number Guessing game!")
    print("I'm thinking a number between 1 and 100.")

    attempts = attempt_calculation()
    guess = 0
    while guess != random_picker:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Guess a Number: "))
        attempts = check_answer(guess, random_picker, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return

        elif guess != random_picker:
            print("Guess Again.")


game()