import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
keep_dealing = True


def start_game():
    play_game = input("\nDo you want to play a game of blackjack? y or n: ")
    if play_game == "n":
        exit()

    player_cards = [random.choice(cards),random.choice(cards)]
    player_score = sum(player_cards)

    computer_cards = [random.choice(cards),random.choice(cards)]

    def computer_new_card():
        computer_score2 = sum(computer_cards)
        while computer_score2 < 17:
            return computer_cards.append(random.choice(cards))
            computer_score2 = sum(computer_cards)
    
    computer_new_card()

    print(f"\nYour cards: [{player_cards[0]}, {player_cards[1]}], current score: {player_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    def new_card():
        return player_cards.append(random.choice(cards))

    def end_game():
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        print(f"\nYour final hand is {player_cards}, final score: {player_score}")
        print(f"Computer's final hand is {computer_cards}, final score: {computer_score}")
        if player_score <= 21 and player_score > computer_score:
            print("You win!")
        elif computer_score > 21 and player_score <= 21:
            print("You win!")
        elif player_score <=21 and player_score == computer_score:
            print("It's a draw.")
        else:
            print("You lose.")
        keep_dealing = False
        start_game()

    new_card_input = input("\nType y to get another card, n to pass: ")
    if new_card_input == "y":
        keep_dealing = True
    else:
        end_game()

    while keep_dealing == True:
        player_score = int(sum(player_cards))
        if player_score > 21:
            end_game()
        if player_score <= 21:
            new_card()
            player_score = sum(player_cards)
            print(f"Your cards: {player_cards}, current score: {player_score}")
            if player_score > 21:
                end_game()
            else:
                new_card_input2 = input("\nType y to get another card, n to pass: ")
                if new_card_input2 == "n":
                    end_game()
        
start_game()


