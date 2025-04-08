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
MODE_SQUARE = 4
MODE_RIGHT3 = 5
MODE_EQUILATERAL3 = 6
MODE_RHOMBUS = 7

current_mode = MODE_PENCIL
drawing = False
start_pos = (0, 0)


def draw_rhombus(surface, color, rect, width):  
    points = [
        (rect.centerx, rect.top),
        (rect.right, rect.centery),
        (rect.centerx, rect.bottom),
        (rect.left, rect.centery)
    ]
    pygame.draw.polygon(surface, color, points, width)

def draw_equilateral_triangle(surface, color, start, end, width):
    side_length = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    height = side_length * math.sqrt(3) / 2
    
    points = [
        (start[0], start[1] + height),  # Нижний левый
        (start[0] + side_length, start[1] + height),  # Нижний правый
        (start[0] + side_length/2, start[1])  # Верхний
    ]
    pygame.draw.polygon(surface, color, points, width)

def draw_right_triangle(surface, color, start, end, width):
    points = [
        start,
        (start[0], end[1]),
        end
    ]
    pygame.draw.polygon(surface, color, points, width)


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

                elif current_mode == MODE_SQUARE:
                    size = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                    rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]), size, size)
                    pygame.draw.rect(base_layer, ColorLine, rect, THICKNESS)
                
                elif current_mode == MODE_RIGHT3:
                    draw_right_triangle(base_layer, ColorLine, start_pos, current_pos, THICKNESS)
                
                elif current_mode == MODE_EQUILATERAL3:
                    draw_equilateral_triangle(base_layer, ColorLine, start_pos, current_pos, THICKNESS)
                
                elif current_mode == MODE_RHOMBUS:
                    rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]), abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                    draw_rhombus(base_layer, ColorLine, rect, THICKNESS)
                    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_mode = MODE_LINE
            elif event.key == pygame.K_2:
                current_mode = MODE_RECT
            elif event.key == pygame.K_3:
                current_mode = MODE_CIRCLE
            elif event.key == pygame.K_4:
                current_mode = MODE_SQUARE
            elif event.key == pygame.K_5:
                current_mode = MODE_RIGHT3
            elif event.key == pygame.K_6:
                current_mode = MODE_EQUILATERAL3
            elif event.key == pygame.K_7:
                current_mode = MODE_RHOMBUS
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

            elif current_mode == MODE_SQUARE:
                size = max(abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]), size, size)
                pygame.draw.rect(screen, ColorLine, rect, THICKNESS)
                
            elif current_mode == MODE_RIGHT3:
                draw_right_triangle(screen, ColorLine, start_pos, current_pos, THICKNESS)
            
            elif current_mode == MODE_EQUILATERAL3:
                draw_equilateral_triangle(screen, ColorLine, start_pos, current_pos, THICKNESS)
            
            elif current_mode == MODE_RHOMBUS:
                rect = pygame.Rect(min(start_pos[0], current_pos[0]), min(start_pos[1], current_pos[1]), abs(current_pos[0] - start_pos[0]), abs(current_pos[1] - start_pos[1]))
                draw_rhombus(screen, ColorLine, rect, THICKNESS)
    
    font = pygame.font.SysFont(None, 24)
    mode_names = ["Карандаш (0)", "Линия (1)", "Прямоугольник (2)", "Круг (3)", "Квадрат (4)", "Прям. треугольник (5)", "Равност. треугольник (6)", "Ромб (7)"]
    text_surface = font.render(f"Режим: {mode_names[current_mode]}", True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    next_text = font.render(f"Color: {ColorLine}", True, "white")
    screen.blit(next_text, (10, 40))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()