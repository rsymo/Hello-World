import pygame
import sys
import random
import time
import logging

# Set up the logger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# Initialize pygame
pygame.init()

# Set up the window
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake')

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
BLUE = (50, 50, 255)

# Set up the snake
SNAKE_WIDTH = 20
SNAKE_HEIGHT = 20
SNAKE_SPEED = 20
snake_position_x = 400
snake_position_y = 300
snake_x_change = 0
snake_y_change = 0
snake_list = []
snake_length = 1

# Set up the food
food_x = random.randint(0, WINDOW_WIDTH - SNAKE_WIDTH)
food_y = random.randint(0, WINDOW_HEIGHT - SNAKE_HEIGHT)
FOOD_WIDTH = 20
FOOD_HEIGHT = 20

# Set up the score
score = 0
font = pygame.font.SysFont(None, 30)

# Set up the clock
clock = pygame.time.Clock()

# Set up the game over screen
def game_over_screen():
    """
    Displays the game over screen and exits the game after a two-second delay.
    """
    logger.debug('Setting up game over screen')
    window.fill(BLACK)
    game_over_text = font.render('Game Over', True, WHITE)
    game_over_text_rect = game_over_text.get_rect()
    game_over_text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    window.blit(game_over_text, game_over_text_rect)
    pygame.display.update()
    time.sleep(2)
    logger.debug('Exiting game')
    pygame.display.quit()
    pygame.quit()
    sys.exit()

# Handle events
def handle_events():
    """
    Handles events such as key presses and window close events.
    """
    global snake_x_change, snake_y_change
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                logger.debug("Left key pressed")
                snake_x_change = -SNAKE_SPEED
                snake_y_change = 0
            if event.key == pygame.K_RIGHT:
                logger.debug("Right key pressed")
                snake_x_change = SNAKE_SPEED
                snake_y_change = 0
            if event.key == pygame.K_UP:
                logger.debug("Up key pressed")
                snake_y_change = -SNAKE_SPEED
                snake_x_change = 0
            if event.key == pygame.K_DOWN:
                logger.debug("Down key pressed")
                snake_y_change = SNAKE_SPEED
                snake_x_change = 0

# Check for collisions
def check_collisions():
    """
    Checks for collisions with the food, walls, and snake.
    """
    global snake_length, score, food_x, food_y
    if snake_position_x == food_x and snake_position_y == food_y:
        logger.debug('Snake ate food')
        food_x = random.randint(0, WINDOW_WIDTH - SNAKE_WIDTH)
        food_y = random.randint(0, WINDOW_HEIGHT - SNAKE_HEIGHT)
        snake_length += 1
        score += 1

    if snake_position_x >= WINDOW_WIDTH or snake_position_x < 0 or snake_position_y >= WINDOW_HEIGHT or snake_position_y < 0:
        logger.debug('Snake hit wall')
        game_over_screen()

    snake_head = []
    snake_head.append(snake_position_x)
    snake_head.append(snake_position_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]
    for snake_segment in snake_list[:-1]:
        if snake_segment == snake_head:
            logger.debug('Snake hit itself')
            game_over_screen()

# Update the snake position
def update_snake_position():
    """
    Updates the snake's position based on its current direction and speed.
    """
    global snake_position_x, snake_position_y
    snake_position_x += snake_x_change
    snake_position_y += snake_y_change
    logger.debug(f'Snake position: {snake_position_x}, {snake_position_y}')

# Draw the game objects
def draw_game_objects():
    """
    Draws the background, snake, food, and score.
    """
    window.fill(BLACK)
    for snake_segment in snake_list:
        pygame.draw.rect(window, GREEN, [snake_segment[0], snake_segment[1], SNAKE_WIDTH, SNAKE_HEIGHT])
    pygame.draw.rect(window, RED, [food_x, food_y, FOOD_WIDTH, FOOD_HEIGHT])
    score_text = font.render(f'Score: {score}', True, WHITE)
    window.blit(score_text, (0, 0))
    pygame.display.update()

# Set up the game loop
while True:
    handle_events()
    check_collisions()
    update_snake_position()
    draw_game_objects()
    clock.tick(10)

