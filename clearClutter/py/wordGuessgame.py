import random
words=['apple','orange','oracle','amazon','microsoft']
guessed_word=random.choice(words)

hint=guessed_word[0]+guessed_word[-1]
store_g_1=[]
try_p=6
a=input("Enter your name : ")
print("Welcome To Word Guess Game : You have six attempts for guessing")

for guess in range(try_p):
    while True:
        letter=input("Guess the letter : ")

        if len(letter)==1:
            break
        else:
            print("OOps ! Please enter single letter.")

    if letter.lower() in guessed_word:
        print("YES")       
        store_g_1.append(letter)
    else: 
        print("NO") 


    if guess==3:
        # print()       
        hint_req=input("Need a hint ?")

        if hint_req.lower().startswith("y"):
            # print()
            print("CLUE : The first letter of word is : "+hint[0]+"  and last letter is : "+hint[1])
        else:
            print("You are confident .")    

# print()            
print("Now let's see what you have guessed so far. You have guessed : ",len(store_g_1),"letters correctly. These letters are : ",store_g_1)

word_guess=input("Now guess the whole word : ")
if word_guess.lower()==guessed_word: 
    print("Congrats , you are correct.")
else:
    print("Sorry, the answer was : ",guessed_word)
# print()    

