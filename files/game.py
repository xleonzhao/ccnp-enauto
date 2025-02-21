import pygame
import curses
import random
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tank vs Plane")

# Colors
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

KEYLEFT = curses.KEY_LEFT
KEYRIGHT = curses.KEY_RIGHT

# Tank properties
tank_pos = {'x': 100, 'y': HEIGHT - 50}
tank_speed = 5

# Plane properties
plane_pos = {'x': WIDTH//2, 'y': 50}
plane_speed = 3

# Bullet properties (for testing)
bullet_list = []
tank_bullets = []

# Health system
tank_health = 100
plane_health = 100

running = True
clock = pygame.time.Clock()

while running:
    screen.fill(BLUE)  # Sky background
    
    # Handle tank movement
    keys = pygame.key.get_pressed()
    if keys[KEYLEFT]:
        tank_pos['x'] -= tank_speed
    if keys[KEYRIGHT]:
        tank_pos['x'] += tank_speed
    
    # Keep tank within screen bounds
    if tank_pos['x'] < 0:
        tank_pos['x'] = 0
    elif tank_pos['x'] > WIDTH - 50:
        tank_pos['x'] = WIDTH - 50
    
    # Draw tank and plane
    pygame.draw.rect(screen, GREEN, (tank_pos['x'], tank_pos['y'], 40, 30))
    pygame.draw.rect(screen, GREEN, (plane_pos['x'], plane_pos['y'], 40, 30))
    
    # Simple ground line
    pygame.draw.line(screen, GREEN, (0, HEIGHT-5), (WIDTH, HEIGHT-5), 5)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        # Tank shooting
        if event.type == KEYDOWN and event.key == K_SPACE:
            bullet = {'x': tank_pos['x'] + 20, 'y': tank_pos['y'], 'state': 'up'}
            bullet_list.append(bullet)
    
    # Update bullets and check collisions
    for i in range(len(bullet_list)):
        if bullet_list[i]['state'] == 'up':
            bullet_list[i]['y'] -= 5
        else:
            bullet_list[i]['y'] += 5
        
        if bullet_list[i]['y'] < 0 or bullet_list[i]['y'] > HEIGHT:
            del bullet_list[i]
    
    # Simple AI movement for the plane (random example)
    if random.random() < 0.02:  # 2% chance to change direction each frame
        direction = random.choice([-1, 1])
        plane_pos['x'] += plane_speed * direction
    
    # Ensure plane stays within screen bounds
    if plane_pos['x'] < 0:
        plane_pos['x'] = 0
    elif plane_pos['x'] > WIDTH - 40:
        plane_pos['x'] = WIDTH - 40
    
    # Check for collisions (simplified here)
    tank_rect = pygame.Rect(tank_pos['x'], tank_pos['y'], 40, 30)
    plane_rect = pygame.Rect(plane_pos['x'], plane_pos['y'], 40, 30)
    
    if tank_rect.colliderect(plane_rect):
        # Both would be damaged here
        pass
    
    # Update and draw bullets
    for bullet in bullet_list:
        pygame.draw.circle(screen, GREEN, (bullet['x'], bullet['y']), 5)
    
    # Simple health display
    font = pygame.font.Font(None, 24)
    text_tank = font.render(f"Tank: {tank_health}", True, GREEN)
    text_plane = font.render(f"Plane: {plane_health}", True, GREEN)
    screen.blit(text_tank, (10, 10))
    screen.blit(text_plane, (10, 40))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
