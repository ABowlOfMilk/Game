import pygame
from sys import exit

#Stuffs that needs to be here
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,400))

#title,and font
pygame.display.set_caption("Vinny goes to death row")
Text = pygame.font.Font("Fonts/Pixel Millennium.ttf", 25)

#Background
sky_surface = pygame.image.load("graphics/Sky.png").convert()
ground = pygame.image.load("graphics/ground.png").convert()
Surface_Text = Text.render("My Game is Trash", False, "Black")

#BAD BAD
BadGuy = pygame.image.load("graphics/BAD_BAD.png").convert_alpha()
BadGuy_centerX = 600

#Player
player = pygame.image.load("graphics/Player.png").convert_alpha()
player_rect = player.get_rect(midbottom = (80,300))

#Shit that runs
while True:
    for  event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    #Background Stuffs
    screen.blit(sky_surface,(0,0))
    screen.blit(ground,(0,300))
    screen.blit(Surface_Text,(250,50))
    
    #BadGuy Stuffs
    screen.blit(BadGuy,(BadGuy_centerX,225))
    BadGuy_centerX -= 4
    if BadGuy_centerX < -100: BadGuy_centerX = 800
    
    #Player Stuffs
    screen.blit(player,player_rect)

    #other things that need to be there for the shit to run good
    pygame.display.update()
    clock.tick(60)