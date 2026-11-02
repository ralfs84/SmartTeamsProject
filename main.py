from test import myList
import random

x = random.randint(0, len(myList) - 1)
count = 1

answer = myList[x]
print(answer)
guess = input('enter a guess\n')
while guess != answer:# while guess is not just The Answer
    guess = input('enter a guess\n') ## will continue asking until the word provided is in the list of EXISTING words/removes gibberish
    while guess in myList:
    
        for i in range (4):
            if guess[i] == answer[i]:

                print("Position", i + 1, "is the same\n")
            else:
                print("Position", i + 1, "is not the same\n")
                            

                #str(myList[x]).find(guess[i:i+1])
                #print(guess[i:i+1], "is in the word")


#print("win!! yay!!!")