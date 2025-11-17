print("welcome to pizza place!!")
size = input("What size of pizza do you want? S M or L : ")
bill = 0
#size
if size == "S" or size=="s":
    bill +=100
elif size== "M" or size=="m":
    bill +=150
elif size=="L" or size=="l":
    bill+=180
else :
    print("wrong input given")
#for peperoni
pep = input("do you want any peperoni on your pizza? Y or N : ")
if pep== "Y" or pep=="y" :
    if size=="S" or size=="s":
        bill+=30
    elif size=="M" or size=="m":
        bill+=40
    else:
        bill+=50
else:
    print("no peperoni.")
#for cheese
che = input (" do you want extra cheese? Y or N : ")
if che== "Y" or che=="y":
    if size=="S" or size=="s":
        bill+=30
    elif size=="M" or size=="m":
        bill+=40
    else:
        bill+=50
else:
    print("no extra cheese.")
print(f"Your total bill is {bill}rs")