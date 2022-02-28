from cProfile import run
from errno import ENETDOWN
import random
import pygame
from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT, RLEACCEL)

# color
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# # Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
	def __init__(self):
		super(Player, self).__init__()
		#boring white rectangles
		# self.surf = pygame.Surface((75, 25))
		# self.surf.fill(white)
		self.surf = pygame.image.load("Run (7).png").convert()
		#? The RLEACCEL constant is an optional parameter that helps pygame render
		#? more quickly on non-accelerated displays.
		self.surf.set_colorkey(white, RLEACCEL)
		self.rect = self.surf.get_rect()

	def update(self, pressed_keys):
		if pressed_keys[K_UP]:
			self.rect.move_ip(0, -5)
		if pressed_keys[K_DOWN]:
			self.rect.move_ip(0, 5)
		if pressed_keys[K_LEFT]:
			self.rect.move_ip(-5, 0)
		if pressed_keys[K_RIGHT]:
			self.rect.move_ip(5, 0)

		# Keep player on the screen
		if self.rect.left < 0:
			self.rect.left = 0
		if self.rect.right > SCREEN_WIDTH:
			self.rect.right = SCREEN_WIDTH
		if self.rect.top <= 0:
			self.rect.top = 0
		if self.rect.bottom >= SCREEN_HEIGHT:
			self.rect.bottom = SCREEN_HEIGHT

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super(Enemy, self).__init__()
		# self.surf = pygame.Surface((20, 10))
		# self.surf.fill((255, 255, 255))
		self.surf = pygame.image.load("Gantu.png").convert()
		self.surf.set_colorkey(white, RLEACCEL)
		self.rect = self.surf.get_rect(
			center=(
				random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
				random.randint(0, SCREEN_HEIGHT),
			)
		)
		self.speed = random.randint(5, 20)

	# Move the sprite based on speed
	# Remove the sprite when it passes the left edge of the screen
	def update(self):
		self.rect.move_ip(-self.speed, 0)
		if self.rect.right < 0:
			self.kill()

class Palm(pygame.sprite.Sprite):
	def __init__(self):
		super(Palm, self).__init__()
		self.surf = pygame.image.load("palm.png").convert()
		self.surf.set_colorkey(black, RLEACCEL)
		# The starting position is randomly generated
		self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
    # Move the Palm based on a constant speed
    # Remove the Palm when it passes the left edge of the screen
	def update(self):
		self.rect.move_ip(-5, 0)
		if self.rect.right < 0:
			self.kill()


pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
pygame.display.set_caption("Collision Detection Game")

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDPALM = pygame.USEREVENT + 2
pygame.time.set_timer(ADDPALM, 1000)


# Instantiate player. Right now, this is just a rectangle.
player = Player()

enemies = pygame.sprite.Group()
palms = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)


running = True
while running:

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
		# add new enemy
		elif event.type == ADDENEMY:
			# create the new enemy and add it to sprite groups
			new_enemy = Enemy()
			enemies.add(new_enemy)
			all_sprites.add(new_enemy)
		elif event.type == ADDPALM:
			new_palm = Palm()
			palms.add(new_palm)
			all_sprites.add(new_palm)

	# Get all the keys currently pressed
	pressed_keys = pygame.key.get_pressed()
	# Update the player sprite based on user keypresses
	player.update(pressed_keys)

	#update enemy position
	enemies.update()
	palms.update()

	# Fill the screen with white
	# screen.fill(black)
	screen.fill((135, 206, 250))
	# # Create a surface and pass in a tuple containing its length and width
	# surf = pygame.Surface((50, 50))
	# # Give the surface a color to separate it from the background
	# surf.fill(black)
	# rect = surf.get_rect()
	# surf_center = ((SCREEN_WIDTH - surf.get_width()) / 2, (SCREEN_HEIGHT - surf.get_height()) / 2 )
	# screen.blit(surf, surf_center) # blit() is how you copy the contents of one Surface to another
	
	# Draw the player on the screen
	# screen.blit(player.surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
	# screen.blit(player.surf, player.rect)
	# Draw all sprites
	for entity in all_sprites:
		screen.blit(entity.surf, entity.rect)

	if pygame.sprite.spritecollideany(player, enemies):
		player.kill()
		running = False
	# Update the display
	pygame.display.flip() # get your newly created Surface to display on the screen

	# Ensure program maintains a rate of 30 frames per second
	clock.tick(30)

	# pygame.display.flip()

pygame.quit()


#? display.flip() will update the contents of the entire display
#? display.update() allows to update a portion of the screen, instead of the entire area of the screen.
#? Passing no arguments, updates the entire display

	# # pygame.draw.circle(screen, red, (250, 250), 50)
	# pygame.draw.circle(screen, red, (250, 250), 50, 2, True, False, True, False)
	# # rect1 = pygame.rect(200, 200, 75, 45)
	# pygame.draw.rect(screen, black, pygame.Rect(210, 230, 90, 40))