# Example file showing a basic pygame "game loop"
from asyncio import events
from faulthandler import cancel_dump_traceback_later
from random import random, randrange
from re import T
from tkinter import Button
from tracemalloc import stop
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))
a = pygame.image.load("padoru.png")
b = pygame.image.load("photo.jpg")
c = pygame.image.load("good.jpeg")
img_track = pygame.image.load("track.png")
a = pygame.transform.scale(a,(100,100))
a_rect = a.get_rect()
a_rect.x = 50
a_rect.y = 300
b = pygame.transform.scale(b,(100,100))
b_rect = b.get_rect()
b_rect.x = 1300
b_rect.y = 300
c = pygame.transform.scale(c,(150,150))
c_rect = c.get_rect()
c_rect.x = 2000
c_rect.y = 500
speed=10
is_jumping = False
jump = 28
nowjump =jump
g = 1.5
score =0
font = pygame.font.Font(None,36)
clock = pygame.time.Clock()
running = True
gameover =False
highscore=0
random
speedlist = [5,6,7,8,9]

level=0
while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               a_rect.y = 300
            if event.key ==  pygame.K_SPACE:
               is_jumping = True
            if event.key ==pygame.K_r:
               score=0
               b_rect.x = 1500
               c_rect.x = 2300
               gameover =False
               running = True
    if  gameover==False:
        score +=14
        if is_jumping:
            a_rect.y -= nowjump
            nowjump -= g 
            
        if gameover == True:
            speed=0
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_jumping =True
        if a_rect.y > 300:
               a_rect.y = 300
               nowjump = jump
               is_jumping = False
        
        c_rect.x -= speed
        b_rect.x -= speed
        if b_rect.x < -50:
            b_rect.x = 1300
        if c_rect.x < -50:
            c_rect.x = 1500


        if a_rect.colliderect(b_rect):
            if score>highscore:
                highscore =score
            gameover = True
        if a_rect.colliderect(c_rect):
            if score>highscore:
                highscore =score
            gameover = True
        if score >3000:
            speed = speedlist[3]
            level = 3
        elif score >2000:
            speed = speedlist[2]
            level =2
        elif score>1000:
            speed = speedlist[1]
            level = 1
            
        
    


    




            

            

    
                
           
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    score_show=font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(score_show,(10,10))
    screen.blit(a,a_rect)
    screen.blit(b,b_rect)
    highscore_show=font.render(f"HIGH Score:{highscore}",True,(0,0,0))
    screen.blit(highscore_show,(250,10))
    level_show = font.render(f"Level: {level}",True, (0,0,0))
    screen.blit(level_show,(10,50))
    screen.fill((255,255,255))
    screen.blit(img_track,(0,370))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()