import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define snake and food properties
snake_block_size = 20
snake_speed = 15
snake_x = window_width // 2
snake_y = window_height // 2
snake_x_change = 0
snake_y_change = 0
snake_body = []
snake_length = 1
food_x = round(random.randrange(0, window_width - snake_block_size) / snake_block_size) * snake_block_size
food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size

clock = pygame.time.Clock()

# Define functions
def draw_snake(snake_body):
    for part in snake_body:
        pygame.draw.rect(window, GREEN, [part[0], part[1], snake_block_size, snake_block_size])

def draw_food(food_x, food_y):
    pygame.draw.rect(window, RED, [food_x, food_y, snake_block_size, snake_block_size])

def game_loop():
    game_over = False
    game_exit = False
    global snake_x, snake_y, snake_x_change, snake_y_change, snake_body, snake_length, food_x, food_y

    while not game_exit:
        while game_over:
            # Display game over message and options
            window.fill(WHITE)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("Game Over! Press Q-Quit or C-Play Again", True, BLACK)
            window.blit(message, [window_width / 6, window_height / 3])
            pygame.display.update()

            # Check for user input after game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = snake_block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -snake_block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = snake_block_size
                    snake_x_change = 0

        # Check for boundaries or self-collision
        if (
            snake_x >= window_width
            or snake_x < 0
            or snake_y >= window_height
            or snake_y < 0
            or [snake_x, snake_y] in snake_body[1:]
        ):
            game_over = True

        snake_x += snake_x_change
        snake_y += snake_y_change
        window.fill(WHITE)

        # Check if snake has eaten the food
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width -
                                                        snake_block_size) / snake_block_size) * snake_block_size
            food_y = round(random.randrange(0, window_height - snake_block_size) / snake_block_size) * snake_block_size
            snake_length += 1

        # Update snake body
        snake_head = [snake_x, snake_y]
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # Draw snake and food
        draw_snake(snake_body)
        draw_food(food_x, food_y)

        pygame.display.update()

        # Check if snake collides with itself
        for part in snake_body[1:]:
            if part == snake_head:
                game_over = True

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game loop
game_loop()






 

  
    
