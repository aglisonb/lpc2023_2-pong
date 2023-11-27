import pygame
import sys
import random

# definindo medidas
width = 1024
height = 700
mid = (width / 2) - ((40 + 50) / 2)

# tamanho da tela
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# desenhando os objetos
player = pygame.Rect(width - 20, height / 2 - 100, 10, 140)
bot = pygame.Rect(10, height / 2 - 100, 10, 180)
ball = pygame.Rect(width / 2 - 15, height / 2 - 15, 30, 30)

ballx = 0
bally = 0
p_speed = 0
o_speed = 10
a = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), bot)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (255, 255, 255), (width / 2, 0), (width / 2, height))
    pygame.display.flip()
    clock.tick(75)
