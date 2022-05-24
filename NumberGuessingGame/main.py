def set_difficulty():
    difficulty = input("Choose the difficulty 'easy' or 'hard': ")
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5

def check_answer(user_guess, answer, turn_count):
    if user_guess > answer:
        print("Too high")
        return turn_count - 1
    elif user_guess < answer:
        print("Too low")
        return turn_count - 1
    elif user_guess == answer:
        print(f"You got it right! The answer is {answer}.")


def game():
    import random
    #answer is a global variable
    answer = random.randint(1,100)

    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    #sets number_of_turns as global variable
    number_of_turns = set_difficulty()

    keep_guessing = True
    while keep_guessing == True:
        print(f"\nYou have {number_of_turns} attempts to guess")
        #sets user_guess as global variable
        user_guess = int(input("Make a guess: "))

        number_of_turns = check_answer(user_guess, answer, number_of_turns)

        #This needs to go first
        if number_of_turns == 0:
            print("You ran out of turns.")
            #You can use return here instead of keep_guessing = False to exit the entire function early
            return
        elif user_guess != answer:
            print("Guess again: ")
        elif user_guess == answer:
            return

game()


