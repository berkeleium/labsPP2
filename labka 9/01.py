import pygame
import random
import time

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 600
FPS = 60
PLAYER_SPEED = 5
ENEMY_SPEED = 4

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load(r"C:\Users\Admin\Desktop\LAB\labka 9\images\AnimatedStreet.png")
player_img = pygame.image.load(r"C:\Users\Admin\Desktop\LAB\labka 9\images\Player.png")
enemy_img = pygame.image.load(r"C:\Users\Admin\Desktop\LAB\labka 9\images\Enemy.png")
base_coin_img = pygame.image.load(r"C:\Users\Admin\Desktop\LAB\labka 9\images\coin.png")

pygame.mixer.music.load(r"C:\Users\Admin\Desktop\LAB\labka 9\sounds\Lectures_G1_Week10_racer_resources_background.wav") 
crash_sound = pygame.mixer.Sound(r"C:\Users\Admin\Desktop\LAB\labka 9\sounds\Lectures_G1_Week10_racer_resources_crash.wav")
get_coin_sound = pygame.mixer.Sound(r"C:\Users\Admin\Desktop\LAB\labka 9\sounds\coin-recieved.mp3")

font = pygame.font.SysFont("Verdana", 60) 
game_over_text = font.render("Game Over", True, "red")
coin_count_font = pygame.font.SysFont("Verdana", 20)

COIN_SIZES = [
    {"size": (35, 35), "value": 1},  # Маленькая монета - 1 очко
    {"size": (55, 55), "value": 2},  # Средняя монета - 2 очка
    {"size": (75, 75), "value": 3}   # Большая монета - 3 очка
]

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2  # Начальная позиция по X
        self.rect.bottom = HEIGHT - 10  # Начальная позиция по Y
        
    def update(self):
        """Обновление позиции игрока"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        self.rect.x = max(0, min(self.rect.x, WIDTH - self.rect.width))

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.reset()
        
    def update(self):
        """Обновление позиции врага"""
        self.rect.y += ENEMY_SPEED
        if self.rect.top > HEIGHT:
            self.reset()

    def reset(self):
        """Сброс позиции врага"""
        self.rect.x = random.randint(0, WIDTH - self.rect.width)  # Случайная позиция по X
        self.rect.y = -self.rect.height  # Начальная позиция по Y (над экраном)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.set_random_type()  # Установка случайного типа
        self.reset()  # Установка начальной позиции
        
    def set_random_type(self):
        self.type = random.choice(COIN_SIZES)  # Выбираем случайный тип
        self.image = pygame.transform.scale(base_coin_img, self.type["size"])
        self.rect = self.image.get_rect()
        
    def update(self):
        """Обновление позиции монеты"""
        self.rect.y += ENEMY_SPEED // 2
        if self.rect.top > HEIGHT:
            self.reset()
            
    def reset(self):
        """Сброс позиции монеты"""
        self.set_random_type()
        self.rect.x = random.randint(0, WIDTH - self.rect.width)
        self.rect.y = -self.rect.height
        
    def get_value(self):
        """Получение ценности монеты"""
        return self.type["value"]

player = Player()
enemy = Enemy()
coin = Coin()

all_sprites = pygame.sprite.Group(player, enemy, coin)
enemies = pygame.sprite.Group(enemy)
coins = pygame.sprite.Group(coin)

clock = pygame.time.Clock()
score = 0
pygame.mixer.music.play(-1)  # Запуск фоновой музыки (с повтором)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    all_sprites.update()
    
    # Проверка столкновений с монетой
    if pygame.sprite.collide_rect(player, coin):
        score += coin.get_value()
        get_coin_sound.play()
        coin.reset()
        
        if score % 5 == 0:
            ENEMY_SPEED += 0.5
    
    # Проверка столкновения с врагом
    if pygame.sprite.collide_rect(player, enemy):
        crash_sound.play()
        screen.fill("black")
        screen.blit(game_over_text, game_over_text.get_rect(center=(WIDTH//2, HEIGHT//2)))
        pygame.display.flip()
        time.sleep(2)
        running = False
    
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    
    score_text = coin_count_font.render(f"Score: {score}", True, "black")
    screen.blit(score_text, (10, 10))
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()