import pygame
pygame.init()

WIDTH=600
HEIGHT=600
rocket_x=0
rocket_y=0
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Rocket Game")

rocket=pygame.image.load("rocket.png")
Bg=pygame.image.load("background.png")

while rocket_y<600:
    screen.blit(Bg,(0,0))
    screen.blit(rocket,(0,0))