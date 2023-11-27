import pygame
import sys
import random


def player_animation():
    player.y += p_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height


# definindo medidas e os textos
width = 1024
height = 700
mid = (width / 2) - ((40 + 50) / 2)
p_score = 0
b_score = 0
pygame.init()
game_font = pygame.font.Font("font.ttf", 100)

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
b_speed = 10
a = 10

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                p_speed += a

            if event.key == pygame.K_UP:
                p_speed -= a
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                p_speed -= a
            if event.key == pygame.K_UP:
                p_speed += a

    player_animation()

    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), bot)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (255, 255, 255), (width / 2, 0), (width / 2, height))
    player_text = game_font.render(f"{p_score}", False, (255, 255, 255))
    screen.blit(player_text, (740, 50))
    bot_text = game_font.render(f"{p_score}", False, (255, 255, 255))
    screen.blit(bot_text, (270, 50))
    pygame.display.flip()
    clock.tick(75)
