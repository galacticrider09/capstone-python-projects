def guessit():
    print("""

    _______ __   __ _______ _______ _______   _______ __   __ _______   __    _ __   __ __   __ _______ _______ ______   
    |       |  | |  |       |       |       | |       |  | |  |       | |  |  | |  | |  |  |_|  |  _    |       |    _ |  
    |    ___|  | |  |    ___|  _____|  _____| |_     _|  |_|  |    ___| |   |_| |  | |  |       | |_|   |    ___|   | ||  
    |   | __|  |_|  |   |___| |_____| |_____    |   | |       |   |___  |       |  |_|  |       |       |   |___|   |_||_ 
    |   ||  |       |    ___|_____  |_____  |   |   | |       |    ___| |  _    |       |       |  _   ||    ___|    __  |
    |   |_| |       |   |___ _____| |_____| |   |   | |   _   |   |___  | | |   |       | ||_|| | |_|   |   |___|   |  | |
    |_______|_______|_______|_______|_______|   |___| |__| |__|_______| |_|  |__|_______|_|   |_|_______|_______|___|  |_|

    """)


    import random
    print("I am thinking of a random number between 1 and 100!!!\n")
    print("haha try to guess it . . . . .  \n")
    the_number = random.randrange(1,100)

    def hard():
        print("you get 5 lives:")
        def guess_num():
            Lives = 5
            while Lives > 0 :
                guess = int(input("Enter your guess : "))
                if guess == the_number:
                    print(f"congrats you got it!!! the number was {the_number}.")
                    return
                elif guess > the_number :
                    print("too high!")
                    Lives -= 1
                    print(f"You have {Lives} lives remaining.")
                elif guess < the_number :
                    print("too low!")
                    Lives -= 1
                    print(f"You have {Lives} lives remaining.")
            if Lives == 0 :
                    print("You lost!!!! used up all the lives. ")
                    print(f"The number was {the_number}.")
                    return
        guess_num()
    def easy():
        print("you get 10 lives:")
        def guess_num():
            Lives = 10
            while Lives > 0 :
                guess = int(input("Enter your guess : "))
                if guess == the_number:
                    print(f"congrats you got it!!! the number was {the_number}.")
                    return
                elif guess > the_number :
                    print("too high!")
                    Lives -= 1
                    print(f"You have {Lives} lives remaining.")
                elif guess < the_number :
                    print("too low!")
                    Lives -= 1
                    print(f"You have {Lives} lives remaining.")
            if Lives == 0 :
                    print("You lost!!!! used up all the lives. ")
                    print(f"The number was {the_number}.")
                    return
        guess_num()


    game_mode = str(input("What mode do you want to play with Easy or Hard? : " ).lower())
    if game_mode == "easy" :
        easy()
    elif game_mode == "hard":
        hard()
    else :
        print("Invalid input!!!")


guessit()


ask = 1
while ask == 1 :
    again = input("do you want to play again ? y or n :").lower()
    if again == "y":
        guessit()
    else:
        ask += 1