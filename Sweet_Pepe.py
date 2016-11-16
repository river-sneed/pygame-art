# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "Bon Appetit my Memes"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
''' add colors you use as RGB values here '''
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
    #screen.fill(WHITE)
    #pygame.draw.rect(screen, RED, [50, 50, 400, 300])
    #pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
    #pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])
    #pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    screen.fill(WHITE)
    pygame.draw.ellipse(screen, SWEET_PEPE_BLUE, [-100, 400, 650, 400])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [-20, 150, 750, 400])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [50, 10, 380, 500])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [250, 10, 380, 500])
    pygame.draw.ellipse(screen, SWEET_PEPE_GREEN, [200, 70, 500, 170])
    pygame.draw.rect(screen, SWEET_PEPE_RED, [225, 375, 485, 75])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [190, 375, 75, 75])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [655, 375, 100, 37])
    pygame.draw.ellipse(screen, SWEET_PEPE_RED, [655, 415, 75, 37])
    pygame.draw.ellipse(screen, WHITE, [450, 110, 250, 90])
    pygame.draw.ellipse(screen, BLACK, [450, 110, 250, 90], 7)
    pygame.draw.ellipse(screen, WHITE, [200, 110, 200, 90])
    pygame.draw.ellipse(screen, BLACK, [200, 110, 200, 90], 7)
    pygame.draw.ellipse(screen, BLACK, [250, 115, 75, 75])
    pygame.draw.ellipse(screen, BLACK, [520, 115, 75, 75])
    

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    #pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)
    #pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
