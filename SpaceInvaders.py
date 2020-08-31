import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)

background = pygame.image.load("background.png")

score = 0

playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = []
enemyX = []
enemyY = []
enemyX_change=[]
no_of_enemy = 6

for i in range(no_of_enemy):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)

bulletImg = pygame.image.load("bullet.png")
bulletX = playerX
bulletY = 480
bulletY_change = 10
bullet_state = "ready"


def bullet_fire(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))


running = True

while running:

    screen.fill((255, 180, 230))

    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change -= 5
            if event.key == pygame.K_RIGHT:
                playerX_change += 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            playerX_change = 0

    for i in range(no_of_enemy):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyX[i] += enemyX_change[i]
            enemyY[i] += 40
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyX[i] += enemyX_change[i]
            enemyY[i] += 40
        enemy(enemyX[i], enemyY[i], i)

        if math.sqrt((math.pow(bulletX - enemyX[i], 2)) + (math.pow(bulletY - enemyY[i], 2))) <= 27:
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)
            score += 1
            bulletY = 480
            bullet_state = "ready"

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change




    player(playerX, playerY)
    pygame.display.update()
