from pydoc import text
from Dictionary import myList
import random

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

x = random.randint(0, len(myList) - 1)
count = 1

answer = "bull"
#answer = myList[x]
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
            if tguess[i] == tanswer[i]: 
                ColourPrint = ColourPrint + GREEN + guess[i] + RESET
            
                tanswer = tanswer[:i] + " " + tanswer[i + 1:]
                tguess = tguess[:i] + " " + tguess[i + 1:]
            elif tguess[i] != tanswer[i] and tguess[i] in tanswer:
                ColourPrint = ColourPrint + YELLOW + guess[i] + RESET

                tanswer = tanswer[:i] + " " + tanswer[i + 1:] 
                tguess = tguess[:i] + " " + tguess[i + 1:]
            else:
                ColourPrint = ColourPrint + RED + guess[i] + RESET
              
                tanswer = tanswer[:i] + " " + tanswer[i + 1:]
                tguess = tguess[:i] + " " + tguess[i + 1:]
                
                if guess[i] not in wrong:
                        wrong = wrong + guess[i] +","
               

            """temp = temp + guess[i]   

            if tguess[i] == tanswer[i]:
                #print("Position", i + 1, "is the same\n")
                ColourPrint = ColourPrint + GREEN + guess[i] + RESET
                temp = temp + guess[i]
                tanswer = tanswer[:i] + " " + tanswer[i + 1:]
                tguess = tguess[:i] + " " + tguess[i + 1:]
                #print(GREEN + guess[i] + RESET )
                #print("position ", i +1 , " is green\n")
            elif tguess[i] not in tanswer and tguess[i] != tanswer[i]:
                #print("Position", i + 1, "is not the same\n")
                ColourPrint = ColourPrint + RED + guess[i] + RESET
                temp = temp + guess[i]
                tanswer = tanswer[:i] + " " + tanswer[i + 1:]
                tguess = tguess[:i] + " " + tguess[i + 1:]
                #print("position ", i +1 , " is red\n")
                if guess[i] not in wrong:
                        wrong = wrong + guess[i] +","
                #wrong = wrong + [guess[i]] 
            else:
                    ColourPrint = ColourPrint + YELLOW + guess[i] + RESET
                    #tanswer = tanswer[:i] + " " + tanswer[i + 1:] 
                    tguess = tguess[:i] + " " + tguess[i + 1:]"""
   
        counter = counter + 1
        tanswer = answer
        tguess = guess
        if counter == 5:
            break

        print("-------------------------------------------------------------\n")                
        """for j in range (4):
            if guess[j] in answer:
                print(guess[j]+" is in word\n")
            else:
                print(guess[j]+" is not in word\n")
        print("-------------------------------------------------------------\n")"""              
        """for k in range (4):
                for l in range (4):
                    if guess[k] == answer[l] and guess[k] != answer[k] and guess[k] != ColourPrint:
                            print(guess[k] +" is in postion "+ str(l+1)+ "\n")
                            print(guess[k] + " is yellow")
                            ColourPrint = ColourPrint + YELLOW + guess[k] + RESET"""
       
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


print(answer)
                    #str(myList[x]).find(guess[i:i+1])
                    #print(guess[i:i+1], "is in the word")


    #print("win!! yay!!!")