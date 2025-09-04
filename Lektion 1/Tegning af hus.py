import pygame
import pygame.draw_py

pygame.init() # Initialize Pygame
screen = pygame.display.set_mode((640, 480)) # Create a window of 640x480 pixels
screen.fill((255, 255, 255)) # Fill the screen with white

pygame.draw.line(screen, (00, 00, 00), (100, 380), (300, 380), 5) #Gulvet
pygame.draw.line(screen, (128, 92, 32), (100, 380), (100, 200), 5) # Venstre væg
pygame.draw.line(screen, (128, 92, 32), (300, 380), (300, 200), 5) # Højre væg
pygame.draw.polygon(screen, (00, 00, 00), ((100, 200), (200, 100), (300, 200)), 5) # Taget
pygame.draw.circle(screen, (00, 00, 00), (250, 240), 30, 3) # Vinduet
pygame.draw.rect(screen, (00,00,00) , (140, 280, 60, 100), 3) # Døren
pygame.draw.circle(screen, (00, 00, 00), (185, 340), 4, 3) # Dørhåndtaget

# Make sure the window stays open until the user closes it
run_flag = True
while run_flag is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears