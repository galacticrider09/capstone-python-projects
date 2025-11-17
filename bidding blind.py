print("WELCOME TO BIDDING BLIND PROGRAM")
main_dict = {
}
def basic():
    names = input("What is your name ? : ")
    bids = int(input("Enter your bidding amount : "))
    main_dict.update({names : bids , })
    others = input("Are there any other bidders ? yes or no : ")
    print("\n" *100)
    if others == "yes" :
        basic()

basic()

highest_bid = float('-inf')
winner = []

for biddder , bid in main_dict.items():
    if bid > highest_bid:
        winner = biddder
        highest_bid = bid
print(f"{winner} won the auction with ${highest_bid} bid ")