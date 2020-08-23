import random
import pygame
from UpdatedSnakeGame_CLASS import *
# this snake game actually works!
pygame.init()
# snake list
all_snake = 0
all_snake_x = [61]
all_snake_y = [61]
i = 0
j = 0
o = 1
last_element = -1
temp_pos = 0
game_end = False

timer = 0
inc = 40
wn_height = 601
wn_width = 601
wn = pygame.display.set_mode((wn_height, wn_width))
surface = pygame.Surface((wn_height, wn_width))
# colors
font = pygame.font.SysFont(None, 24)
WHITE = [255, 255, 255]
GREY = [200, 200, 200]
BLACK = [0, 0, 0]
RED = [255, 0, 100]
GREEN = [0, 225, 100]
# snake pos
snake_x = 21
snake_y = 21
snake_change = 20
snake = Snake(snake_x, snake_y)
# movement bools
snake_up = False
snake_down = False
snake_right = False
snake_left = False
# snake food
snake_food = SnakeFood(0, 0)
snake_food.PickLocation()


def drawGrid():
    for y in range(0, 40):
        pygame.draw.line(wn, BLACK, (y * 20, 0), (y * 20, wn_height), 1)
        y += 1
    for z in range(0, 40):
        pygame.draw.line(wn, BLACK, (0, z * 20), (wn_width, z * 20), 1)
        z += 1


def player(x, y):
    rect = pygame.Rect(x, y, 19, 19)
    pygame.draw.rect(wn, GREEN, rect)


def snakeFood(x, y):
    rect = pygame.Rect(x, y, 19, 19)
    pygame.draw.rect(wn, RED, rect)


running = True
while running:
    wn.fill(WHITE)
    if game_end:
        wn.fill(RED)
        timer = -100000
    timer += 1
    drawGrid()
    length = len(all_snake_x)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KeyBoard Input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake_up = False
                snake_down = True
                snake_right = False
                snake_left = False
            if event.key == pygame.K_UP:
                snake_up = True
                snake_down = False
                snake_right = False
                snake_left = False
            if event.key == pygame.K_RIGHT:
                snake_up = False
                snake_down = False
                snake_right = True
                snake_left = False
            if event.key == pygame.K_LEFT:
                snake_up = False
                snake_down = False
                snake_right = False
                snake_left = True

    # if the snake hits the wall or other part of itself
    if all_snake_x[0] < 1 or all_snake_x[0] > 581 or all_snake_y[0] < 1 or all_snake_y[0] > 581:
        game_end = True
    if len(all_snake_x) >= 4:
        for o in range(0, len(all_snake_x) - 1):
            if all_snake_y[0] == all_snake_y[o + 1] and all_snake_x[0] == all_snake_x[o + 1]:
                game_end = True
            o += 1

    # slowing down the snake and snake movement
    if timer >= inc:
        if snake_up:
            temp_pos = all_snake_y[0] - snake_change
            temp_pos2 = all_snake_x[0]
            all_snake_y.pop(-1)
            all_snake_x.pop(-1)
            all_snake_y.insert(0, temp_pos)
            all_snake_x.insert(0, temp_pos2)
            timer = 0
        elif snake_down:
            temp_pos = all_snake_y[0] + snake_change
            temp_pos2 = all_snake_x[0]
            all_snake_y.pop(-1)
            all_snake_x.pop(-1)
            all_snake_y.insert(0, temp_pos)
            all_snake_x.insert(0, temp_pos2)
            timer = 0
        elif snake_right:
            temp_pos = all_snake_x[0] + snake_change
            temp_pos2 = all_snake_y[0]
            all_snake_x.pop(-1)
            all_snake_y.pop(-1)
            all_snake_x.insert(0, temp_pos)
            all_snake_y.insert(0, temp_pos2)
            timer = 0
        elif snake_left:
            temp_pos = all_snake_x[0] - snake_change
            temp_pos2 = all_snake_y[0]
            all_snake_x.pop(-1)
            all_snake_y.pop(-1)
            all_snake_x.insert(0, temp_pos)
            all_snake_y.insert(0, temp_pos2)
            timer = 0

    snakeFood(snake_food.getX(), snake_food.getY())

    if snake_food.getX() == all_snake_x[0] and snake_food.getY() == all_snake_y[0]:
        if snake_up:
            all_snake_y.append(all_snake_y[0] + 20)
            all_snake_x.append(all_snake_x[0])
        elif snake_down:
            all_snake_y.append(all_snake_y[0] - 20)
            all_snake_x.append(all_snake_x[0])
        elif snake_right:
            all_snake_x.append(all_snake_x[0] + 20)
            all_snake_y.append(all_snake_y[0])
        elif snake_left:
            all_snake_x.append(all_snake_x[0] - 20)
            all_snake_y.append(all_snake_y[0])
        all_snake += 1
        snake_food.PickLocation()

    # displaying all of the snake
    for i in range(0, length):
        player(all_snake_x[i], all_snake_y[i])
        i += 1
        if i == length - 1:
            i = 0

    img = font.render("Score: " + str(all_snake), True, BLACK)
    wn.blit(img, (520, 10))

    pygame.display.update()
