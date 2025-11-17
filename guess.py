word_list=["aardvark","baboon","camel"]

import random
chosen_word= random.choice(word_list)
print(chosen_word)
lives = 6
game_over = False
on_going = []
guessed=0
while guessed!=len(chosen_word) and lives!=0:
    guess = input("Guess a letter:\n  ").lower()
    display = ""
    for word in chosen_word:
        if word == guess :
            display += word
            on_going.append(guess)
            guessed+=1
        elif word in on_going :
            display += word
        else:
            display+= "_"
    if guessed==len(chosen_word):
        print('You Win')
    if guess not in chosen_word:
        lives -= 1
        print(f"lives left = {lives}")
    if lives==0:
        print('You Loose')
    print(display)
