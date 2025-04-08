import pygame
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
base_layer = pygame.Surface((800, 600))
clock = pygame.time.Clock()
ColorLine = 'red'

mouse_pos = pygame.mouse.get_pos()
prev_pos = mouse_pos
current_pos = mouse_pos

THICKNESS = 5

MODE_PENCIL = 0
MODE_LINE = 1
MODE_RECT = 2
MODE_CIRCLE = 3

current_mode = MODE_PENCIL
drawing = False
start_pos = (0, 0)

running = True
while running:
    current_pos = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = current_pos
                prev_pos = current_pos
                
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and drawing:
                drawing = False
                if current_mode == MODE_LINE:
                    pygame.draw.line(base_layer, ColorLine, start_pos, current_pos, THICKNESS)
                elif current_mode == MODE_RECT:
                    rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]), abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                    pygame.draw.rect(base_layer, ColorLine, rect, THICKNESS)
                elif current_mode == MODE_CIRCLE:
                    radius = int(math.hypot(current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
                    pygame.draw.circle(base_layer, ColorLine, start_pos, radius, THICKNESS)
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_mode = MODE_LINE
            elif event.key == pygame.K_2:
                current_mode = MODE_RECT
            elif event.key == pygame.K_3:
                current_mode = MODE_CIRCLE
            elif event.key == pygame.K_0:
                current_mode = MODE_PENCIL
                
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            elif event.key == pygame.K_MINUS and THICKNESS > 1:
                THICKNESS -= 1
            elif event.key == pygame.K_g:
                ColorLine = 'green'
            elif event.key == pygame.K_b:
                ColorLine = 'blue'
            elif event.key == pygame.K_r:
                ColorLine = 'red'
            elif event.key == pygame.K_c:
                base_layer.fill((0, 0, 0))

    screen.fill((0, 0, 0))
    screen.blit(base_layer, (0, 0))
    
    if drawing:
        if current_mode == MODE_PENCIL:
            pygame.draw.line(base_layer, ColorLine, prev_pos, current_pos, THICKNESS)
            prev_pos = current_pos
        else:
            if current_mode == MODE_LINE:
                pygame.draw.line(screen, ColorLine, start_pos, current_pos, THICKNESS)
            elif current_mode == MODE_RECT:
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]), abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                pygame.draw.rect(screen, ColorLine, rect, THICKNESS)
            elif current_mode == MODE_CIRCLE:
                radius = int(math.hypot(current_pos[0] - start_pos[0], current_pos[1] - start_pos[1]))
                pygame.draw.circle(screen, ColorLine, start_pos, radius, THICKNESS)
    
    font = pygame.font.SysFont(None, 24)
    mode_text = ["Карандаш (0)", "Линия (1)", "Прямоугольник (2)", "Круг (3)"][current_mode]
    text_surface = font.render(f"Режим: {mode_text}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    next_text = font.render(f"Color: {ColorLine}", True, "white")
    screen.blit(next_text, (10, 40))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()