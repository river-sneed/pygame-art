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
TITLE = "pepe"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 30

# Colors
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
PURPLE = (83, 33, 158)

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
    #pygame.draw.ellipse(screen, BLACK, [x+45, y+11, 25, 9], 3)
    pygame.draw.ellipse(screen, WHITE, [x+20, y+11, 20, 9])
    #pygame.draw.ellipse(screen, BLACK, [x+20, y+11, 20, 9], 3)
    pygame.draw.ellipse(screen, BLACK, [x+25, y+11.5, 7.5, 7.5])  
    pygame.draw.ellipse(screen, BLACK, [x+52, y+11.5, 7.5, 7.5])  

def draw_pepe_red(x, y):
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
    pygame.draw.ellipse(screen, YELLOW, [x+83, y+39.5, 7.5, 7.5], 1)

def draw_fence(x,y):
    pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5], [x+10, y+40], [x, y+40], [x, y+5]])                                            
    pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
    pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)

def draw_fun_fence(x,y):
    pygame.draw.polygon(screen, RED, [[x, y], [x+5, y], [x, y+100], [x-5, y+100]])
    pygame.draw.polygon(screen, ORANGE, [[x+5, y], [x+10, y], [x+5, y+100], [x, y+100]])
    pygame.draw.polygon(screen, YELLOW, [[x+10, y], [x+15, y], [x+10, y+100], [x+5, y+100]])
    pygame.draw.polygon(screen, GREEN, [[x+15, y], [x+20, y], [x+15, y+100], [x+10, y+100]])
    pygame.draw.polygon(screen, BLUE, [[x+20, y], [x+25, y], [x+20, y+100], [x+15, y+100]])
    pygame.draw.polygon(screen, PURPLE, [[x+25, y], [x+30, y], [x+25, y+100], [x+20, y+100]])

    

''' make pepes '''
pepes = []
for i in range(20):
    x = random.randrange(-100, 1600)
    y = random.randrange(0,200)
    pepes.append([x, y])

fences = []
for i in range(1):
    x = 0
    y = 300
    fences.append([x, y])

boring = True
daytime = True
lights_on = True
fun = True

# Game loop
done = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                boring = not boring
            elif event.key == pygame.K_s:
                daytime = not daytime
            elif event.key == pygame.K_f:
                fun = not fun

                
    # Game logic
    ''' move pepes '''
    for p in pepes:
        p[0] -= 1

        if p[0] < -100:
            p[0] = random.randrange(800, 1600)
            p[1] = random.randrange(0, 200)

    for f in fences:
        if fun:
            f[0] = 1

        else:
            f[0] -= 1

            if f[0] < -100:
                f[0] = random.randrange(800, 1600)
                f[1] = random.randrange(0, 200

    ''' set sky color '''
    if daytime:
        sky = SKY
    else:
        sky = BLACK

    ''' set window color (if there was a house)'''
    if lights_on:
        window_color = YELLOW
    else:
        window_color = WHITE
        
    # Drawing code
    ''' sky '''
    screen.fill(sky)

    ''' sun '''
    pygame.draw.ellipse(screen, YELLOW, [575, 75, 100, 100])

    ''' clouds '''
    for p in pepes:
        x = p[0]
        y = p[1]

        if boring:
            draw_pepe(x,y)
        else:
            draw_pepe_red(x,y)

    '''fence'''
    for f in fences:
        x = f[0]
        y = f[1]

        if fun:
            draw_fence(x,y)
        else:
            draw_fun_fence(x,y)
                                        

    ''' grass '''
    pygame.draw.rect(screen, GREEN, [0, 400, 800, 200])

    ''' fence '''
'''    y = 380
    if fence:
        for x in range(5, 800, 30):
            pygame.draw.polygon(screen, WHITE, [[x+5, y], [x+10, y+5],
                                                [x+10, y+40], [x, y+40],
                                                [x, y+5]])
        pygame.draw.line(screen, WHITE, [0, 390], [800, 390], 5)
        pygame.draw.line(screen, WHITE, [0, 410], [800, 410], 5)
    else:
        for x in range(5, 800, 30):
)
                

                pygame.draw.polygon(screen, RED, [[x, y], [x+5, y], [x, y+100], [x-5, y+100]])
                pygame.draw.polygon(screen, ORANGE, [[x+5, y], [x+10, y], [x+5, y+100], [x, y+100]])
                pygame.draw.polygon(screen, YELLOW, [[x+10, y], [x+15, y], [x+10, y+100], [x+5, y+100]])
                pygame.draw.polygon(screen, GREEN, [[x+15, y], [x+20, y], [x+15, y+100], [x+10, y+100]])
                pygame.draw.polygon(screen, BLUE, [[x+20, y], [x+25, y], [x+20, y+100], [x+15, y+100]])
                pygame.draw.polygon(screen, PURPLE, [[x+25, y], [x+30, y], [x+25, y+100], [x+20, y+100]])'''



    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
