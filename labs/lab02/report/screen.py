import os
import pygame

# Чтобы в WSL не ругался на звук (по желанию)
os.environ["SDL_AUDIODRIVER"] = "dummy"

pygame.init()

# Размеры окна
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hello appsec world")

# Цвет фона
bg_color = (255, 255, 255)

# Текст
font = pygame.font.SysFont(None, 75)
text = font.render("Hello appsec world*", True, (0, 255, 0))
text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # заливаем фон
    screen.fill(bg_color)

    # рисуем рамку вокруг окна
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, screen_width, screen_height), 1)

    # рисуем текст
    screen.blit(text, text_rect)

    # ОБНОВЛЯЕМ ЭКРАН КАЖДЫЙ КАДР
    pygame.display.flip()

pygame.quit()
