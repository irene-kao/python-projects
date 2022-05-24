from replit import clear

#Creates dictionary where name is the key and bid is the value
keep_bidding = "yes"
bid_dictionary = {}

print("Welcome to the blind auction!")
print("Please have each bidder enter their bid privately.\n")

#Loops through program and see who made highest bid
while keep_bidding == "yes":
    name = input("What is your name?: ")
    bid_value = int(input("What's your bid?: $"))
    bid_dictionary[name] = bid_value

    keep_bidding = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()

    if keep_bidding == "yes":
        clear()

highest_value = 0
for name in bid_dictionary:
    if bid_dictionary[name] > highest_value:
        highest_value = bid_dictionary[name]

print(bid_dictionary)

print(f"The winning bid is {highest_value}.")

