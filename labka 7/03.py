import pygame

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
pos_x = 400
pos_y = 250

while True:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, "red", (pos_x, pos_y), 25)

    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and pos_y < 475:
                pos_y += 20
            if event.key == pygame.K_UP and pos_y > 25:
                pos_y -= 20
            if event.key == pygame.K_LEFT and pos_x > 25:
                pos_x -= 20
            if event.key == pygame.K_RIGHT and pos_x < 775:
                pos_x += 20
    # STEP = 20
    # BALL_RADIUS = 25
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_UP] and pos_y - BALL_RADIUS - STEP >= 0:
    #     pos_y -= STEP
    # if keys[pygame.K_DOWN] and pos_y + BALL_RADIUS + STEP <= 500:
    #     pos_y += STEP
    # if keys[pygame.K_LEFT] and pos_x - BALL_RADIUS - STEP >= 0:
    #     pos_x -= STEP
    # if keys[pygame.K_RIGHT] and pos_x + BALL_RADIUS + STEP <= 800:
    #     pos_x += STEP
    clock.tick(20)