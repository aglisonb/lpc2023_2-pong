import pygame
import sys
import random


def ball_movement():
    global ballx, bally, b_score, p_score
    ball.x += ballx
    ball.y += bally
    if ball.top <= 0 or ball.bottom >= height:
        bally *= -1
        bounce_sound_effect.play()
    if ball.right >= width or ball.left <= 0:
        if ball.right >= width:
            b_score += 1
            scoring_sound_effect.play()
        if ball.left <= 0:
            p_score += 1
            scoring_sound_effect.play()
        ball_reset()
    if ball.colliderect(player) or ball.colliderect(bot):
        ballx *= -1
        bounce_sound_effect.play()


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
    dir = random.choice(direction)
    ang = random.choice(angle)
    if dir == 0:
        if ang == 0:
            bally, ballx = -10, 5
        if ang == 1:
            bally, ballx = -10, 5
        if ang == 2:
            bally, ballx = -10, 10
    if dir == 1:
        if ang == 0:
            bally, ballx = 10, 5
        if ang == 1:
            bally, ballx = 10, 5
        if ang == 2:
            bally, ballx = 10, 10


# texts and measures
width = 1280
height = 720
mid = (width / 2) - ((40 + 50) / 2)
p_score = 0
b_score = 0
pygame.init()
game_font = pygame.font.Font("assets/PressStart2P.ttf", 100)

# angles creatives, top and bottom []
direction = [0, 1]
angle = [0, 1, 2]

# songs
bounce_sound_effect = pygame.mixer.Sound('assets/bounce.wav')
scoring_sound_effect = pygame.mixer.Sound('assets/258020__kodack__arcade-bleep-sound.wav')

# size screen
size = (width, height)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg = (0, 0, 0)

# draw
player = pygame.Rect(width - 20, height / 2 - 100, 10, 180)
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
                    dir = random.choice(direction)
                    ang = random.choice(angle)
                    if dir == 0:
                        if ang == 0:
                            bally, ballx = -6, 8
                        if ang == 1:
                            bally, ballx = -7, 7
                        if ang == 2:
                            bally, ballx = -8, 6
                    if dir == 1:
                        if ang == 0:
                            bally, ballx = 6, 8
                        if ang == 1:
                            bally, ballx = 7, 7
                        if ang == 2:
                            bally, ballx = 8, 6

                if event.key == pygame.K_UP:
                    dir = random.choice(direction)
                    ang = random.choice(angle)
                    if dir == 0:
                        if ang == 0:
                            bally, ballx = -6, 8
                        if ang == 1:
                            bally, ballx = -7, 7
                        if ang == 2:
                            bally, ballx = -8, 6
                    if dir == 1:
                        if ang == 0:
                            bally, ballx = 6, 8
                        if ang == 1:
                            bally, ballx = 7, 7
                        if ang == 2:
                            bally, ballx = 8, 6

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
    screen.blit(player_text, (width/2 + 250, 50))
    bot_text = game_font.render(f"{b_score}", False, (255, 255, 255))
    screen.blit(bot_text, (270, 50))
    pygame.display.flip()
    clock.tick(60)