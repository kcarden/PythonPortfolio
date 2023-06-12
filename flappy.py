import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 400
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Flappy Triangle")

# Set up colors
white = (255, 255, 255)

# Set up the player triangle
player_width = 50
player_height = 50
player_x = window_width // 2 - player_width // 2
player_y = window_height // 2 - player_height // 2
player_velocity = 0
gravity = 0.5

# Set up the game clock
clock = pygame.time.Clock()

# Load the font
font = pygame.font.Font(None, 36)

# Set up the game variables
score = 0
game_over = False
game_started = False

# Set up the pipes
pipe_width = 70
pipe_gap = 200
pipe_speed = 3
top_pipe = pygame.Rect(0, 0, pipe_width, 0)
bottom_pipe = pygame.Rect(0, 0, pipe_width, 0)

def draw_player():
    pygame.draw.polygon(window, white, [(player_x, player_y), (player_x + player_width, player_y + player_height // 2), (player_x, player_y + player_height)], 0)

def draw_pipes():
    pygame.draw.rect(window, white, top_pipe)
    pygame.draw.rect(window, white, bottom_pipe)

def display_score():
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, (10, 10))

def check_collision():
    if player_y < 0 or player_y + player_height > window_height:
        return True
    if top_pipe.colliderect(player_rect) or bottom_pipe.colliderect(player_rect):
        return True
    return False

def generate_pipes():
    pipe_height = random.randint(100, window_height - pipe_gap - 100)
    top_pipe_rect = pygame.Rect(window_width, 0, pipe_width, pipe_height)
    bottom_pipe_rect = pygame.Rect(window_width, pipe_height + pipe_gap, pipe_width, window_height - pipe_height - pipe_gap)
    return top_pipe_rect, bottom_pipe_rect

def restart_game():
    global player_y, player_velocity, score, game_over, top_pipe, bottom_pipe
    player_y = window_height // 2 - player_height // 2
    player_velocity = 0
    score = 0
    game_over = False
    top_pipe, bottom_pipe = generate_pipes()

# Wait for the player to press the space key to start the game
while not game_started:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True

    # Clear the screen
    window.fill((0, 0, 0))

    # Display the prompt
    prompt_text = font.render("Press Space to Start", True, white)
    window.blit(prompt_text, (window_width // 2 - 140, window_height // 2))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(30)

# Game loop
while True:
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player_velocity = -10

        # Update player position
        player_y += player_velocity
        player_velocity += gravity

        # Update pipe position
        top_pipe.x -= pipe_speed
        bottom_pipe.x -= pipe_speed

        # Check collision
        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        if check_collision():
            game_over = True

        # Check if the pipe has passed the player
        if top_pipe.x + pipe_width < player_x:
            score += 1
            top_pipe, bottom_pipe = generate_pipes()

        # Clear the screen
        window.fill((0, 0, 0))

        # Draw player, pipes, and score
        draw_player()
        draw_pipes()
        display_score()

        # Update the display
        pygame.display.update()

        # Limit the frame rate
        clock.tick(30)

    # Game over
    restart_text = font.render("Press R to Restart", True, white)
    window.blit(restart_text, (window_width // 2 - 100, window_height // 2))
    pygame.display.update()

    # Wait for restart or quit
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()
                    game_over = False
                    game_started = False
                    # Wait for the player to press the space key to start the game
                    while not game_started:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                            elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE:
                                    game_started = True
                                    
