# A scene that can become a sunny day or a rainy night
# Unit 11 - Graphics
#
# Annie C. 


# Imports
import pygame
import random

# Initialize game engine
pygame.mixer.pre_init()
pygame.init()

# Window
SIZE = (800, 600)
TITLE = "Sunny Day"
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60

# Colors
RED = (255, 0, 0)
GREEN = (0, 175, 0)
WHITE = (255, 255, 255)
BLUE = (75, 200, 255)
YELLOW = (255, 255, 175)
DARK_BLUE = (0, 0, 255)
GREY_BLUE = (29, 77, 155)
GREY = (102, 115, 117)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BRIGHT_BLUE = (39, 172, 244)
PURPLE = (179, 39, 244)
BRIGHT_GREEN = (89, 244, 66)
YELLOW = (244, 234, 41)
BROWN = (99, 63, 9)
DARK_GREEN = (12, 135, 24)
BRIGHT_YELLOW = (247, 238, 66)
PINK = (237, 23, 176)
LIGHTNING_YELLOW = (242, 223, 14)
BACK_BLUE = (103, 151, 229)
FRONT_BLUE = (176, 196, 232)
LIGHT_BLUE = (93, 149, 200)
BUSH_GREEN = (29, 140, 12)


# Make clouds
num_clouds = 30
near_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 100)
    loc = [x, y]
    near_clouds.append(loc)

num_clouds = 50
far_clouds = []

for i in range(num_clouds):
    x = random.randrange(0, 1600)
    y = random.randrange(-50, 300)
    loc = [x, y]
    far_clouds.append(loc)


#Make rain

num_small_drops = 500
srain = []

num_big_drops = 50
brain = []

num_huge_drops = 2
hrain = []

for i in range(num_small_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(1, 5)
    stop = random.randrange(400, 700)
    sr = [x, y, r, r, stop]
    srain.append(sr)

for i in range(num_big_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(10, 14)
    stop = random.randrange(600, 700)
    br = [x, y, r, r, stop]
    brain.append(br)

for i in range(num_huge_drops):
    x = random.randrange(0, 1000)
    y = random.randrange(-100, 600)
    r = random.randrange(30, 50)
    stop = random.randrange(600, 700)
    hr = [x, y, r, r, stop]
    hrain.append(hr)

# Sound Effects
pygame.mixer.music.load("sounds/rain.ogg")
thunder = pygame.mixer.Sound("sounds/thunder.ogg")

def draw_cloud(loc, color):
    x = loc[0]
    y = loc[1]
    
    pygame.draw.ellipse(screen, color, [x, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 60, y + 20, 40 , 40])
    pygame.draw.ellipse(screen, color, [x + 20, y + 10, 25, 25])
    pygame.draw.ellipse(screen, color, [x + 35, y, 50, 50])
    pygame.draw.rect(screen, color, [x + 20, y + 20, 60, 40])

def draw_small_drop(sr):
    rect = sr[:4]
    pygame.draw.ellipse(screen, BACK_BLUE, rect)

def draw_big_drop(br):
    rect = br[:4]
    pygame.draw.ellipse(screen, FRONT_BLUE, rect)

def draw_huge_drop(hr):
    rect = hr[:4]
    pygame.draw.ellipse(screen, BLUE, rect)  

def draw_tree(x, y):
    pygame.draw.rect(screen, BROWN, [x + 20, y + 20, 50, 200])
    pygame.draw.ellipse(screen, DARK_GREEN, [x - 15, y - 50, 120, 150])

def draw_house(x, y):
    pygame.draw.rect(screen, ORANGE, [x, y, 300, 200])
    pygame.draw.rect(screen, BLACK, [x, y, 300, 200], 3)
    pygame.draw.polygon(screen, BLACK, [[x - 50, y], [x + 150, y - 100], [x + 350, y]], 5)
    pygame.draw.polygon(screen, RED, [[x - 50, y], [x + 150, y - 100], [x + 350, y]])
    pygame.draw.rect(screen, BLACK, [x + 100, y + 50, 100, 150], 5)
    pygame.draw.rect(screen, PURPLE, [x + 100, 300, 100, 150])
    pygame.draw.ellipse(screen, BLACK, [x + 115, y + 110, 15, 15])

def draw_window(x, y, color):
    pygame.draw.rect(screen, color, [x + 15, y + 20, 70, 70])
    pygame.draw.rect(screen, color, [x + 215, y + 20, 70, 70])
    pygame.draw.rect(screen, BLACK, [x + 15, y + 20, 70, 70], 3)
    pygame.draw.rect(screen, BLACK, [x + 215, y + 20, 70, 70], 3)
    pygame.draw.line(screen, BLACK, [x + 15 , y + 55], [x + 85, y + 55], 3)
    pygame.draw.line(screen, BLACK, [x + 50, y + 20], [x + 50, y + 90], 3)
    pygame.draw.line(screen, BLACK, [x + 215, y + 55], [x + 285, y + 55], 3)
    pygame.draw.line(screen, BLACK, [x + 250, y + 20], [x + 250, y + 90], 3)
    

def draw_flowers(x, y):
    pygame.draw.rect(screen, DARK_GREEN, [x + 2, y + 10, 5, 20])
    pygame.draw.ellipse(screen, RED, [x + 5, y + 6, 10, 10])
    pygame.draw.ellipse(screen, RED, [x, y + 10, 10, 10])
    pygame.draw.ellipse(screen, RED, [x - 6, y + 6, 10, 10])
    pygame.draw.ellipse(screen, RED, [x - 6, y + 2, 10, 10])
    pygame.draw.ellipse(screen, RED, [x, y - 3, 10, 10])
    pygame.draw.ellipse(screen, RED, [x + 6, y + 2, 10, 10])
    pygame.draw.ellipse(screen, RED, [x + 4, y + 4, 10, 10])
    pygame.draw.ellipse(screen, YELLOW, [x, y + 4, 10, 10])
    

def draw_bushes(x, y):
    pygame.draw.ellipse(screen, BUSH_GREEN, [x + 400, y + 20, 30, 150])


daytime = True
lights_on = False

# Game loop

done = False
lightning = False

while not done:
    # Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                lightning = True
                thunder.play()
            elif event.key == pygame.K_SPACE:
                daytime = not daytime
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                lightning = False
            elif event.key == pygame.K_l:
                lights_on = not lights_on
            elif event.key == pygame.K_SPACE:
                daytime = daytime
           
    # Game logic
    ''' move clouds '''
    for c in far_clouds:
        c[0] -= 1

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 150)

    for c in near_clouds:
        c[0] -= 2

        if c[0] < -100:
            c[0] = random.randrange(800, 1600)
            c[1] = random.randrange(-50, 200)
    ''' move rain '''

    for sr in srain:
        sr[0] -= 1
        sr[1] += 4

        if sr[1] > sr[4]:
            sr[0] = random.randrange(0, 1000)
            sr[1] = random.randrange(-100, 0)

    for br in brain:
        br[0] -= 2
        br[1] += 8

        if br[1] > br[4]:
            br[0] = random.randrange(0, 1000)
            br[1] = random.randrange(-100, 0)

    for hr in hrain:
        hr[0] -= random.randrange(3, 5)
        hr[1] += random.randrange(10, 14)

        if hr[1] > hr[4]:
            hr[0] = random.randrange(0, 1000)
            hr[1] = random.randrange(-100, 0)  
            
    ''' set sky color '''
    if daytime:
        sky = BRIGHT_BLUE
        cloud = WHITE
        color = WHITE
        lightning = False
        pygame.mixer.music.play(-1)
        
    else:
        sky = GREY_BLUE
        cloud = GREY
        color = YELLOW
        
        
    # Drawing code
    ''' sky '''
    if lightning:
        screen.fill(LIGHTNING_YELLOW)
    else:
        screen.fill(sky)
    '''grass'''
    pygame.draw.rect(screen, BRIGHT_GREEN, [0, 450, 800, 600])

    #sun
    if daytime:
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
    #moon
    else:
        pygame.draw.ellipse(screen, BRIGHT_YELLOW, [575, 75, 100, 100])

    
    
    ''' clouds '''
    for c in far_clouds:
        draw_cloud(c, cloud)


    ''' small rain ''' 
    if not daytime:
        for sr in srain:
            draw_small_drop(sr)
    
    ''' clouds '''
    for c in near_clouds:
        draw_cloud(c, cloud)
    
    '''house'''
    draw_house(300, 250)
                     
    '''window'''
    draw_window(300, 250, color)
    
    '''bushes'''
    draw_bushes(260, 280)
    draw_bushes(310, 280)
    draw_bushes(360, 280)
    
    ''' fence '''
    y = 380
    for x in range(5, 800, 30):
        pygame.draw.polygon(screen, WHITE, [[x+5, y+20], [x+10, y+35],
                                            [x+10, y+80], [x, y+80],
                                            [x, y+35]])
    pygame.draw.line(screen, WHITE, [0, 425], [800, 425], 5)
    pygame.draw.line(screen, WHITE, [0, 445], [800, 445], 5)
    

    '''tree'''
    draw_tree(60, 300)

    '''flowers'''
    draw_flowers(200, 520)
    draw_flowers(600, 570)
    draw_flowers(50, 450)
    draw_flowers(500, 475)
    draw_flowers(700, 460)
    draw_flowers(400, 450)
    draw_flowers(300, 550)
    draw_flowers(150, 450)
    draw_flowers(270, 530)
    draw_flowers(650, 470)
    draw_flowers(300, 465)
    draw_flowers(750, 525)
    draw_flowers(670, 500)
    draw_flowers(120, 540)
    draw_flowers(350, 500)
    draw_flowers(450, 530)
    draw_flowers(550, 490)
    
    ''' big rain '''
    if not daytime:
        for br in brain:
            draw_big_drop(br)

    ''' huge rain '''
    if not daytime:
        for hr in hrain:
            draw_huge_drop(hr)

    # Update screen
    pygame.display.flip()
    clock.tick(refresh_rate)

# Close window on quit
pygame.quit()
