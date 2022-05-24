# Game to guess who has more followers

# data is a list with 50 dictionaries
import random
from game_data import data
from replit import clear

def generate():
    a = random.randint(0,len(data)-1)
    return data[a]
    # return random.choice(data)

def compare(first, second):
    if first['follower_count'] > second['follower_count']:
        return first
    else:
        return second

def anti_compare(first, second):
    if first['follower_count'] < second['follower_count']:
        return first
    else:
        return second

def game():
    print("Welcome to the higher lower game.")
    print("Guess whether A or B has more followers.")
    
    score = 0
    keep_playing = True
        
    first_thing = generate()
    while keep_playing == True:
        print(f"\nCompare A: {first_thing['name']}, {first_thing['description']}, from {first_thing['country']}")

        print("vs.")

        second_thing = generate()
        print(f"Against B: {second_thing['name']}, {second_thing['description']}, from {second_thing['country']}")

        # computer will output "a" or "b" 
        correct = compare(first_thing, second_thing)
        not_correct = anti_compare(first_thing, second_thing)

        user_selection = input("\n").lower()
        if user_selection == "a":
            user_selection = first_thing
        elif user_selection == "b":
            user_selection = second_thing

        clear()
        if user_selection == correct:
            first_thing = correct
            score += 1
            print(f"\nYou're right! Current score: {score}")
        else:
            print(f"\nSorry you lost. {correct['name']} has more followers, at {correct['follower_count']}M compared to {not_correct['name']} at {not_correct['follower_count']}M. Your final score is {score}.")
            keep_playing = False

game()


