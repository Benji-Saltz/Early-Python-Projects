lives=7
save=(str(input("Player 1 input a word")))
length=len(save)
start=save.replace(save,"_")
print("Hello player 2 input letters which will reveal the word \n you have 7 attempts: ") 
print(start*length)
while True:
    
    letters=(str(input("enter a letter:")))
    if letters == save:
        print(save,"You guessed it!")
    elif letters!=save:
        print(start*length)
        lives-=1
    elif lives==0:
        print("You lose!")
    





