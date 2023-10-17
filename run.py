import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 400
GRID_SIZE, GRID_COUNT = 20, SCREEN_WIDTH // 20
SNAKE_SPEED = 10  # Increase for faster speed
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Python Snake Game")

# Initialize clock for controlling the game loop speed
clock = pygame.time.Clock()

# Initialize the snake
snake = [(GRID_COUNT // 2, GRID_COUNT // 2)]
snake_direction = (0, 1)
snake_growing = False

# Initialize the food
food = (random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1))

def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

def move_snake():
    global snake_direction, snake_growing, food

    head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, head)

    if head == food:
        snake_growing = True
        food = (random.randint(0, GRID_COUNT - 1), random.randint(0, GRID_COUNT - 1))
    else:
        if not snake_growing:
            snake.pop()

def draw_snake():
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def draw_food():
    pygame.draw.rect(screen, RED, (food[0] * GRID_SIZE, food[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE))

def check_collision():
    if snake[0][0] < 0 or snake[0][0] >= GRID_COUNT or snake[0][1] < 0 or snake[0][1] >= GRID_COUNT:
        return True
    for segment in snake[1:]:
        if snake[0] == segment:
            return True
    return False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != (0, 1):
                snake_direction = (0, -1)
            elif event.key == pygame.K_DOWN and snake_direction != (0, -1):
                snake_direction = (0, 1)
            elif event.key == pygame.K_LEFT and snake_direction != (1, 0):
                snake_direction = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_direction != (-1, 0):
                snake_direction = (1, 0)

    move_snake()
    if check_collision():
        running = False

    screen.fill((0, 0, 0))
    draw_grid()
    draw_snake()
    draw_food()
    pygame.display.flip()
    clock.tick(SNAKE_SPEED)

# Quit Pygame
pygame.quit()
