import viz, vizact, vizinfo, vizproximity
from gem import Gem
from plane import Plane

class ModelScene:
	
	def __init__(self, model, escena, gems, gemspos, gemcount, planes, planespos, nextScene, gemsound, planesound):
		self.mine = viz.addChild(model, scene = escena)
		
		self.planeList = list()
		contpos = 0
		
		for x in planes:
			planeitem = Plane(x, planespos[contpos], escena, nextScene[contpos], planesound)
			self.planeList.append(planeitem)
			contpos = contpos + 1
		
		self.btn_regresa = viz.addButtonLabel("regresar", scene = escena)
		self.btn_regresa.setPosition(0.9,0.1)
		
		self.gemList = list()
		contpos = 0
		
		print escena
		for x in gems:
			gemitem = Gem(x, gemspos[contpos], escena, gemsound)
			self.gemList.append(gemitem)
			contpos = contpos + 1
		
	def getGemList(self):
		return self.gemList
		
	def getGemSensorList(self):
		sensorList = list()
		for x in self.gemList:
			sensorList.append(x.getSensorGem())
		return sensorList
	
	def enterGem(self, e):
		sensorList = list()
		#print "MANAGER", manager
		for x in self.gemList:
			if x.getSensorGem() == e.sensor:				
				x.setInfoPanelTrue()
				
	def getPlaneList(self):
		return self.planeList
		
	def getPlaneSensorList(self):
		sensorList = list()
		for x in self.planeList:
			sensorList.append(x.getSensorPlane())
		return sensorList
		
	def enterPlane(self, e, manager):
		sensorList = list()
		for x in self.planeList:
			if x.getSensorPlane() == e.sensor:
				#x.setInfoPanelTrue()
				print e.sensor
	
	def getReturnButton(self):
		return self.btn_regresa