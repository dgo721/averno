import viz, vizact, vizinfo, vizproximity

class Gem:
	def __init__(self, gem, gempos, escena, sound):
		print "ESCENA-2", escena
		self.gem = viz.addChild(gem, scene = escena)
		self.gem.setScale(2.5,2.5,2.5)
		self.gem.setPosition(gempos[0],gempos[1])
		self.sensorGem = vizproximity.addBoundingBoxSensor(self.gem,scale=[6,4,6])
		self.chimesound = sound
		self.canvas = viz.addGUICanvas()
		self.canvas.alignment(viz.ALIGN_CENTER)
		viz.MainWindow.setDefaultGUICanvas(self.canvas)
		self.info = vizinfo.InfoPanel('AVERNO', align=viz.ALIGN_RIGHT_TOP, icon=False)
		self.info.setTitle( 'Ejemplo' )
		self.info.setPanelVisible(False)
		self.canvas.setRenderWorld([600,500],[3,viz.AUTO_COMPUTE])
		self.canvas.setPosition([self.gem.getPosition()[0],self.gem.getPosition()[1]+0.5,self.gem.getPosition()[2]])
		self.canvas.setEuler(0,0,0)
		
	def setInfoPanelTrue(self):		
		self.chimesound.play()
		print self.info
		self.info.setPanelVisible(True)
		
	def getSensorGem(self):
		return self.sensorGem