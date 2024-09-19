import pygame
pygame.init()

x = 400
y = 400

blue = [0, 0, 128]
white = [255, 255, 255]
orange = [255, 165, 0]
black = [0, 0, 0]

DISPLAY = pygame.display.set_mode([x, y])
pygame.display.set_caption('Ping Pong')

paddle1 = 250
paddle2 = 250

x_pos = 100
y_pos = 100

x_movement = 5
y_movement = 2

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    DISPLAY.fill(black)

    # Drawing the walls
    pygame.draw.rect(DISPLAY, blue, (0, 0, 400, 25))
    pygame.draw.rect(DISPLAY, blue, (0, 175, 400, 25))

    # Drawing the paddles
    pygame.draw.rect(DISPLAY, orange, (15, paddle1, 10, 25))
    pygame.draw.rect(DISPLAY, orange, (285, paddle2, 10, 25))

    # Drawing the ball (corrected the line below)
    pygame.draw.rect(DISPLAY, white, (x_pos, y_pos, 5, 5))

    # Update ball position
    x_pos = x_pos + x_movement
    y_pos = y_pos + y_movement

    if x_pos == 25 and paddle1 < y_pos + 2.5 < paddle1+25:
        x_movement = x_movement * -1

    if x_pos == 280 and paddle2 < y_pos +2.5 < paddle2+25:
        x_movement = x_movement * -1

    if y_pos < 25 or y_pos > 375:
        y_movement = y_movement * -1

    # Frame rate control
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and paddle1 >
25:
            paddle1 = paddle1 - 20
            elif event.key == pygame,K_s and paddle1 <
350:
            paddle1 = padle1 + 20
            elif event.key == pygame.K_u and paddle2 >
25:
            paddle2 = paddle2 - 20
            elif event.key == pygame.K_j and paddle2 <
350:
            paddle2 = paddle2 + 20
    pygame.display.flip()

pygame.quit()