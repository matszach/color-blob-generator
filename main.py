from PIL import Image, ImageDraw
import numpy as np
from random import randint, choice

NOF_NODES = 5000
UNIT = 5
IMG_SIZE = 100

nodes = [(int(IMG_SIZE/2), int(IMG_SIZE/2))]

while len(nodes) < NOF_NODES:
	n = choice(nodes)
	dir = randint(0, 3)
	if dir == 0: 
		m = n[0] - 1,  n[1]
	elif dir == 1: 
		m = n[0] + 1,  n[1]
	elif dir == 2: 
		m = n[0],  n[1] - 1
	else:
		m = n[0],  n[1] + 1
		
	if m not in nodes:
		nodes.append(m)
		
print(nodes)
	
	
img = Image.new('RGB', (int(IMG_SIZE * UNIT), int(IMG_SIZE * UNIT)), (200, 200, 200))
draw = ImageDraw.Draw(img)


for i, n in enumerate(nodes):
	col = (0, 0, int(100 + i/NOF_NODES * 150))
	draw.rectangle((n[0] * UNIT, n[1] * UNIT, n[0] * UNIT + UNIT, n[1] * UNIT + UNIT), fill=col)
	
img.save('out.png')