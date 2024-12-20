# Example file showing a basic pygame "game loop"
from asyncio import events
from faulthandler import cancel_dump_traceback_later
from re import T
from tkinter import Button
from tracemalloc import stop
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 400))
a = pygame.image.load("padoru.png")
b = pygame.image.load("photo.jpg")
a = pygame.transform.scale(a,(100,100))
a_rect = a.get_rect()
a_rect.x = 50
a_rect.y = 300
b = pygame.transform.scale(b,(100,100))
b_rect = b.get_rect()
b_rect.x = 1300
b_rect.y = 300
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

while running:
    score +=14
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_SPACE:
                is_jumping = True
            if event.key ==pygame.K_r:
                score=0
                b_rect.x = 1500
                gameover =False
    if not gameover:
        if is_jumping:
            a_rect.y -= nowjump
            nowjump -= g
        if event.type == pygame.MOUSEBUTTONDOWN:
            is_jumping =True
        if a_rect.y > 300:
               a_rect.y = 300
               nowjump = jump
               is_jumping = False
              
            
        b_rect.x -= speed
        if b_rect.x < -50:
                b_rect.x= 1288
                
        if a_rect.colliderect(b_rect):
            if score>highscore:
                highscore =score
            gameover = True
        if gameover == True:
            speed=0
            score-=14
        
    


    




            

            

    
                
           
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")
    score_show=font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(score_show,(10,10))
    screen.blit(a,a_rect)
    screen.blit(b,b_rect)
    highscore_show=font.render(f"HIGH Score:{highscore}",True,(0,0,0))
    screen.blit(highscore_show,(250,10))

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()