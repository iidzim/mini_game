import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

pygame.init()

#! Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#! color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

running = True
while running:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

	# Fill the screen with white
	screen.fill(white)
	# Create a surface and pass in a tuple containing its length and width
	surf = pygame.Surface((50, 50))
	# Give the surface a color to separate it from the background
	surf.fill(black)
	rect = surf.get_rect()
	surf_center = ((SCREEN_WIDTH - surf.get_width()) / 2, (SCREEN_HEIGHT - surf.get_height()) / 2 )
	screen.blit(surf, surf_center) #! blit() is how you copy the contents of one Surface to another
	pygame.display.flip() #! get your newly created Surface to display on the screen



	pygame.display.flip()

pygame.quit()


#? display.flip() will update the contents of the entire display
#? display.update() allows to update a portion of the screen, instead of the entire area of the screen.
#? Passing no arguments, updates the entire display

	# # pygame.draw.circle(screen, red, (250, 250), 50)
	# pygame.draw.circle(screen, red, (250, 250), 50, 2, True, False, True, False)
	# # rect1 = pygame.rect(200, 200, 75, 45)
	# pygame.draw.rect(screen, black, pygame.Rect(210, 230, 90, 40))