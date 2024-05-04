import pygame
import sys
import math

# Pygame başlatma
pygame.init()

# Ekran ayarları
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Çift Kale Maç')

# Renkler
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Oyuncu ve top ayarları
player_size = 50
ball_size = 30
player1_pos = [width / 2, height - 2 * player_size]
player2_pos = [width / 2, player_size]
ball_pos = [width / 2, height / 2]
ball_speed = [2, 2]
player_speed = 5

# Skor ayarları
player1_score = 0
player2_score = 0
font = pygame.font.Font(None, 36)


# Yansıma hesaplama fonksiyonu
def calculate_reflection(player_pos, player_speed, ball_pos, ball_speed):
    # Oyuncu ve top arasındaki vektörü hesapla
    dx = ball_pos[0] - player_pos[0]
    dy = ball_pos[1] - player_pos[1]

    # Normalleştir
    distance = math.hypot(dx, dy)
    dx, dy = dx / distance, dy / distance

    # Topun yeni hızını hesapla
    new_speed = [-dx * player_speed + ball_speed[0], -dy * player_speed + ball_speed[1]]
    return new_speed


# Oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    # Oyuncu 1 kontrolleri
    if keys[pygame.K_a]:
        player1_pos[0] -= player_speed
    if keys[pygame.K_d]:
        player1_pos[0] += player_speed
    if keys[pygame.K_w]:
        player1_pos[1] -= player_speed
    if keys[pygame.K_s]:
        player1_pos[1] += player_speed

    # Oyuncu 2 kontrolleri
    if keys[pygame.K_LEFT]:
        player2_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player2_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player2_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player2_pos[1] += player_speed

    # Topun hareketi
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Topun sınırlarla etkileşimi
    if ball_pos[0] >= width - ball_size or ball_pos[0] <= 0:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] >= height - ball_size or ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]

    # Topun oyunculara çarpması
    if player1_pos[0] < ball_pos[0] < player1_pos[0] + player_size and player1_pos[1] < ball_pos[1] < player1_pos[
        1] + player_size:
        ball_speed = calculate_reflection(player1_pos, player_speed, ball_pos, ball_speed)
    if player2_pos[0] < ball_pos[0] < player2_pos[0] + player_size and player2_pos[1] < ball_pos[1] < player2_pos[
        1] + player_size:
        ball_speed = calculate_reflection(player2_pos, player_speed, ball_pos, ball_speed)

   
