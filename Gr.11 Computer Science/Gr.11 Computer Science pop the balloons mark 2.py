#########################################
# Programmer: Benji Saltz
# Date: 14/11/2016
# File Name: pop_the_balloons.py
# Description: This program is a template for a game. It demonstrates use of lists.
'''
Details: In this game, you start when the game starts and pop as many bonus balloons as you can at the beggining.
After 5 seconds, the game resumes with limited balloons coming on the screen. Smaller balloons are worth more.
when 100 points are scored, the game stops and tells you how long it took you to pop 100 balloons. comes with a background
as well.
'''
#########################################
import time#allows timer to function
import random#allows reandom variables to be used
import pygame#allows use of pygame
import os#allows image to be used
os.environ['SDL_VIDEODRIVER'] = 'windib'#allows image to be used


pygame.init()

from math import sqrt                   # only sqrt function is needed from the math module
from random import randint              # only randint function is needed from the random module

HEIGHT = 600#height of screen
WIDTH  = 800#width of screen
game_window=pygame.display.set_mode((WIDTH,HEIGHT))#Sets size of screen

WHITE = (255,255,255)                   #
BLACK = (  0,  0,  0)                   # used colours
outline=0                               # thickness of the shapes' outline
count_score=0#variable to keep score 

RED = []#a list to store random hue of red
GREEN = []#a list to store random hue of green
BLUE = []#a list to store random hue of blue
Background = pygame.image.load("Background.png")#background image 
Background = Background.convert_alpha()     # converts the image pixel format for faster blitting
backgroundX=0#sets background
backgroundY=0#sets background
Background=pygame.transform.scale(Background,(800,600)) #makes location of background                                                                            
balloon_Visible=[]#list to set when balloons are visible or not
font = pygame.font.SysFont("Arial Black",30) # create a variable font
font2 = pygame.font.SysFont("Arial Black",100) # create a variable font
#messages that appear on screen
Start_message="GOOOOOOO"
message = "Balloons Popped: "
message3= "Time: "
End_message="It took you: "
End_message1="seconds to pop 100 balloons."
End_message3="GAME OVER"
#starting speed
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
    message2=int(time.clock())#clock function, allows timer
    #changes in speed when points are greater
    if count_score>=20:
        min_speed=5
        max_speed=15
    elif count_score>=40:
        min_speed=10
        max_speed=30
    elif count_score>=60:
        min_speed=15
        max_speed=40
    print("Time: ",message2)#prints time in shell
    message1 = count_score
    game_window.fill(BLACK)
    game_window.blit(Background, (backgroundX,backgroundY))#sets background
    #draws balloons
    for i in range(200):
        pygame.draw.circle(game_window, (RED[i],BLUE[i],GREEN[i]), (balloonX[i], balloonY[i]), balloonR[i], outline)
    #messages which pop up according to points or time
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
    

   
    pygame.display.update()             # display must be updated, in order to show the drawings
       
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
##count_time=pygame.time.get_ticks()
##for i in range(60):
##    seconds=(pygame.time.get_ticks()-count_time)/1000
##    print("Counting time: ",seconds)
exit_flag = False                       #
balloon_Visible=[0]*200
balloonR = [0]*200                      # create lists of 20 items each
balloonX = [0]*200                       # for balloons' properties
balloonY = [0]*200                       #
balloonSPEED = [0]*200                   #
GREEN=[0]*200 #lists for colours to corrispond to balloons
RED=[0]*200
BLUE=[0]*200
redraw_game_window()
for i in range(100):
    RED[i] = random.randint(0,255)   #sets a balloon to a random colour                                      
    BLUE[i] = random.randint(0,255) 
    GREEN[i] = random.randint(0,255)
    balloonX[i] = randint(0, WIDTH)     # initialize the coordinates and the size of the balloons
    balloonY[i] = randint(HEIGHT/2, HEIGHT)
    balloonR[i] = randint(8,50)
    balloonSPEED[i] = randint(min_speed,max_speed)#sets balloon's speeds
    balloon_Visible[i]=True
balloonCLR = WHITE
while not exit_flag:                    #
    for event in pygame.event.get():    # check for any events
        if event.type == pygame.QUIT:   # If user clicked close
            exit_flag = True            # Flag that we are done so we exit this loop

# act upon mouse events, allows when any part of the mouse is held down to make balloons disappear when the mouse is over them
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(200):
                (cursorX,cursorY)=pygame.mouse.get_pos()
                if distance(cursorX, cursorY, balloonX[i], balloonY[i])< balloonR[i]:
                    balloon_Visible[i]=False
                    balloonX[i],balloonY[i]=random.randint(0,800),random.randint(700,1200)
                    balloon_Visible[i]=True
                    if balloonR[i]<=20:#When a balloon is popped with a small radius, it is worth more
                        count_score+=3
                    else:
                        count_score+=1
                    print("The score is: ",count_score)
# move the balloons
    for i in range(200):
        balloonY[i] = balloonY[i] - balloonSPEED[i]
#Allows balloons to respawn as they hit the top
        if balloonY[i]==0:
            balloonX[i],balloonY[i]=random.randint(0,800),random.randint(700,1200)
            
    redraw_game_window()#redraws game window after an event happens
    pygame.time.delay(30)#sets game speed
    if count_score==100: #When 100 balloons are popped, the game stops, displays how fast you popped 100 balloons then exits
        pygame.time.delay(1000)
        exit_flag=True
        pygame.quit()    # always quit pygame when done!
    
