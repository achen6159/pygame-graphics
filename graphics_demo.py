# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
SIZE = (800, 600)
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BRIGHT_BLUE = (39, 172, 244)
PURPLE = (179, 39, 244)
BRIGHT_GREEN = (70, 244, 39)
YELLOW = (244, 234, 41)
    

def draw_cloud(x, y):
    pygame.draw.ellipse(screen, WHITE, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, WHITE, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, WHITE, [x + 20, y + 20, 60, 40])
    
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
    '''sky'''
    screen.fill(BRIGHT_BLUE)

    '''grass'''
    pygame.draw.rect(screen, BRIGHT_GREEN, [0, 450, 800, 600])

    '''house'''
    pygame.draw.rect(screen, ORANGE, [300, 250, 300, 200])
    pygame.draw.rect(screen, BLACK, [300, 250, 300, 200], 3)
    pygame.draw.polygon(screen, BLACK, [[250, 250], [450, 150], [650, 250]], 5)
    pygame.draw.polygon(screen, RED, [[250, 250], [450, 150], [650, 250]])
    pygame.draw.rect(screen, BLACK, [400, 300, 100, 150], 5)
    pygame.draw.rect(screen, PURPLE, [400, 300, 100, 150])
    pygame.draw.ellipse(screen, BLACK, [415, 360, 15, 15])

    '''sun'''
    pygame.draw.ellipse(screen, YELLOW, [20, 20, 100, 100])
    
    pygame.draw.line(screen, YELLOW, [0, 60], [30, 60], 3)
    pygame.draw.line(screen, YELLOW, [5, 30], [30, 40], 3)
    pygame.draw.line(screen, YELLOW, [0, 90], [30, 80], 3)
    pygame.draw.line(screen, YELLOW, [6, 120], [30, 100], 3)
    pygame.draw.line(screen, YELLOW, [32, 140], [53, 110], 3)
    pygame.draw.line(screen, YELLOW, [70, 120], [70, 145], 3)
    pygame.draw.line(screen, YELLOW, [95, 110], [110, 140], 3)
    pygame.draw.line(screen, YELLOW, [105, 90], [140, 120], 3)
    pygame.draw.line(screen, YELLOW, [110, 80], [150, 85], 3)
    pygame.draw.line(screen, YELLOW, [105, 60], [145, 55], 3)
    pygame.draw.line(screen, YELLOW, [80, 55], [135, 25], 3)
    pygame.draw.line(screen, YELLOW, [90, 25], [110, 5], 3)
    pygame.draw.line(screen, YELLOW, [70, 30], [70, 0], 3)
    pygame.draw.line(screen, YELLOW, [45, 25], [30, 5], 3)

    '''clouds'''
    draw_cloud(50, 150)
    draw_cloud(200, 75)
    draw_cloud(350, 10)
    draw_cloud(475, 30)
    draw_cloud(650, 125)

    '''fence'''
    y = 380
    for x in range(5, 800, 30):
       pygame.draw.polygon(screen, WHITE, [[x+5, y+20], [x+10, y+35],
                                            [x+10, y+80], [x, y+80],
                                            [x, y+35]])
    pygame.draw.line(screen, WHITE, [0, 425], [800, 425], 5)
    pygame.draw.line(screen, WHITE, [0, 445], [800, 445], 5) 

    '''pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)'''
    '''pygame.draw.ellipse(screen, BLUE, [100, 100, 600, 300])'''
    '''pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)'''

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    '''pygame.draw.arc(screen, ORANGE, [100, 100, 100, 100], 0, math.pi/2, 1)'''
    '''pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)'''


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
