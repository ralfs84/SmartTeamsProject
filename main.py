from Dictionary import myList
import random

x = random.randint(0, len(myList) - 1)
count = 1

answer = myList[x]
answer = answer.lower() #converts to lower case
#wrong = []
wrong = ""

print(answer + ' is the answer')
guess = input('enter a guess\n')
guess = guess.lower() #converts to lower

while guess != answer:# while guess is not just The Answer
    if guess in myList:
        print('Not the word but is in list\n') ## will continue asking until the word provided is in the list of EXISTING words/removes gibberish
        for i in range (4):
            if guess[i] == answer[i]:
                #print("Position", i + 1, "is the same\n")
                print("position ", i +1 , " is green\n")
            elif guess[i] not in answer and guess[i] != answer[i]:
                #print("Position", i + 1, "is not the same\n")
                print("position ", i +1 , " is red\n")
                if guess[i] not in wrong:
                        wrong = wrong + guess[i] +","
                #wrong = wrong + [guess[i]]      
        print("-------------------------------------------------------------\n")                
        """for j in range (4):
            if guess[j] in answer:
                print(guess[j]+" is in word\n")
            else:
                print(guess[j]+" is not in word\n")
        print("-------------------------------------------------------------\n")"""              
        for k in range (4):
                 for l in range (4):
                      if guess[k] == answer[l] and guess[k] != answer[k]:
                            #print(guess[k] +" is in postion "+ str(l+1)+ "\n")
                            print(guess[k] + " is yellow")
        print("-------------------------------------------------------------\n")
        print(wrong)                                           
        guess = input('Enter a new guess\n')         
    elif guess not in myList:
        guess = input('Not a word\nEnter a new guess\n')



                #str(myList[x]).find(guess[i:i+1])
                #print(guess[i:i+1], "is in the word")


#print("win!! yay!!!")