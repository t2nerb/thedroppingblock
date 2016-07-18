import pygame,time,random

pygame.init()

disp_width = 800
disp_height = 600

car_width = 37
car_height = 90

black = ((0,0,0))
white = ((255,255,255))
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((disp_width,disp_height))
pygame.display.set_caption('Don\'t ask wtf this is')
clock = pygame.time.Clock()

carImg = pygame.image.load('Images.png')

def obstacles(obs_x, obs_y, obs_width, obs_height, color):
	pygame.draw.rect(gameDisplay, color, [obs_x, obs_y, obs_width, obs_height])

def car(x,y):
	gameDisplay.blit(carImg, (x,y))

def text_objects(text, info):
	textSurface = info.render(text,True,red)
	return textSurface, textSurface.get_rect()

def message_display(text):
	size = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects(text, size)
	TextRect.center = ((disp_width/2),(disp_height/2))
	gameDisplay.blit(TextSurf, TextRect)
	pygame.display.update()

def crash():
	message_display('CRASHED!!!')



def gameloop():
	x = (disp_width * 0.5)
	y = (disp_height * 0.8)
	car_xleft = 0
	car_xright = 0

	obs_xcoord = random.randrange(0,disp_width)
	obs_ycoord = -500
	obs_speed = 10
	obs_width = 40
	obs_height = 80
	

	alive = True 
	while alive:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				alive = False 
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					car_xleft -= 30 
				elif event.key == pygame.K_RIGHT:
					car_xright += 30 
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					car_xleft = 0
				if event.key == pygame.K_RIGHT:
					car_xright = 0

		car_xdisp = car_xleft + car_xright
		if (x + car_xdisp) < (disp_width-37) and (x + car_xdisp) > 0:
			x += car_xdisp
			
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				crash()
				time.sleep(3)
				alive = False

		gameDisplay.fill(white)

		#def obstacles(obs1, obs2, obs_width, obs_height, color):
		obstacles(obs_xcoord, obs_ycoord, obs_width, obs_height, black)
		obs_ycoord += obs_speed
		car(x,y)
		if obs_ycoord > disp_height:
			obs_ycoord = 0 - obs_height
			obs_xcoord = random.randrange(0,disp_width)
		
		pygame.display.update()
		clock.tick(120)
gameloop()
pygame.quit()
quit()
	

