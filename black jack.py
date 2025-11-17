import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
dealer_dec = []
player_dec = []
def want_to_play():
    again = input("Do you want to play (yes or no) : ").lower()
    if again == "yes":
        draw_cards()
        dealers_draw()
        players_draw()
        final()
        round2()
        want_to_play()
def draw_cards():
    while len(player_dec) < 2 :
        player_dec.append(random.choice(cards))
    while len(dealer_dec) < 2 :
        dealer_dec.append(random.choice(cards))
def winner():
    if sum(player_dec) > sum(dealer_dec) and sum(dealer_dec) < 21:
        dealer_dec.append(random.choice(cards))
        dealers_draw()
    if sum(dealer_dec) >= 21:
        print("You Won!!!!")
    if sum(player_dec) < sum(dealer_dec) <= 21:
        dealers_draw_unhidden()
        print("You Lost !!!")
    if sum(dealer_dec) < sum(player_dec) <= 21:
        print("you won!!!!!!!!!!!")
    if sum(player_dec) == sum(dealer_dec) and sum(player_dec) <= 21 and sum(dealer_dec)<=21:
        dealers_draw()
        print("Its a Draw.")

def round2():
    ask = input("Do you want to Hit or Stay : ").lower()
    if ask == "hit" :
        player_dec.append(random.choice(cards))
        final()
        players_draw()
        winner()
    if ask == "stay":
        players_draw()
        winner()
def final():
    while sum(player_dec) > 21 :
        dealers_draw_unhidden()
        print("you lost!!!")
        exit()
def dealers_draw_unhidden():
    print(f"dealers draw : {dealer_dec[0]} + {dealer_dec[1]} : {sum(dealer_dec)}")
def dealers_draw():
    if len(dealer_dec) == 2 :
        print(f"dealers draw : {dealer_dec[0]} + hidden{dealer_dec[1]}")
    if len(dealer_dec) > 2 :
        print(f"dealers draw : {dealer_dec[0]} + {dealer_dec[1]} + {dealer_dec[2]} : {sum(dealer_dec)}")
def players_draw():
    if len(player_dec) == 2 :
        print(f"players draw : {player_dec[0]} + {player_dec[1]} : {sum(player_dec)}")
    if len(player_dec) == 3 :
        print(f"players draw : {player_dec[0]} + {player_dec[1]} + {player_dec[2]} : {sum(player_dec)}")
want_to_play()