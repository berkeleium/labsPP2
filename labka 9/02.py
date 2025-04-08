import pygame
import random
import time

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 600, 600
CELL = 30  # Размер одной клетки
FPS = 5    # Начальная скорость игры

# Цвета
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)    
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
colorPURPLE = (128, 0, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Verdana", 60)
game_over_text = font.render("Game Over", True, colorRED)
score_font = pygame.font.SysFont("Verdana", 20)

def draw_grid():
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx = 1
        self.dy = 0
        self.growing = False
        self.score = 0

    def move(self):
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        
        # Проверка выхода за границы (телепортация)
        new_head.x = new_head.x % (WIDTH // CELL)
        new_head.y = new_head.y % (HEIGHT // CELL)

        # Проверка столкновения с собой
        if any(new_head.x == segment.x and new_head.y == segment.y for segment in self.body):
            return False

        # Добавляем новую голову
        self.body.insert(0, new_head)

        # Удаляем хвост, если не растем
        if not self.growing:
            self.body.pop()
        else:
            self.growing = False

        return True

    def draw(self):
        # Голова красного цвета
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        # Тело желтого цвета
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food_manager):
        """Проверка столкновения с едой"""
        for food in food_manager.foods:
            if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
                self.growing = True
                self.score += food.value
                food_manager.remove_food(food)
                return

class Food:
    def __init__(self):
        self.pos = self.generate_random_pos()
        self.spawn_time = time.time()  # Время появления
        self.lifetime = random.uniform(5, 15)  # Время жизни (5-15 секунд)
        self.value = 1

    def generate_random_pos(self):
        """Генерация случайной позиции"""
        return Point(random.randint(0, WIDTH // CELL - 1), 
                   random.randint(0, HEIGHT // CELL - 1))

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

    def is_expired(self):
        """Проверка, истекло ли время жизни"""
        return time.time() - self.spawn_time > self.lifetime

class SpecialFood(Food):
    def __init__(self):
        super().__init__()
        self.value = 3  # Больше очков
        self.lifetime = random.uniform(3, 7)  # Меньше времени жизни

    def draw(self):
        """Отрисовка специальной еды фиолетовым цветом"""
        pygame.draw.rect(screen, colorPURPLE, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

class FoodManager:
    def __init__(self):
        self.foods = []
        self.last_spawn_time = time.time()
        self.spawn_interval = 3  # Интервал спавна еды (секунды)

    def update(self):
        """Обновление состояния еды"""
        current_time = time.time()
        
        # Удаляем просроченную еду
        self.foods = [food for food in self.foods if not food.is_expired()]
        
        # Добавляем новую еду по истечении интервала
        if current_time - self.last_spawn_time > self.spawn_interval:
            self.spawn_food()
            self.last_spawn_time = current_time

    def spawn_food(self):
        """Создание новой еды"""
        # 70% - обычная еда, 30% - специальная
        food = SpecialFood() if random.random() < 0.3 else Food()
        self.foods.append(food)

    def remove_food(self, food):
        """Удаление еды"""
        if food in self.foods:
            self.foods.remove(food)

    def draw(self):
        """Отрисовка всей еды"""
        for food in self.foods:
            food.draw()

# Инициализация игровых объектов
snake = Snake()
food_manager = FoodManager()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx, snake.dy = 1, 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx, snake.dy = -1, 0
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx, snake.dy = 0, 1
            elif event.key == pygame.K_UP and snake.dy == 0:
                snake.dx, snake.dy = 0, -1

    screen.fill(colorBLACK)
    draw_grid()
    
    # Обновление состояния еды
    food_manager.update()
    
    if not snake.move():
        # Конец игры при столкновении с собой
        screen.fill(colorBLACK)
        center_rect = game_over_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(game_over_text, center_rect)
        pygame.display.flip()
        pygame.time.delay(2000)
        running = False
    
    # Проверка столкновений с едой
    snake.check_collision(food_manager)
    
    snake.draw()
    food_manager.draw()
    
    # Отображение счета
    score_text = score_font.render(f"Счет: {snake.score}", True, colorWHITE)
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()