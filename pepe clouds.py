# Computer Programming 1
# Unit 11 - Graphics
#
# A scene that uses loops to make stars and make a picket fence.


# Imports
import pygame
import random

# Initialize game engine
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
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

def draw_pepe(x, y):
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
    pygame.draw.ellipse(screen, BLACK, [x+45, y+11, 25, 9], 3.5)
    pygame.draw.ellipse(screen, WHITE, [x+20, y+11, 20, 9])
    pygame.draw.ellipse(screen, BLACK, [x+20, y+11, 20, 9], 3.5)
    pygame.draw.ellipse(screen, BLACK, [x+25, y+11.5, 7.5, 7.5])  
    pygame.draw.ellipse(screen, BLACK, [x+52, y+11.5, 7.5, 7.5])
   


   
# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True     

    # Game logic

             
    # Drawing code
    ''' sky '''
    screen.fill(BLUE)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' clouds '''
    draw_pepe(50, 150)
    draw_pepe(250, 75)
    draw_pepe(350, 125)
    draw_pepe(450, 175)
    draw_pepe(650, 100)

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                            [x+10, y+40], [x, y+40],
                                            [x, y+5]])
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)


    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
