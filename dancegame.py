import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CHARACTER_WIDTH, CHARACTER_HEIGHT = 100, 100
CHARACTER_X = (WIDTH - CHARACTER_WIDTH) // 2
CHARACTER_Y = (HEIGHT - CHARACTER_HEIGHT) // 2

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cartoon Dancing Game")

# Load the character image
character = pygame.image.load("character.png")
character = pygame.transform.scale(character, (CHARACTER_WIDTH, CHARACTER_HEIGHT))

# Character position
character_x = CHARACTER_X
character_y = CHARACTER_Y

# Create a clock to control the frame rate
clock = pygame.time.Clock()

def game_loop():
    global character_x, character_y

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    character_x -= 20
                elif event.key == pygame.K_RIGHT:
                    character_x += 20

        # Clear the screen
        screen.fill((255, 255, 255))

        # Draw the character
        screen.blit(character, (character_x, character_y))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    game_loop()
