import art

logo = art.logo

print(logo)
# TODO-1: Ask the user for input
other_bidders = False

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bidders = {}
bidders['name'] = []
bidders['bid'] = []

def biggest_bidder(name, bid):
    highest_bid = 0
    for i in range(len(bidders['bid'])):
        if bidders["bid"][i] > highest_bid:
            highest_bid = bidders["bid"][i]
            highest_index = i
    print(f"The winner is {bidders['name'][highest_index]} with a bid of {bidders['bid'][highest_index]}")

while not other_bidders:
    username = input("What is your name?: ")
    userbid = int(input("What is your bid?: $"))
    new_bid = input("Are there any other bidders? (yes/no): ")
    if new_bid == 'no':
        other_bidders = True
    else:
        print("\n"*20)

    bidders['name'].append(username)
    bidders['bid'].append(userbid)

# highest_index = bidders['bid'].index(max(bidders['bid']))

biggest_bidder(username, userbid)

# print(f"Name: {bidders['name'][highest_index]}\nBid: {bidders['bid'][highest_index]} ")



