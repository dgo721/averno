import viz, vizact, vizproximity

class Plane:
	def __init__(self, plane, planepos, escena, next, sound):
		self.plane = viz.addChild(plane, scene = escena)
		self.plane.setScale(2.5,2.5,2.5)
		self.plane.setPosition(planepos[0],planepos[1])
		self.sensorPlane = vizproximity.Sensor(vizproximity.RectangleArea([2,10],center=[self.plane.getPosition(0)[0],0]), None)
		self.chimesound = sound
		self.next = next
		#self.plane.visible(False)
		
	def getSensorPlane(self):
		return self.sensorPlane
		
	def getNextScene(self):
		return self.next