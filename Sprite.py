import pygame

# Start pygame
pygame.init()

# Create a Sprite
sprite1 = pygame.image.load("./images/burgercito.png")

# Create a screen
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello Pygame")
screen.fill((0, 0, 0))

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Renders the sprite 
    screen.blit(sprite1, (640/2 - 128/2, 480/2 - 128/2))

    # Refresh the screen to make visible the sprite
    pygame.display.update()

pygame.quit()
