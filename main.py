from pydoc import text
from Dictionary import myList
import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

x = random.randint(0, len(myList) - 1)
count = 1

#answer = "bull"
answer = myList[x]
answer = answer.lower() #converts to lower case
answer = answer.strip()
#wrong = []
counter = 1
wrong = ""
temp = ""
tguess = ""
ColourPrint = ""
PreviousAnswers = ""
#print(answer + ' is the answer')
guess = input('enter a guess\n')
guess = guess.lower() #converts to lower
guess = guess.strip()

while guess != answer:# while guess is not just The Answer
    if guess in myList:
        print('Not the word but is in list\n') ## will continue asking until the word provided is in the list of EXISTING words/removes gibberish
        tanswer = answer
        tguess = guess
        for i in range (4):
            gcount = tguess.count(guess[i])#count how many times letter is in guessed word
            acount = tanswer.count(guess[i])#count how many times letter is in answer
            if tguess[i] == tanswer[i]: 
                ColourPrint = ColourPrint + GREEN + guess[i] + RESET

                tanswer = tanswer[:i] + " " + tanswer[i+1:]
                tguess = tguess[:i] + " " + tguess[i + 1:]
            elif tguess[i] != tanswer[i] and tguess[i] in tanswer and gcount <= acount:#compare how many times letter shows up so if 3 in guess but answer on has 2 the one letter will be skipped and made red
                ColourPrint = ColourPrint + YELLOW + guess[i] + RESET

                tguess = tguess[:i] + " " + tguess[i + 1:]
            else:
                ColourPrint = ColourPrint + RED + guess[i] + RESET
              
                tguess = tguess[:i] + " " + tguess[i + 1:]
                if guess[i] not in wrong:
                        wrong = wrong + guess[i] +","
        counter = counter + 1
        tanswer = answer
        tguess = guess
        if counter == 5:
            break       

        print("-------------------------------------------------------------\n")                
       
        PreviousAnswers = PreviousAnswers + "\n" + ColourPrint
        print(PreviousAnswers)
        temp = ""
        ColourPrint = ""                    
        print("-------------------------------------------------------------\n")
        print("leters not in word: " + wrong)    
        print("Attempt : " + str(counter))                                      
        guess = input('Enter a new guess\n')    

    elif guess not in myList:
        guess = input('Not a word\nEnter a new guess\n')

if answer == guess:
    print("Yippeeeee the word was ")
    print(answer)
else:
    print("Looooooser answer was ")
    print(answer)


                   