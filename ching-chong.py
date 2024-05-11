import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong Game")

# Set up the game objects
BALL_RADIUS = 10
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([-5, 5]), random.choice([-5, 5])]
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
LEFT_PADDLE_POS = [0, HEIGHT // 2 - PADDLE_HEIGHT // 2]
RIGHT_PADDLE_POS = [WIDTH - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2]
paddle_speed = 5
bot_speed = 5

# Set up scores
left_score = 0
right_score = 0
FONT = pygame.font.Font(None, 36)

# Function to draw paddles
def draw_paddle(pos, color):
    pygame.draw.rect(screen, color, (pos[0], pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))

# Function to draw the ball
def draw_ball(pos):
    pygame.draw.circle(screen, WHITE, pos, BALL_RADIUS)

# Function to display scores
def display_scores():
    left_text = FONT.render("Left Player: " + str(left_score), True, WHITE)
    right_text = FONT.render("Right Player: " + str(right_score), True, WHITE)
    screen.blit(left_text, (20, 20))
    screen.blit(right_text, (WIDTH - right_text.get_width() - 20, 20))

# Function for bot movement
def move_bot():
    if ball_pos[1] < RIGHT_PADDLE_POS[1] + PADDLE_HEIGHT // 2:
        RIGHT_PADDLE_POS[1] -= bot_speed
    elif ball_pos[1] > RIGHT_PADDLE_POS[1] + PADDLE_HEIGHT // 2:
        RIGHT_PADDLE_POS[1] += bot_speed

# Function to display menu
def display_menu():
    play_with_player_button = pygame.Rect(200, 200, 400, 50)
    play_with_bot_button = pygame.Rect(200, 300, 400, 50)
    exit_button = pygame.Rect(200, 400, 400, 50)

    pygame.draw.rect(screen, WHITE, play_with_player_button)
    pygame.draw.rect(screen, WHITE, play_with_bot_button)
    pygame.draw.rect(screen, WHITE, exit_button)

    player_text = FONT.render("Play with Player", True, BLACK)
    bot_text = FONT.render("Play with Bot", True, BLACK)
    exit_text = FONT.render("Exit", True, BLACK)
    game_title = FONT.render("Ping Pong Game", True, WHITE)

    screen.blit(game_title, (200, 100))
    screen.blit(player_text, (300, 210))
    screen.blit(bot_text, (320, 310))
    screen.blit(exit_text, (370, 410))

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if play_with_player_button.collidepoint(mouse_pos):
        if mouse_click[0] == 1:
            return False
    elif play_with_bot_button.collidepoint(mouse_pos):
        if mouse_click[0] == 1:
            return True
    elif exit_button.collidepoint(mouse_pos):
        if mouse_click[0] == 1:
            sys.exit()
    return None

# Function to select paddle color
def select_color():
    color_picker = pygame.Rect(200, 200, 400, 200)
    pygame.draw.rect(screen, WHITE, color_picker)
    pygame.draw.rect(screen, WHITE, (250, 250, 100, 100))
    pygame.draw.rect(screen, BLACK, (350, 250, 100, 100))
    pygame.draw.rect(screen, BLACK, (250, 370, 100, 100))
    pygame.draw.rect(screen, WHITE, (350, 370, 100, 100))

    color_text = FONT.render("Choose Your Color", True, BLACK)
    screen.blit(color_text, (270, 220))

    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    if mouse_click[0] == 1:
        if 250 <= mouse_pos[0] <= 350 and 250 <= mouse_pos[1] <= 350:
            return WHITE
        elif 350 <= mouse_pos[0] <= 450 and 250 <= mouse_pos[1] <= 350:
            return BLACK
        elif 250 <= mouse_pos[0] <= 350 and 370 <= mouse_pos[1] <= 470:
            return BLACK
        elif 350 <= mouse_pos[0] <= 450 and 370 <= mouse_pos[1] <= 470:
            return WHITE

    return None

# Main game loop
clock = pygame.time.Clock()
running = True
game_started = False
vs_bot = None
left_paddle_color = WHITE
right_paddle_color = BLACK
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type ==
