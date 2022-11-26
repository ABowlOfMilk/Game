import pygame
from sys import exit

#Stuffs that needs to be here
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,400))
game_active = True

#title,and font
pygame.display.set_caption("Vinny goes to death row")
Text = pygame.font.Font("Fonts/Pixel Millennium.ttf", 25)

#Background
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground = pygame.image.load("graphics/ground.png").convert()

#SCORE
Score_surf = Text.render("My Game", False, (64,64,64))
Score_rect = Score_surf.get_rect(center = (400,50))

#BAD BAD
BadGuy = pygame.image.load("graphics/BAD_BAD.png").convert_alpha()
BadGuy_rect = BadGuy.get_rect(bottomright = (600,300))

#Player
player = pygame.image.load("graphics/Player.png").convert_alpha()
player_rect = player.get_rect(midbottom = (80,300))
player_gravity = 0

#Shit that runs
while True:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            #onMousePress
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >=300:
                    player_gravity = -20

            #onKeyPress
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >=300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                BadGuy_rect.x = 600


    if game_active :
        #Background Stuffs
        screen.blit(sky_surface,(0,0))
        screen.blit(ground,(0,300))

        #score
        pygame.draw.rect(screen,"#c0e8ec",Score_rect)
        pygame.draw.rect(screen,"#c0e8ec",Score_rect,10)
        screen.blit(Score_surf,Score_rect)


        #BadGuy Stuffs
        screen.blit(BadGuy,BadGuy_rect)
        BadGuy_rect.x -=6
        if BadGuy_rect.right <= 0: BadGuy_rect.left = 800

        #Player Stuffs
        player_gravity +=1
        player_rect.y += player_gravity
        if player_rect.bottom >=300: 
            player_rect.bottom = 300
        screen.blit(player,player_rect)

        #collision
        if BadGuy_rect.colliderect(player_rect):
            game_active = False

    #intro/ menu screen
    else:
        screen.fill('Yellow')

    #other things that need to be there for the shit to run good
    pygame.display.update()
    clock.tick(60)
