word_list=["aardvark","baboon","camel"]

import random
chosen_word= random.choice(word_list)
print(chosen_word)
lives = 6
game_over = False
on_going = []
count = len(chosen_word)
length_of_disp = 0
cutter = False
while  count == len(chosen_word) and lives > 0 and cutter == False :
    for abc in chosen_word:
        guess = input("Guess a letter:\n  ").lower()
        display = ""
        for word in chosen_word:
            #length_of_disp = len(display)
            if guess == word :
                display += word
                on_going.append(guess)
                count -= 1
            elif word in on_going :
                 display += word
            else:
                display+= "_"
            if "_" not in display:
                cutter = True
        if guess not in chosen_word:
            lives -= 1
            print("wrong guess")
            print(f"lives left : {lives}")
        print(display)
    if count != len(chosen_word):
        print("You won.")
        break
    if lives == 0 :
        print("you lost")























#
#
# while len(display) < len(chosen_word) and lives > 0  :
#     guess = input("Enter a guess : ").lower()
#     for abc in chosen_word:
#         if guess == abc:
#             display += abc
#             on_going.append(guess)
#             print(display)
#         elif guess != abc:
#             print("wrong input. ")
#         else:
#             display += "_"
