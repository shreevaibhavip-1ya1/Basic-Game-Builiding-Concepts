import pygame

pygame.init()

window = pygame.display.set_mode((400,400))

window.fill((255, 255, 255))

GREEN = (0, 255 , 0)

# Solid circle
pygame.draw.circle(window, GREEN, (300, 300), 50)

# Outline circle
pygame.draw.circle(window, GREEN, (300, 300), 50, 3)

# Game loop
running = True

while running:
  
  for event in pygame.event.get():
    
    if event.type == pygame.QUIT:
      running = False
      
pygame.quit()
