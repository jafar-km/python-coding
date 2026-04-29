# TODO-1: Ask the user for input
import art
print(art.logo)
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added


def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


Bidders = {}

continue_bidding = True
while continue_bidding :
    name = input("What is your name?\n")
    bid = int(input("What is your bid?: $\n"))
    Bidders[name] = bid
    new_bid = input("Are there any other bidders? Types 'yes' or 'no'.\n").lower()
    if new_bid == "no" :
        continue_bidding = False
        find_highest_bidder(Bidders)
    elif new_bid == "yes" :
        print("\n" * 100)






