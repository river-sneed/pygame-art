# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (1000, 800)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
SKY = (135, 206, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125, 0)
YELLOW = (255, 255, 0)
SWEET_PEPE_GREEN = (104, 152, 76 )
SWEET_PEPE_BLUE = ( 35, 74, 252 )
SWEET_PEPE_RED = ( 169, 106, 64 )


# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 


    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    x = 100
    y = 100

    pygame.draw.ellipse(screen, SWEET_PEPE_BLUE, [x-10, y+40, 65, 40])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x-2, y+15, 75, 40])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x+5, y+1, 38, 50])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x+25, y+1, 38, 50])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [x+20, y+7, 50, 17])
    pygame.draw.rect(screen, SWEET_PEPE_RED, [x+22.5, y+37.5, 48.5, 7.5])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [x+19, y+37.5, 7.5, 7.5])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [x+65.5, y+37.5, 10.0, 3.7])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [x+65.5, y+41.5, 7.5, 3.7])
    pygame.draw.ellipse(screen, WHITE, [x+45, y+11, 25, 9])
    pygame.draw.ellipse(screen, RED, [x+45, y+11, 25, 9], 3)
    pygame.draw.ellipse(screen, WHITE, [x+20, y+11, 20, 9])
    pygame.draw.ellipse(screen, RED, [x+20, y+11, 20, 9], 3)
    pygame.draw.ellipse(screen, BLACK, [x+25, y+11.5, 7.5, 7.5])  
    pygame.draw.ellipse(screen, BLACK, [x+52, y+11.5, 7.5, 7.5])
    pygame.draw.ellipse(screen, WHITE, [x+45, y+39.5, 7.5, 7.5])
    pygame.draw.rect(screen, WHITE, [x+47, y+39.5, 40, 6])
    pygame.draw.ellipse(screen, RED, [x+83, y+39.5, 7.5, 7.5])

    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
