import pygame, sys
from pygame.locals import *
import colorsys

# per default: 500 pixels = 1 unit


iter_no = 100


def ValToColor(min, max, value):
	# converts a value in a range from min to max to a color with variable hue 

	delta = max - min

	step = float(1 / delta)

	hue = step * float((value - min))

	try:
		rgb = colorsys.hsv_to_rgb(hue, 0.75, 0.75)
		r = round(rgb[0] * 255)
		g = round(rgb[1] * 255)
		b = round(rgb[2] * 255)
		color = (r, g, b)
		return color
	except:
		color = (0,0,0)
		return(color)



########################
#  USER INPUT RESOLUTION
########################

choice = input("Do you wish to specify custom resolution (y/n)? ")
if choice == 'y' or choice == 'Y':
	x_in = input("X resolution: ")
	y_in = input("Y resolution: ")

	try:
		x_res = int(x_in)
		y_res = int(y_in)
	except:
		print("Error, defaulting to 1500 x 1000")
		x_res = 1500
		y_res = 1000

else:
	x_res = 1500
	y_res = 1000

######################
# MANDEL START
######################

pygame.init()
ds = pygame.display.set_mode((x_res,y_res))
pygame.display.set_caption("Mandelbrot Set")

blue = (142, 202, 230)
black = (2, 48, 71)

# DRAW BACKGROUND
ds.fill(blue)
font = pygame.font.SysFont(None, 60)
img = font.render("Loading...", False, black)
ds.blit(img, (x_res / 2, y_res / 2))



# for every pixel there exists
for y in range(0, y_res):
	for x in range(0, x_res):
		c = complex(((x / (x_res / 3)) - 2.0), ((y_res / 2) - y) / (y_res / 2))

		z = complex(0,0)
		for i in range(0,iter_no):
			z = z*z + c
			if abs(z) > 1000:
				pix_col = ValToColor(0, iter_no, i)
				#print("diverges at iteration " + str(i) + ", color: " + str(pix_col))
				ds.set_at((x,y), pix_col)
				break

		if abs(z) < 2.0:
			ds.set_at((x,y), black)
		elif (abs(z) >= 2.0 and abs(z) <= 1000):
			pix_col = ValToColor(0,iter_no,0)
			ds.set_at((x,y), pix_col)

	pygame.display.update()


while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
