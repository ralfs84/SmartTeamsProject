from test import myList

print(myList[1])
guess = input('guess\n')
while len(guess) != 4:
    guess = input('enter a guess\n')
    

if guess in myList:
     print("win")

