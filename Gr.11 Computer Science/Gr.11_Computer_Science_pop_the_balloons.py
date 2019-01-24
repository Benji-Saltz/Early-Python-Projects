#########################################
# Programmer: Mrs. G
# Date: 20/03/2014
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
#########################################
import time #allows timer to function
import random #allows reandom variables to be used
import pygame #allows use of pygame
import os #allows image to be used
os.environ['SDL_VIDEODRIVER'] = 'windib' #allows image to be used


pygame.init()

from math import sqrt                   # only sqrt function is needed from the math module
from random import randint              # only randint function is needed from the random module

HEIGHT = 600 #height of screen
WIDTH  = 800#width of screen
game_window=pygame.display.set_mode((WIDTH,HEIGHT))#Sets size of screen

WHITE = (255,255,255)                   #
BLACK = (  0,  0,  0)                   # used colours
outline=0                               # thickness of the shapes' outline
count_score=0 #variable to keep score 
RED = [] #a list to store random hue of red
GREEN = []#a list to store random hue of green
BLUE = []#a list to store random hue of blue
Background = pygame.image.load("Background.png")#background image
Background = Background.convert_alpha()     # converts the image pixel format for faster blitting
backgroundX=0#sets background
backgroundY=0
Background=pygame.transform.scale(Background,(800,600))                                        # alpha preserves the transparency (if the background is transparent)
balloon_Visible=[]#variable for balloon being visible
font = pygame.font.SysFont("Arial Black",30) # create a variable font
font2 = pygame.font.SysFont("Arial Black",100) # create a variable font
message = "Balloons Popped: " #messages to be displayed on the screen
message3= "Time: "
Start_message="GET READY"
End_message="It took you: "
End_message1="seconds to pop 100 balloons."
End_message3="GAME OVER"
loss=0
min_speed=3
max_speed=10
#---------------------------------------#
# function that calculates distance     #
# between two points in coordinate system
#---------------------------------------#
def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)# Pythagorean theorem    

#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    message2=int(time.clock())
    if message2==20:
        min_speed=5
        max_speed=15
    elif message2==40:
        min_speed=5
        max_speed=15
    elif message2==60:
        min_speed=10
        max_speed=20
    print("Time: ",message2)
    message1 = count_score
    game_window.fill(BLACK)
    game_window.blit(Background, (backgroundX,backgroundY))
    #pygame.display.update()
    #pygame.time.delay(600)
    for i in range(200):
        pygame.draw.circle(game_window, (RED[i],BLUE[i],GREEN[i]), (balloonX[i], balloonY[i]), balloonR[i], outline)
    if message2<=5:
        text8 = font2.render(Start_message, 1,(255,255,255)) # put the font and the message together
        game_window.blit(text8,(75,300))# draw it on the screen at the text_X and text_Y
    if count_score<100:
        text = font.render(message, 1,(255,255,255)) # put the font and the message together
        game_window.blit(text,(420,20))# draw it on the screen at the text_X and text_Y
        text1 = font.render(str(message1), 1,(255,255,255)) # put the font and the message together
        game_window.blit(text1,(700,20))# draw it on the screen at the text_X and text_Y
        text2 = font.render(message3, 1,(255,255,255)) # put the font and the message together
        game_window.blit(text2,(500,60))# draw it on the screen at the text_X and text_Y
        text3 = font.render(str(message2), 1,(255,255,255)) # put the font and the message together
        game_window.blit(text3,(600,60))# draw it on the screen at the text_X and text_Y

    if count_score==100:
        game_window.blit(Background, (backgroundX,backgroundY))
        text4 = font.render(End_message, 1,(random.randint(0,255),random.randint(0,255),random.randint(0,255))) # put the font and the message together
        game_window.blit(text4,(70,200))# draw it on the screen at the text_X and text_Y
        text5 = font.render(str(message2), 1,(random.randint(0,255),random.randint(0,255),random.randint(0,255))) # put the font and the message together
        game_window.blit(text5,(260,200))# draw it on the screen at the text_X and text_Y
        text6 = font.render(End_message1, 1,(random.randint(0,255),random.randint(0,255),random.randint(0,255))) # put the font and the message together
        game_window.blit(text6,(300,200))# draw it on the screen at the text_X and text_Y
        text7 = font2.render(End_message3, 1,(random.randint(0,255),random.randint(0,255),random.randint(0,255))) # put the font and the message together
        game_window.blit(text7,(75,50))# draw it on the screen at the text_X and text_Y
    

   
    pygame.display.update()             # display must be updated, in order                                   # to show the drawings
       
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
exit_flag = False                       #
balloon_Visible=[0]*200
balloonR = [0]*200                      # create lists of 20 items each
balloonX = [0]*200                      # for balloons' properties
balloonY = [0]*200                       #
balloonSPEED = [0]*200                #
GREEN=[0]*200
RED=[0]*200
BLUE=[0]*200
redraw_game_window()
for i in range(200):
    
    RED[i] = random.randint(0,255)                                         # that contains its type and size
    BLUE[i] = random.randint(0,255) 
    GREEN[i] = random.randint(0,255)
    balloonX[i] = randint(0, WIDTH)     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(800, 900)
    balloonR[i] = randint(20,50)
    balloonSPEED[i] = randint(min_speed,max_speed)
    balloon_Visible[i]=True
balloonCLR = WHITE
while not exit_flag:                    #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop

# act upon mouse events
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(200):
                    (cursorX,cursorY)=pygame.mouse.get_pos()
                    if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i]:
                        balloon_Visible[i]=False
                        balloonX[i],balloonY[i]=random.randint(0,800),random.randint(700,800)
                        balloon_Visible[i]=True
                        count_score+=1
                        print("The score is: ",count_score)
                                        
# move the balloons
    for i in range(200):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
        if balloonY[i]==0:
            balloonX[i],balloonY[i]=random.randint(0,800),random.randint(700,800)
# update the screen    
    redraw_game_window()
    pygame.time.delay(1)
    if count_score==100:
        pygame.time.delay(1000)
        exit_flag=True
        pygame.quit()    # always quit pygame when done!
    
