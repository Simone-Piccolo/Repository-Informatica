import pygame

# --- COSTANTI DELLA PALLINA ---
BALL_RADIUS  = 12
BALL_COLOR   = (220, 220,  80)  # Colore giallo
BALL_SPEED_X =  4               # Velocità orizzontale iniziale
BALL_SPEED_Y = -5               # Valore negativo: la pallina parte andando verso l'alto

class Ball:
    """
    Classe che gestisce la pallina: movimento, rimbalzi e disegno a schermo.
    """
    def __init__(self, x: int, y: int):
        # Coordinate del centro della pallina
        self.x     = x
        self.y     = y
        # Velocità attuale lungo gli assi X e Y
        self.vel_x = BALL_SPEED_X
        self.vel_y = BALL_SPEED_Y
        # Stato della pallina: se False, significa che è caduta fuori dallo schermo
        self.alive = True

    def update(self, screen_w: int, screen_h: int):
        """Aggiorna la posizione della pallina e gestisce i rimbalzi contro i muri."""
        
        # 1. Aggiorna la posizione sommando la velocità attuale
        self.x += self.vel_x
        self.y += self.vel_y

        # 2. Rimbalzo sul bordo sinistro
        if self.x - BALL_RADIUS <= 0:
            self.x = BALL_RADIUS      # Riporta la pallina esattamente a filo col bordo
            self.vel_x = -self.vel_x  # Inverte la direzione orizzontale (verso destra)

        # 3. Rimbalzo sul bordo destro
        elif self.x + BALL_RADIUS >= screen_w:
            self.x = screen_w - BALL_RADIUS
            self.vel_x = -self.vel_x  # Inverte la direzione (verso sinistra)

        # 4. Rimbalzo sul bordo superiore (soffitto)
        if self.y - BALL_RADIUS <= 0:
            self.y = BALL_RADIUS
            self.vel_y = -self.vel_y  # Inverte la direzione verticale (inizia a scendere)

        # 5. Bordo inferiore (la pallina cade nel vuoto)
        elif self.y - BALL_RADIUS >= screen_h:
            self.alive = False        # Segnala la perdita di una vita al main.py

    def bounce_off_paddle(self, paddle_rect: pygame.Rect):
        """Gestisce la collisione e il rimbalzo sulla racchetta del giocatore."""
        
        # Condizione A: verifico che la pallina stia effettivamente scendendo.
        # Questo evita che la pallina si incastri e rimbalzi all'infinito 
        # se colpisce la racchetta di striscio o dal basso.
        if self.vel_y > 0:
            
            # Creo un rettangolo fittizio (hitbox) grande quanto la pallina 
            # per poter usare le funzioni di collisione native di Pygame
            ball_rect = pygame.Rect(self.x - BALL_RADIUS,
                                    self.y - BALL_RADIUS,
                                    BALL_RADIUS * 2,
                                    BALL_RADIUS * 2)
            
            # Condizione B: i due rettangoli (pallina e racchetta) si stanno toccando
            if ball_rect.colliderect(paddle_rect):
                
                # Inverte la direzione verticale (la pallina torna a salire)
                self.vel_y = -self.vel_y
                
                # Sposta fisicamente la pallina esattamente sopra la racchetta.
                # È fondamentale per evitare che al frame successivo risulti ancora 
                # "incastrata" dentro la racchetta (effetto colla).
                self.y = paddle_rect.top - BALL_RADIUS
                
                # Effetto angolo: cambia la traiettoria orizzontale in base a dove 
                # la pallina colpisce la racchetta. Se colpisce il bordo sinistro, 
                # la manda a sinistra e viceversa.
                offset = self.x - paddle_rect.centerx
                self.vel_x = offset // 10

                # ESPERIMENTO 1: Accelerazione progressiva 
                # Aumenta la velocità del 5% a ogni rimbalzo valido sulla racchetta
                if abs(self.vel_y) < 15: # Limite massimo di velocità per evitare che diventi ingiocabile
                    self.vel_y = int(self.vel_y * 1.05)

    def draw(self, surface: pygame.Surface):
        """Disegna la pallina sullo schermo come un cerchio pieno."""
        
        # pygame.draw.circle richiede che le coordinate del centro siano numeri interi,
        # quindi convertiamo self.x e self.y (che potrebbero essere decimali) con int()
        pygame.draw.circle(surface, BALL_COLOR, (int(self.x), int(self.y)), BALL_RADIUS)
