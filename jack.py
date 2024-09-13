import pygame
pygame.init()

x = 500
y = 500

white = [255, 255, 255]
black = [0,0,0]
BLUE = (80,90,250)

Display = pygame.display.set_mode([x,y])
pygame.display.set_caption('blahblahblah')
clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

running = True

while running:
    Display.fill(BLUE)
    pygame.draw.rect(Display,white, [rect_x, rect_y 100, 20])
    rect_x = rect_x + 2
    rect_y = rect_y + 2
    clock.tick(60)
