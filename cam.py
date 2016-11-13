from SimpleCV import *
from cue_sdk import *
from msvcrt import getch

class Screen(object):
	def __init__(self, controller, corners):
		self.grid = []
		self.controller = controller

		for corner in corners:
			for i in xrange(corner[0], corner[1]+1):
				self.grid.append(i)	

Corsair = CUESDK("CUESDK_2015.dll")
Corsair.RequestControl(CAM.ExclusiveLightingControl)

corners = [(14, 23), (51, 60), (38, 47), (26, 35)]
board = Screen(Corsair, corners)

cam = Camera(prop_set={"width":1000,"height":400})
disp = Display()

while disp.isNotDone():
	if disp.mouseRight:break
	if disp.mouseLeft:
		img = cam.getImage()
		np = img.getNumpy()

		pixNum = 0;
		grid = board.grid
		for i in xrange(4):
			for j in xrange(10):
				avgR=0; avgG=0; avgB=0
				for xStep in xrange(i*96, (i+1)*96):
					for yStep in xrange(i*135, (i+1)*135):
						avgR += np[xStep][yStep][0]
						avgG += np[xStep][yStep][1]
						avgB += np[xStep][yStep][2]
				Corsair.SetLedsColors(CorsairLedColor(grid[pixNum], avgR/12960, avgG/12960, avgB/12960))
				pixNum += 1
		img.show()
			