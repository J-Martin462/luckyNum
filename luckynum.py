import random



numList = [random.randint(1,70)]
print (numList)

i=1
while i != 70:
    numList.append(random.randint(1,70))
    i+=1

guessLst = []

i=1 

while i != 6:
    guessLst.append(numList[random.randint(0,69)])
    i+=1
    print(guessLst)

guess = "we"
while guess.isdigit() == False:
    guess = input('Enter a number 1 - 70')
int(guess)



