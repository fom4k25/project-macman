import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MacMan (Pac-Man)")

# Цвета
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Игрок
player_size = 30
player_x, player_y = WIDTH // 2, HEIGHT // 2
speed = 5

# Еда
food = pygame.Rect(100, 100, 10, 10)

# Игровой цикл
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    screen.fill(BLACK)

    # Еда
    pygame.draw.rect(screen, BLUE, food)

    # Игрок
    pygame.draw.circle(screen, YELLOW, (player_x, player_y), player_size // 2)

    pygame.display.flip()
    clock.tick(30)
