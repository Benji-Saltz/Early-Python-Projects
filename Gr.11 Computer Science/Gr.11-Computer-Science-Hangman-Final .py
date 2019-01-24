'''
By: Benji Saltz
Date: 13/10/16
Description: Welcome to hangman! It requires two players. One enters and word and a hint, while the other gets the opportunity to guess the word letter by letter
includes ascii art for lives and creates a hanging man (and a bit of a story as well).
'''
lives=7 #displays how many tries you could get wrong before you lose the game
usedletters='' #counts used letters
print("welcome to HANGMAN")
while True:
    try:
        secretword=input("Enter a WORD for your opponent to guess. USE ONLY LETTERS: ").upper() #allows player to enter a secret word
        category=input(str("Put a category which corrisponds to your word: ")) #allows player to enter a category to help the other player
        string=('_'*len(secretword))#allows word to go away and store number of letters in the word as a string
        if secretword.isalpha():# only allows game to start if the secret word is only letters
            break
    except:
        print("Use letters only, I SWEAR IF I SEE A SEVEN") #What is displayed if word is not letters
print('\n'*100)#makes game start down the page so the first player doesn't see the word
print("Welcome to hangman! Guess a letter or the whole word!")
print("The category is:",category) #displays category
while True:#allows game to be played as long as lives are not depleted
    if lives>0:#Game works until lives are zero
        string=('_'*len(secretword))#displays word as underscores 
        for i in range(0,len(usedletters)):#allows letters to be saved
            for j in range(0,len(secretword)):#allows used letters to corrispond to the word
                if secretword[j] == usedletters[i]:#used to allow used letters to show where the letters are in word
                    correctletter = list(string)#letter shows up where it corrisponds in word
                    correctletter[j] = usedletters[i]#letter is proved to be a corrct letter in word
                    string = ''.join(correctletter)#replaces underscore with corrisponding letter

        for i in range(0,len(string)):#tracks string
            print(string[i]+' ',end='')#allows letters to appear
        print('')
        if '_' not in string:#if letters are not correct
            break
        print("You have",lives,"attempt(s) to guess the word")#displays lives
        print("guessed letters: ",usedletters)#displays used letters
        if lives==7:#These are drawings which corrispond to how many lives you have, drawing a hangman
            print("_______")
            print(" |/    |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif lives==6:
            print("_______")
            print(" |/    |")
            print(" |    (_)")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif lives==5:
            print("_______")
            print(" |/    |")
            print(" |    (_)")
            print(" |    \|/")
            print(" |")
            print(" |")
            print(" |")
            print("_|___")
        elif lives==4:
            print("_______")
            print(" |/    |")
            print(" |    (_)")
            print(" |    \|/")
            print(" |     |")
            print(" |")
            print(" |")
            print("_|___")
        elif lives==3:
            print("_______")
            print(" |/    |")
            print(" |    (_)")
            print(" |    \|/")
            print(" |     |")
            print(" |    / \\")
            print(" |")
            print("_|___")
        elif lives==2:
            print("_______")
            print(" |/    | Please don't hang me, I have a family")
            print(" |    (_)")
            print(" |    \|/")
            print(" |     |")
            print(" |    / \\")
            print(" |")
            print("_|___")
        elif lives==1:
            print("    _______")
            print("     |/    | Please don't hang me, I have a family")
            print("     |    (_)")
            print("     |    \|/")
            print(" (_) |     |")
            print(" \|/ |    / \\")
            print("  |  |")
            print(" / \_|___") 
        while True:
            try:
                guessedletters=input("guess a letter: ").upper() #allows you to guess letters
                if len(guessedletters)>1 or guessedletters.isdigit():#allows only one letter to be given 
                    print("I SAID GUESS A LETTER")
                elif guessedletters in usedletters:#stops user to enter an already guessed letter
                    print("YOU HAVE ALREADY ENTERED THIS LETTER ALREADY")
                    lives==lives
                else:
                    
                    break
            except:
                print("letters only")
        usedletters+=guessedletters
        if guessedletters not in secretword:#If letters are not in the secret word, lives go down by one
            lives-=1
    else: #When lives equal zero you lose
        print("GAME OVER YOUR'E BAD!!!!!!!!"*110)
        print("\nThe word was: ",secretword)
        print("\nYou're hated by the whole community")
        break

if lives>0 or guessedletters==secretword:#If you guess the word, I will display you won
    print("Game over, you won"*110)
    
                
            
        
