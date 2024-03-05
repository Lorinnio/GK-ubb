import pygame
import math

# Inicjalizacja Pygame
pygame.init()

# Ustawienia ekranu
screen_size = (600, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Jedenastokąt')

# Kolory
black = (0, 0, 0)
white = (255, 255, 255)

# Parametry wielokąta
n = 11  # Liczba wierzchołków
radius = 150  # Promień
center = (300, 300)  # Środek okręgu

# Obliczanie współrzędnych wierzchołków
vertices = []
for i in range(n):
    angle = 2 * math.pi * i / n
    x = center[0] + radius * math.cos(angle)
    y = center[1] + radius * math.sin(angle)
    vertices.append((x, y))

# Główna pętla gry
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tło
    screen.fill(black)

    # Rysowanie wielokąta
    pygame.draw.polygon(screen, white, vertices)

    # Aktualizacja ekranu
    pygame.display.flip()

# Zakończenie Pygame
pygame.quit()
