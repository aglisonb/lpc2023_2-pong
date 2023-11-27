import pygame
import sys
import random


def ball_movement():
    global ballx, bally, b_score, p_score
    ball.x += ballx
    ball.y += bally
    if ball.top <= 0 or ball.bottom >= height:
        bally *= -1
    if ball.right >= width or ball.left <= 0:
        if ball.right >= width:
            b_score += 1
        if ball.left <= 0:
            p_score += 1
        ball_reset()
    if ball.colliderect(player) or ball.colliderect(bot):
        ballx *= -1


def player_animation():
    player.y += p_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= height:
        player.bottom = height


def ball_reset():
    global ballx, bally
    ball.center = (width / 2, height / 2)
    ballx *= 0
    bally *= 0
    bot.center = (10, height / 2)
    player.center = (width - 5, height / 2)


# texts and measures
width = 1024
height = 700
mid = (width / 2) - ((40 + 50) / 2)
p_score = 0
b_score = 0
pygame.init()
game_font = pygame.font.Font("font.ttf", 100)

# size screen
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg = (0, 0, 0)

# draw
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
        if ballx == 0 or bally == 0:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    ballx = 7 * random.choice((1, -1))
                    bally = 7 * random.choice((1, -1))

                if event.key == pygame.K_UP:
                    ballx = 7 * random.choice((1, -1))
                    bally = 7 * random.choice((1, -1))

    player_animation()
    ball_movement()

    if ball.x < width / 2:
        if bot.top <= ball.y:
            bot.top += b_speed
        if bot.bottom >= ball.y:
            bot.bottom -= b_speed

    if bot.top <= 0:
        bot.top = 0
    if bot.bottom >= height:
        bot.bottom = height


    # visible
    screen.fill(bg)
    pygame.draw.rect(screen, (255, 255, 255), player)
    pygame.draw.rect(screen, (255, 255, 255), bot)
    pygame.draw.rect(screen, (255, 255, 255), ball)
    pygame.draw.aaline(screen, (255, 255, 255), (width / 2, 0), (width / 2, height))
    player_text = game_font.render(f"{p_score}", False, (255, 255, 255))
    screen.blit(player_text, (740, 50))
    bot_text = game_font.render(f"{b_score}", False, (255, 255, 255))
    screen.blit(bot_text, (270, 50))
    pygame.display.flip()
    clock.tick(75)