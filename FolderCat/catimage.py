
# cat moving around

import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60 #frames per second
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('Cat moves')

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catx = 10
caty = 10
direction = 'right'

while True: # the main game loop
	DISPLAYSURF.fill(WHITE)
	
	
	
	DISPLAYSURF.blit(catImg, (catx, caty))
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
    
	keys=pygame.key.get_pressed()
	if keys[K_RIGHT]: 
		catx += 5
	if keys[K_LEFT]: 
		catx -= 5
	if keys[K_DOWN]: 
		caty += 5
	if keys[K_UP]: 
		caty -= 5    	
		
	pygame.display.update()
	fpsClock.tick(FPS)