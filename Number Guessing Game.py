import random

def ask_for_guess(min_num, max_num):

    while True:
        user_input = input(f"Take a guess ({min_num}-{max_num}): ")

        try:
            guess = int(user_input)

            if guess < min_num or guess > max_num:
                print(f"Oops! Stay within {min_num} and {max_num}.")
                continue

            return guess

        except ValueError:
            print("That doesn't look like a number. Try again.")


def run_round():
    min_num, max_num = 1, 100
    secret = random.randint(min_num, max_num)
    tries = 0

    print("\n I've chosen a number between 1 and 100.")
<<<<<<< HEAD
    print("Let's see how quickly can you guess it!")
=======
    print("Let's see how quickly you can guess it!")
>>>>>>> 232c3765fd5d26d36df656d1aca65e0ec428b6dd

    while True:
        guess = ask_for_guess(min_num, max_num)
        tries += 1

        if guess < secret:
            print("Too low… go higher.")
        elif guess > secret:
            print("Too high… go lower.")
        else:
            print(f" Nice! You got it in {tries} tries.")
            break


def start_game():
    print("Welcome to the Number Guessing Game!")

    while True:
        run_round()

        play_again = input("\nWant to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print(" Thanks for playing. See you next time!")
            break


start_game()
