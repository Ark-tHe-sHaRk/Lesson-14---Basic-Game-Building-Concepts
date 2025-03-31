#Importing the nessesary libraries
import pygame

#Importing the pygame module
pygame.init()

#Setting the dimesions of the window
screen = pygame.display.set_mode((300, 300))
done = False

#Setting the title of window
pygame.display.set_caption("Drawing Hollow and Solid Ball")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #Drawing a hollow circle
    pygame.draw.circle(screen, (0, 125, 225), (150, 150), 50, 1)
    #Drawing a solid circle
    pygame.draw.circle(screen, (0, 255, 0), (150, 150), 25, 0)

    #Displaying the window
    pygame.display.flip()
    #Filling the screen with white color
    screen.fill((255, 255, 255))
    