from cgitb import reset
import pygame
from pygame.locals import *
import random

#pygame init
pygame.init()

#Pygame Window Name
pygame.display.set_caption('Bing Bong')

#creating surface with dimension
surface = pygame.display.set_mode(( 1200, 800 ))

#Images in Game
baby_yoda = pygame.image.load('baby-yoda.jpg')

#import font
font = pygame.font.Font('freesansbold.ttf', 30)

#Set Icon
pygame.display.set_icon(baby_yoda)

#clock
clock = pygame.time.Clock()

#Running variable to control while True loop
running = True

#Paddle Y Coordinates
paddlechange_1 = 365
paddlechange_2 = 365

#ping coordinates
pingx = 600
pingxchange = 8
pingy = 400
pingychange = random.uniform(2.0, 5.0)

#score
Babayaga_score = 0
Darthvader_score = 0

#pause bool
Paused = False

#start/reset bool
started = False
Reset = False

#key dictonary
pressed_keys = {"Paddle1Up": False, "Paddle1Down": False, "Paddle2Up": False, "Paddle2Down": False}

while running:
    #background colour
    surface.fill((70, 130, 180))

    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN: #Checking what key is pressed, and changing dictionary values based on it
            if event.key == pygame.K_w:
                pressed_keys["Paddle1Up"] = True
                
            if event.key == pygame.K_s:
                pressed_keys["Paddle1Down"] = True

            if event.key == pygame.K_p:
                pressed_keys["Paddle2Up"] = True
                
            if event.key == pygame.K_l:
                pressed_keys["Paddle2Down"] = True
            
            if event.key == pygame.K_SPACE:
                if not Paused:
                    Paused = True

                else:
                    Paused = False

        elif event.type == pygame.KEYUP: #Checking what key is released, and changing dictionary values based on it
            if event.key == pygame.K_w:
                pressed_keys["Paddle1Up"] = False
            
            if event.key == pygame.K_s:
                pressed_keys["Paddle1Down"] = False

            if event.key == pygame.K_p:
                pressed_keys["Paddle2Up"] = False
            
            if event.key == pygame.K_l:
                pressed_keys["Paddle2Down"] = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if 500.0 <= mouse[0] <= 700.0 and 600.0 <= mouse[1] <= 660.0:
                if not started:
                    started = True
                    clock.tick(1)

                elif Paused:
                    Paused = False
                    Reset = True

        elif event.type == QUIT: #If Press Quit, Then Shut Down Window
            running = False

    mouse = pygame.mouse.get_pos()

    if 30 <= pingx <= 35 and paddlechange_1 - 10 <= pingy <= paddlechange_1 + 80 or 1165 <= pingx <= 1170 and paddlechange_2 - 10 <= pingy <= paddlechange_2 + 80:
        pingxchange *= -1

    if pingy <= 18 + pingychange or pingy >= 782 + pingychange:
        pingychange *= -1

    if not Paused and started:
        pingx -= pingxchange
        pingy -= pingychange

        #movement
        if pressed_keys["Paddle1Up"]:
            if paddlechange_1 >= 15:
                paddlechange_1 -= 15

        if pressed_keys["Paddle1Down"]:
            if paddlechange_1 <= 715:
                paddlechange_1 += 15

        if pressed_keys["Paddle2Up"]:
            if paddlechange_2 >= 15:
                paddlechange_2 -= 15

        if pressed_keys["Paddle2Down"]:
            if paddlechange_2 <= 715:
                paddlechange_2 += 15

    if Paused:
        surface.blit(font.render("Game Paused", True , (0, 0, 0)), (500, 400))
        pygame.draw.rect(surface, ((254, 219, 121)), [500, 600, 200, 60], 0)
        surface.blit(font.render("Reset", True, (0, 0, 0)), (560, 615))

    if Reset:
        started = False
        Reset = False
        pingx, pingy = 600, 400
        paddlechange_1, paddlechange_2 = 365, 365
        Babayaga_score, Darthvader_score = 0,0

    #ping pong ball
    pygame.draw.circle(surface, ((0,0,0)), (( pingx, pingy)), 18.0, 0)

    #paddles
    pygame.draw.rect(surface, ((53,94,59)), [0, paddlechange_1, 15, 70], 0)
    pygame.draw.rect(surface, ((53,94,59)), [1185, paddlechange_2, 15, 70], 0)

    #Score
    if pingx < 15:
        Darthvader_score += 1
        pingx = 600
        pingy = 400
        pingychange = random.uniform(2.0, 5.0)
        clock.tick(1)
    if pingx > 1185:
        Babayaga_score += 1
        pingx = 600
        pingy = 400
        pingychange = random.uniform(2.0, 5.0)
        clock.tick(1)
        
    surface.blit(font.render("Baba Yaga: " + str(Babayaga_score), True , (0, 0, 0)), (100, 10))
    surface.blit(font.render("Darth Vader: " + str(Darthvader_score), True, (0, 0, 0)), (900, 10))

    if not started:
        #Start/Reset button
        pygame.draw.rect(surface, ((254, 219, 121)), [500, 600, 200, 60], 0)
        surface.blit(font.render("Start", True, (0, 0, 0)), (560, 615))

    #update
    pygame.display.update()

    #tick
    clock.tick(60)

pygame.quit()