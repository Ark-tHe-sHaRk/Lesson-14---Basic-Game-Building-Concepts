#Importing nessesary libraries
import pygame

#Importing the pygame module
pygame.init()

#Setting the dimesions of the window
screen = pygame.display.set_mode((300, 300))
done = False

#Setting the title of window
pygame.display.set_caption("Drawing Rectangle")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 125, 225), pygame.Rect(30, 30, 60, 60))

#Displaying the window
    pygame.display.flip()