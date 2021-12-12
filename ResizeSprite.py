import pygame

# Start pygame
pygame.init()

# Create a Sprite
sprite1 = pygame.image.load("./images/miniJochito.png")

# Change size of sprite
sprite1 = pygame.transform.scale(sprite1, (256, 256))

# Create a screen
screen = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption("Hello Jochito")
screen.fill((0, 0, 0))

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Renders the sprite
    screen.blit(sprite1, (screen.get_width()/2 - sprite1.get_width() /
                2, screen.get_height()/2 - sprite1.get_height()/2))

    # Refresh the screen to make visible the sprite
    pygame.display.update()

pygame.quit()
