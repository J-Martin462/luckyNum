import random

# Ramdom list gen
numList = set()
print (numList)

i=1
while i != 70:
    numList.add(random.randint(1, 70))
    i+=1

#var and Lst setup
keyLst = []

guessLst = []

i=1 

cont = True

guess = 71
print(numList)
#creation of the guessing list
while i != 6:
    keyLst.append(numList.pop())
    i+=1
    print(keyLst)

# #user input checkpoints
# while cont == True:
#     int(guess)
#     while str(guess).isdigit() == False:
#         print('Please only enter a number.')
#         guess = input('Enter a number 1 - 70: ')
#     while str(guess).isdigit() == False or int(guess) > 70:
#         if str(guess).isdigit() == False:
#             print('Enter a number less than or equal to 70')
#             guess = input('Enter a number 1 - 70: ')
#         elif int(guess) > 70:
#             print('Please only enter a number')
#             guess = input('Enter a number 1 - 70: ')
#     guessLst.append(guess)

#     print(guessLst)

#     if len(guessLst) == 5:
#         cont == False


input("I need to learn how not to leave my computer unlocked.")

input("How long will this go?")

input("Did something else get deleted? Ahhh!!! A mistery.")