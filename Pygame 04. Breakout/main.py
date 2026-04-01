import pygame
import sys
import time

from ball   import Ball
from paddle import Paddle

SCREEN_W  = 800
SCREEN_H  = 600
FPS       = 60

COUNTDOWN = 60        
MAX_LIVES =  3        

BG_COLOR      = ( 20,  20,  40)
TEXT_COLOR    = (220, 220, 220)
COLOR_WIN     = ( 80, 220, 120)
COLOR_LOSE    = (220,  80,  80)

pygame.init()
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
pygame.display.set_caption("Non farla cadere!")
clock      = pygame.time.Clock()
font_large  = pygame.font.SysFont("Arial", 56, bold=True)
font_medium = pygame.font.SysFont("Arial", 30)
font_small  = pygame.font.SysFont("Arial", 20)

def load_heart(size: int = 28) -> pygame.Surface:
    import os
    path = os.path.join(os.path.dirname(__file__), "assets", "heart.png")
    if os.path.exists(path):
        img = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(img, (size, size))
    surf = pygame.Surface((size, size), pygame.SRCALPHA)
    pygame.draw.circle(surf, (220, 60, 60), (size // 2, size // 2), size // 2)
    return surf

heart_img = load_heart()

def time_remaining(start: float, duration: int) -> float:
    return max(0.0, duration - (time.time() - start))

def is_expired(start: float, duration: int) -> bool:
    return time.time() - start >= duration

def draw_hud(surface: pygame.Surface, remaining: float, lives: int):
    # 1. Timer centrato in alto
    timer_surf = font_medium.render(str(int(remaining)), True, TEXT_COLOR)
    surface.blit(timer_surf, timer_surf.get_rect(centerx=SCREEN_W // 2, top=10))

    # 2. Vite in alto a destra
    for i in range(lives):
        x = SCREEN_W - 10 - (i + 1) * (heart_img.get_width() + 4)
        surface.blit(heart_img, (x, 10))

def draw_timer_bar(surface: pygame.Surface, remaining: float, duration: int):
    # Sfondo
    bg_rect = pygame.Rect(50, 48, SCREEN_W - 100, 10)
    pygame.draw.rect(surface, (80, 40, 40), bg_rect, border_radius=4)

    # Riempimento verde
    ratio = remaining / duration
    fill_w = int((SCREEN_W - 100) * ratio)
    if fill_w > 0:
        fill_rect = pygame.Rect(50, 48, fill_w, 10)
        pygame.draw.rect(surface, (80, 200, 80), fill_rect, border_radius=4)

def draw_end_screen(surface: pygame.Surface, won: bool):
    overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 160))
    surface.blit(overlay, (0, 0))

    msg   = "Hai vinto!" if won else "Hai perso!"
    color = COLOR_WIN    if won else COLOR_LOSE
    surf  = font_large.render(msg, True, color)
    surface.blit(surf, surf.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 - 40)))

    hint = font_medium.render("Premi R per rigiocare", True, TEXT_COLOR)
    surface.blit(hint, hint.get_rect(center=(SCREEN_W // 2, SCREEN_H // 2 + 40)))

def reset_game():
    ball = Ball(SCREEN_W // 2, int(SCREEN_H * 0.66))
    paddle = Paddle(SCREEN_W, SCREEN_H)
    start_time = time.time()
    lives = MAX_LIVES
    return (ball, paddle, start_time, lives)


# --- SETUP INIZIALE ---
ball, paddle, start_time, lives = reset_game()
game_over = False
won = False

running = True

while running:

    # ---- 1. EVENTI ------------------------------------------------ #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r and game_over:
                # Riavvia partita
                ball, paddle, start_time, lives = reset_game()
                game_over = False
                won = False

    # ---- 2. AGGIORNA ---------------------------------------------- #
    if not game_over:
        keys = pygame.key.get_pressed()
        paddle.update(keys)

        ball.update(SCREEN_W, SCREEN_H)
        ball.bounce_off_paddle(paddle.rect)

        # Se la pallina cade giù
        if not ball.alive:
            lives -= 1
            # ESPERIMENTO 2: Restringe la paddle ogni volta che cade
            paddle.rect.width = max(40, paddle.rect.width - 15)
            
            if lives > 0:
                ball = Ball(SCREEN_W // 2, int(SCREEN_H * 0.66))
            else:
                game_over = True
                
        # Controlla timer
        if is_expired(start_time, COUNTDOWN):
            game_over = True
            
        # Determina vittoria/sconfitta
        remaining = time_remaining(start_time, COUNTDOWN)
        if game_over:
            won = lives > 0 and is_expired(start_time, COUNTDOWN)

    # ---- 3. DISEGNA ----------------------------------------------- #
    screen.fill(BG_COLOR)

    pygame.draw.rect(screen, (80, 180, 220), paddle.rect, border_radius=4)
    ball.draw(screen)
    
    draw_hud(screen, remaining, lives)
    draw_timer_bar(screen, remaining, COUNTDOWN)

    if game_over:
        draw_end_screen(screen, won)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
