def game():
    import random


    print("Welcome to Rock Paper and Scissors")
    choice = int(input("enter your choice 0 for rock , 1 for paper and 2 for scissors : "))
    if choice > 2 :
        print("wrong input")
        exit()
    the_game = ['''
        _______
    ---'   ____)
        (_____)
        (_____)
        (____)
    ---.__(___)
    ''',
    '''
        _______
    ---'   ____)____
            ______)
            _______)
            _______)
    ---.__________)
    '''
    ,'''
        _______
    ---'   ____)____
            ______)
        __________)
        (____)
    ---.__(___)
    ''' ]
    # 00 11 22  01 02  10 12  20 21
    print("Your Choice : ")
    print(the_game[choice])
    if choice > 2 :
        print("wrong input")
    bot = random.randint(0,2)
    print("Bots Choice : ")
    print(the_game[bot])
    if bot==0:
        if choice== 0:
            print("draw")
        elif choice== 1:
            print("YOU WIN,  BOT LOST")
        else:
            print("BOT WINS, YOU LOST")
    if bot==1:
        if choice== 0:
            print("BOT WINS, YOU LOST")
        elif choice== 1:
            print("draw")
        else:
            print("YOU WIN,  BOT LOST")
    if bot==2:
        if choice== 0:
            print("YOU WIN,  BOT LOST")
        elif choice== 1:
            print("BOT WINS, YOU LOST")
        else:
            print("draw")

game()

ask=True
while ask==True:
    ask2=input("Do you want to play again : y or n:").lower()
    if ask2=="y":
        game()
    else:
        ask=False

