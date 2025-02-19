import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Missile Command")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Missile class
class Missile:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = 0
        self.speed = random.randint(1, 5)
    
    def move(self):
        self.y += self.speed
    
    def draw(self):
        pygame.draw.line(screen, RED, (self.x, self.y), (self.x, self.y + 10), 2)

# Game loop
def game_loop():
    clock = pygame.time.Clock()
    missiles = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Add new missile
        if random.randint(1, 20) == 1:
            missiles.append(Missile())
        
        # Move and draw missiles
        screen.fill(BLACK)
        for missile in missiles:
            missile.move()
            missile.draw()
        
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    game_loop()