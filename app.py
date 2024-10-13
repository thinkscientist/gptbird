import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH = 400
HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
SKY_BLUE = (135, 206, 235)

# Game settings
FPS = 60
GRAVITY = 0.4
BIRD_JUMP = -8
PIPE_SPEED = -2
PIPE_GAP = 180
PIPE_FREQUENCY = 2000  # milliseconds

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GPT Bird")
clock = pygame.time.Clock()

# Load fonts
font = pygame.font.SysFont(None, 48)
small_font = pygame.font.SysFont(None, 36)

# Load images for parallax background
background_sky = pygame.image.load("sky.png").convert()
background_trees = pygame.image.load("trees3.png").convert_alpha()

# Load sound effects
jump_sound = pygame.mixer.Sound("jump_sound.mp3")

# Load pipe image for texture
pipe_image = pygame.image.load("pipe.png").convert_alpha()

# Bird class with bird shape
class Bird:
    def __init__(self):
        # Load bird image or create a simple bird shape
        self.image = pygame.Surface((40, 30), pygame.SRCALPHA)
        # Draw the bird body (ellipse)
        pygame.draw.ellipse(self.image, (255, 215, 0), [0, 5, 30, 20])  # Gold color
        # Draw the bird wing
        pygame.draw.polygon(self.image, (255, 165, 0), [(15, 15), (5, 25), (25, 25)])  # Orange wing
        # Draw the bird beak
        pygame.draw.polygon(self.image, (255, 140, 0), [(30, 15), (35, 13), (35, 17)])  # Dark orange beak
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 4, HEIGHT // 2)
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.rect.y += int(self.velocity)

    def jump(self):
        self.velocity = BIRD_JUMP
        jump_sound.play()  # Play jump sound effect

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# Pipe class with 3D texture
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.height = random.randint(50, HEIGHT - PIPE_GAP - 50)
        self.top_rect = pygame.Rect(self.x, 0, 50, self.height)
        self.bottom_rect = pygame.Rect(self.x, self.height + PIPE_GAP, 50, HEIGHT - self.height - PIPE_GAP)
        # Scale the pipe image to the appropriate size
        self.top_image = pygame.transform.scale(pipe_image, (50, self.height))
        self.bottom_image = pygame.transform.scale(pipe_image, (50, HEIGHT - self.height - PIPE_GAP))

    def update(self):
        self.x += PIPE_SPEED
        self.top_rect.x = self.x
        self.bottom_rect.x = self.x

    def draw(self, surface):
        # Draw the textured pipes
        surface.blit(self.top_image, self.top_rect)
        surface.blit(self.bottom_image, self.bottom_rect)

# Button class
class Button:
    def __init__(self, text, x, y, width, height, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.callback = callback

    def draw(self, surface):
        pygame.draw.rect(surface, (70, 130, 180), self.rect)  # Steel Blue
        text_surf = small_font.render(self.text, True, WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Parallax background positions
sky_x = 0
trees_x = 0

# Function to draw the parallax background
def draw_parallax_background(surface):
    global sky_x, trees_x

    # Move the backgrounds
    sky_x -= 0.5  # Sky moves slower for parallax effect
    trees_x -= 1  # Trees move slightly faster

    # Reset positions to create seamless loop
    if sky_x <= -WIDTH:
        sky_x = 0
    if trees_x <= -WIDTH:
        trees_x = 0

    # Draw the sky background
    surface.blit(background_sky, (sky_x, 0))
    surface.blit(background_sky, (sky_x + WIDTH, 0))

    # Draw the trees background
    surface.blit(background_trees, (trees_x, HEIGHT - background_trees.get_height()))
    surface.blit(background_trees, (trees_x + WIDTH, HEIGHT - background_trees.get_height()))

# Game functions
def start_screen():
    title_text = font.render("GPT Bird", True, WHITE)
    title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    start_button = Button("Start Game", WIDTH // 2 - 75, HEIGHT // 2, 150, 50, main_game)

    while True:
        draw_parallax_background(screen)
        screen.blit(title_text, title_rect)
        start_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.is_clicked(event.pos):
                    start_button.callback()

        pygame.display.flip()
        clock.tick(FPS)

def game_over_screen(score):
    # Stop the music when the game is over
    pygame.mixer.music.stop()

    game_over_text = font.render("Game Over", True, WHITE)
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    game_over_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    score_rect = score_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 30))
    restart_button = Button("Restart", WIDTH // 2 - 75, HEIGHT // 2, 150, 50, main_game)

    while True:
        draw_parallax_background(screen)
        screen.blit(game_over_text, game_over_rect)
        screen.blit(score_text, score_rect)
        restart_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if restart_button.is_clicked(event.pos):
                    restart_button.callback()

        pygame.display.flip()
        clock.tick(FPS)

def main_game():
    global sky_x, trees_x
    # Reset background positions
    sky_x = 0
    trees_x = 0

    # Start playing the background music
    pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play(-1)  # -1 means the music will loop indefinitely

    bird = Bird()
    pipes = []
    score = 0
    last_pipe = pygame.time.get_ticks()

    running = True
    while running:
        clock.tick(FPS)
        draw_parallax_background(screen)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        # Update bird
        bird.update()

        # Add new pipes
        if pygame.time.get_ticks() - last_pipe > PIPE_FREQUENCY:
            pipes.append(Pipe())
            last_pipe = pygame.time.get_ticks()

        # Update pipes
        for pipe in pipes[:]:
            pipe.update()
            if pipe.x < -50:
                pipes.remove(pipe)
                score += 1

        # Collision detection
        for pipe in pipes:
            if bird.rect.colliderect(pipe.top_rect) or bird.rect.colliderect(pipe.bottom_rect):
                game_over_screen(score)
        if bird.rect.top <= 0 or bird.rect.bottom >= HEIGHT:
            game_over_screen(score)

        # Draw bird and pipes
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        # Draw score
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

# Start the game
start_screen()