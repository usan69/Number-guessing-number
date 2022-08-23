from random import randint
from art import logo
from art import logo_error
from replit import clear

EASY_LEVEL = 11
MEDIUM_LEVEL = 9
HARD_LEVEL = 7
EXPERT_LEVEL = 4


def check_answer(guess, answer, turns):
    if guess > answer:
        print("Your guess is too high! sweetheart")
        return turns - 1
    elif guess < answer:
        print("Your guess too low babe")
        return turns - 1
    else:
        print(f"You got the answer baby. the answer was {answer} ")


def set_difficulity():
    level = input("Choose the difficulity type- 'expert' 'hard' 'medium' 'easy' ")
    if level == "easy":
        return EASY_LEVEL
    elif level == "medium":
        return MEDIUM_LEVEL
    elif level == "hard":
        return HARD_LEVEL
    elif level == "expert":
        return EXPERT_LEVEL
    else:
        clear()
        print("Invalid difficulity. Game error!")
        print(logo_error)
        re = input("Press enter to restart")
        return game()


def game():
    print(logo)
    print("Welcome to NUMBER GUESSING NUMBER!")
    print("Please thinking of a number between 1 and 100 !")
    answer = randint(1, 100)
    print(" You have to Guess a number which is in 1-100 ")
    turns = set_difficulity()

    guess = 0
    while guess != answer:
        # turns=set_difficulity()
        print(f"You have {turns} attempts remaining to guess the exact number! :) ")
        guess = int(input("Guess a number :"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You lose your all attempts before guessing the correct number, SORRY!")
            return
        elif guess != answer:
            print("Guess again")


game()