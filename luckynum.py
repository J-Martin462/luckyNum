import random

# Ramdom list gen
numList = [random.randint(1,70)]
print (numList)

i=1
while i != 70:
    numList.append(random.randint(1,70))
    i+=1

#var and Lst setup
keyLst = []

guessLst = []

i=1 

cont = True

guess = 71

setLst = set(numList)

#creation of the guessing list
while i != 6:
    keyLst.append(setLst{1})
    i+=1
    print(keyLst)

#user input checkpoints
while cont == True:
    int(guess)
    while str(guess).isdigit() == False:
        print('Please only enter a number.')
        guess = input('Enter a number 1 - 70: ')
    while str(guess).isdigit() == False or int(guess) > 70:
        if guess > 70:
            print('Enter a number less than or equal to 70')
            guess = input('Enter a number 1 - 70: ')
        elif guess.isdigit() == False:
            print('Please only enter a number')
            guess = input('Enter a number 1 - 70: ')
    guessLst.append(guess)

    print(guessLst)

    if len(guessLst) == 5:
        cont == False



