from ast import Is
import pygame
from asyncio import events
from faulthandler import cancel_dump_traceback_later
from re import T
from tkinter import Button
from tracemalloc import stop


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))
img_dino = pygame.image.load("dino.png")
img_photo= pygame.image.load("photo.jpg")
img_DinoDuck= [pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
img_DinoRun = [pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
img_Bird = [pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]

dino_rect = img_dino.get_rect()
dino_rect.x = 50
dino_rect.y = 300

photo_rect = img_photo.get_rect()
photo_rect.x = 1300
photo_rect.y = 300


speed=20
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
lastime=10
frame=1
is_ducking=False
while running:
    
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                is_jumping = True
            if event.type  == pygame.K_r:
                running = True
                score=0
                photo_rect.x = 1500
                gameover =False
                photo_rect.x -= speed 
                
            if event.type == pygame.K_DOWN:
                dino_rect.y =330
                is_ducking=True
        if event.type == pygame.KEYUP:
            if is_ducking:
                dino_rect.y =300
                is_ducking=False
          
    if not gameover:
        score +=14
        if is_jumping:
            dino_rect.y -= nowjump
            nowjump -= g
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_jumping =True
        if dino_rect.y > 300:
               dino_rect.y = 300
               nowjump = jump
               is_jumping = False
        
        photo_rect.x-=speed    
        photo_rect.x -= speed
        if photo_rect.x < -50:
            photo_rect.x= 2500
        if Bird_rect.x < -50:
            Bird_rect.x= 2000

                
        if dino_rect.colliderect(photo_rect):
            if score>highscore:
                highscore =score
            gameover = True
        if dino_rect.colliderect(Bird_rect):
            if score>highscore:
                highscore =score
            gameover = True
        if gameover == True:
            
            speed=0
            score-=14
        
        nowtime =pygame.time.get_ticks()
        if nowtime - lastime > 300:
            frame =(frame+1)%2
            lastime =nowtime

        if is_ducking: 
            screen.blit(img_DinoDuck,DinoDuck_rect)
        else:
            screen.blit(img_Bird,Bird_rect)
        pygame.display.flip()
          

            

        


    




            

            

    
                
           
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    score_show=font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(score_show,(10,10))
    screen.blit(img_dino,dino_rect)
    screen.blit(img_photo,photo_rect)
    highscore_show=font.render(f"HIGH Score:{highscore}",True,(0,0,0))
    screen.blit(highscore_show,(250,10))
    screen.blit(score_show,(10,10))
    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()