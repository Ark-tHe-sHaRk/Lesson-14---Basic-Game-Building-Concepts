# Importing necessary libraries
import pygame

# Initializing Pygame
pygame.init()

# Creating the window
screen = pygame.display.set_mode((500, 300))  # Corrected dimensions to be a tuple

# Setting the title of the window
pygame.display.set_caption('Adding elements to my window!')

# Main Game Loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Filling the screen with white color
    screen.fill((255, 255, 255))

    # Adding a rectangle to the window
    pygame.draw.rect(screen, (0, 125, 225), pygame.Rect(50, 50, 80, 40))

    # Adding a solid rectangle to the window
    pygame.draw.rect(screen, (0, 255, 255), pygame.Rect(150, 50, 80, 40))

    # Adding a circle to the window
    pygame.draw.circle(screen, (0, 255, 171), (300, 70), 30)

    # Adding a line to the window
    pygame.draw.line(screen, (0, 255, 171), (50, 150), (150, 200), 5)

    # Adding a hexagon to the window
    pygame.draw.polygon(screen, (0, 255, 235), [(250, 150), (300, 180), (250, 210), 
                                                (200, 210), (150, 180), (200, 150)])
    # Adding text to the window
    font = pygame.font.Font(None, 30)
    text = font.render('Hello World!!!', True, (0, 0, 0))
    screen.blit(text, (180, 250)) 

    # Updating the display
    pygame.display.flip()

# Quitting Pygame
pygame.quit()
