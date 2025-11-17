print("Welcome to bid simulator!!!\n")
again = "yes"
name = str([])
bid = int()
book = {}
while again == "yes" : 
    name = input("What is your name? :")
    bid = int(input("Place your bid : "))
    book[name] = bid
    again = input("Is there anyone else who wants to bid ?(yes/no) : ")
    print("\n" *20)


if book:
    winner = max(book.values())
    winner_name = max(book,key=book.get)
    print(winner)
    print(f"Winner of the auction is {winner_name} with the bid of {winner}.")
else:
    print("No bids were placed.")
# print(book)