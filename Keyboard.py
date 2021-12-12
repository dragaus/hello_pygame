import pygame
from pygame.locals import *

# Start pygame
pygame.init()

# Create a Sprite
sprite1 = pygame.image.load("./images/humingbird.png")

# Change size of sprite
sprite1 = pygame.transform.scale(sprite1, (64, 64))

# Create a screen
screen = pygame.display.set_mode((640, 480), 0, 32)
pygame.display.set_caption("Hello Keyboard")
# Use different rgb to change backgroudn color
screen.fill((126, 230, 242))

game_over = False

# This variable will hold the position of our sprite
x, y = (0, 0)

clock = pygame.time.Clock()

while not game_over:
    dt = clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # This is in charge of reading all pressed keys
    pressed = pygame.key.get_pressed()

    # This logical statement will determine what direction we will move our sprite
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        x, y = (0, 0)

    screen.fill((126, 230, 242))
    # Renders the sprite
    screen.blit(sprite1, (x, y))

    # Refresh the screen to make visible the sprite
    pygame.display.update()


pygame.quit()
