import random

numList = [random.randint(1,70)]
print (numList)

i=1
while i != 70:
    numList.append(random.randint(1,70))
    i+=1

keyLst = []

guessLst = []

i=1 

cont = True

while i != 6:
    keyLst.append(numList[random.randint(0,69)])
    i+=1
    print(keyLst)
while cont == True:
    guess = 71
    while str(guess).isdigit() == False and guess > 70:
        guess = input('Enter a number 1 - 70: ')
        if guess > 70:
            print('Enter a number less than or equal to 70')
        elif guess.isdigit() == False:
            print('Please only enter a number')
    int(guess)

    guessLst.append(guess)

    print(guessLst)

    if len(guessLst) == 5:
        cont == False



