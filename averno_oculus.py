import viz, vizconnect, vizact, vizinfo, vizjoy, vizproximity, oculus

viz.window.setName('AVERNO')
#viz.window.setBorder(viz.BORDER_FIXED)
#viz.go()
vizconnect.go('configOculus.py')

model = {
	'mundo1' : "models/AbernoD.obj",
	'mundo2' : "models/AbernoL04.obj",
	'mundo3' : "models/AbernoD.obj",
	'mundo4' : "models/AbernoL04.obj"
}

item = {
	'gem' : "ball.wrl"
}

image = {
	'portada' : "img/Portada_Averno_1024.jpg"
}

button = {
	'portada_A' : "img/button_up_Dojo.png",
	'portada_B' : "img/button_down_Dojo.png"
}

sound = {
	'chime' : "sound/chime.wav",
	'elevator' : "sound/elevator.wav"
}

collide = True
speed = 0.125
isActive = [True, False, False, False, False, False, False]

def setInitialPosition():
	toogleCollide(False)
	viz.MainView.setPosition(-62,0,8)
	viz.MainView.setEuler(0,0,0)
	toogleCollide(True)

def accionbuttonNewGame():
	print "Mundo1"
	isActive[1] = True
	isActive[2] = False
	isActive[3] = False
	isActive[4] = False
	isActive[6] = False
	#manager.addSensor(sensor)
	viz.scene(viz.Scene1)
	setInitialPosition()

def toogleCollide(flag):
	global collude
	if flag == True and collide == True:
		viz.MainView.collision(viz.ON)
	else:
		viz.MainView.collision(viz.OFF)

def returntoMenu():
	print "MenuPrincipal"
	isActive[1] = False
	isActive[2] = False
	isActive[3] = False
	isActive[6] = True
	viz.scene(viz.Scene6)
	viz.MainWindow.stereo(viz.OFF)

def UpdateMovement():
    pos = joy.getPosition()
    twist = joy.getTwist()
    viz.MainView.setAxisAngle(0,1,0,twist*viz.elapsed()*35,viz.BODY_ORI,viz.REL_PARENT)
    viz.MainView.move([pos[0]*viz.elapsed()*5,0,-pos[1]*viz.elapsed()*5])

def EnterRock(e):    
	info.setPanelVisible(True)
	chime_sound.play()

#vizact.ontimer(0,UpdateMovement)

current_scene = 0

#################################################################
#################################################################

#Escenario1
mine = viz.addChild(model['mundo1'], scene = viz.Scene1)
gem = viz.addChild(item['gem'], scene = viz.Scene1)
gem.setScale(2.5,2.5,2.5)
gem.setPosition(10,5)
btn_regresa = viz.addButtonLabel("regresar", scene = viz.Scene1)
btn_regresa.setPosition(0.9,0.1)

rock = viz.addChild(item['gem'], scene = viz.Scene1)
rock.setScale(2.5,2.5,2.5)
rock.setPosition(-30,4)

canvas = viz.addGUICanvas()
canvas.alignment(viz.ALIGN_CENTER)
viz.MainWindow.setDefaultGUICanvas(canvas)
info = vizinfo.InfoPanel('AVERNO', align=viz.ALIGN_RIGHT_TOP, icon=False)
info.setTitle( 'Ejemplo' )
info.setPanelVisible(False)
#canvas.setRenderWorldOverlay([600,500],50,3)
canvas.setRenderWorld([600,500],[3,viz.AUTO_COMPUTE])
canvas.setPosition([-30,5,2])
canvas.setEuler(0,0,0)

vizact.onbuttonup(btn_regresa, returntoMenu)

#################################################################
#################################################################

#Escenario2
mine2 = viz.addChild(model['mundo2'], scene = viz.Scene2)
gem2 = viz.addChild(item['gem'], scene = viz.Scene2)
gem2.setScale(2.5,2.5,2.5)
gem2.setPosition(10,5)
btn_regresa2 = viz.addButtonLabel("regresar", scene = viz.Scene2)
btn_regresa2.setPosition(0.9,0.1)

vizact.onbuttonup(btn_regresa2, returntoMenu)

#################################################################
#################################################################

#Escenario3
mine3 = viz.addChild(model['mundo3'], scene = viz.Scene3)
gem3 = viz.addChild(item['gem'], scene = viz.Scene3)
gem3.setScale(2.5,2.5,2.5)
gem3.setPosition(10,5)
btn_regresa3 = viz.addButtonLabel("regresar", scene = viz.Scene3)
btn_regresa3.setPosition(0.9,0.1)

vizact.onbuttonup(btn_regresa3, returntoMenu)

#################################################################
#################################################################

#Escenario4
mine4 = viz.addChild(model['mundo3'], scene = viz.Scene4)
gem4 = viz.addChild(item['gem'], scene = viz.Scene4)
gem4.setScale(2.5,2.5,2.5)
gem4.setPosition(10,5)
btn_regresa4 = viz.addButtonLabel("regresar", scene = viz.Scene4)
btn_regresa4.setPosition(0.9,0.1)

vizact.onbuttonup(btn_regresa4, returntoMenu)

#################################################################
#################################################################

#Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(viz.ON)

#Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

sensorRock = vizproximity.addBoundingBoxSensor(rock,scale=[6,4,6])
manager.addSensor(sensorRock)

#sensor = vizproximity.addBoundingSphereSensor(lamp,scale=2)
#sensor = vizproximity.Sensor( vizproximity.RectangleArea([2,2],center=[lamp.getPosition(0)[0],0]), None )
#sensor = vizproximity.Sensor( vizproximity.RectangleArea([2,10],center=[gem.getPosition(0)[0],0]), None )
#sensor2 = vizproximity.Sensor( vizproximity.RectangleArea([2,10],center=[gem2.getPosition(0)[0],0]), None )
#sensor3 = vizproximity.Sensor( vizproximity.RectangleArea([2,10],center=[gem3.getPosition(0)[0],0]), None )
#sensor4 = vizproximity.Sensor( vizproximity.RectangleArea([2,10],center=[gem4.getPosition(0)[0],0]), None )
#manager.removeSensor(sensor)
'''
manager.onEnter(sensor,EnterProximity)
manager.onExit(sensor,ExitProximity)
manager.onEnter(sensor2,EnterProximity)
manager.onExit(sensor2,ExitProximity)
manager.onEnter(sensor3,EnterProximity)
manager.onExit(sensor3,ExitProximity)
manager.onEnter(sensor4,EnterProximity)
manager.onExit(sensor4,ExitProximity)
'''
manager.onEnter(sensorRock,EnterRock)
#manager.onExit(sensorRock,ExitRock)

#vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

#Menu principal
bgTexture = viz.add(image['portada'])
quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = viz.Scene6)
quad_bgtexture.texture(bgTexture)
quad_bgtexture.setScale(12.8,10.24,0) #Escala a pantalla completa
quad_bgtexture.setPosition(0.5, 0.5) #Centro de pantalla
viz.scene(viz.Scene6) #Mostrar menú principal
isActive[6] = True

#Botones de interaccion
btn_newGame = viz.addButton(scene = viz.Scene6)
btn_newGame.setPosition(0.75,0.75)
btn_newGame.setScale(8,2.3)
btn_newGame.downpicture(button['portada_B'])
btn_newGame.uppicture(button['portada_A'])

#Botones de interaccion
btn_credits = viz.addButton(scene = viz.Scene6)
btn_credits.setPosition(0.75,0.60)
btn_credits.setScale(8,2.3)
btn_credits.downpicture(button['portada_B'])
btn_credits.uppicture(button['portada_A'])
	
vizact.onbuttonup(btn_newGame, accionbuttonNewGame)

chime_sound = viz.addAudio(sound['chime'])

viz.MainView.eyeheight(4.75)
#viz.MainView.setPosition(-65,5,8)
toogleCollide(True)

#joy = vizjoy.add()

print "MenuPrincipal"

accionbuttonNewGame()

#vizact.ontimer(0,UpdateJoystick)
'''
# Setup Oculus Rift HMD
hmd = oculus.Rift()
if not hmd.getSensor():
	sys.exit('Oculus Rift not detected')

# Go fullscreen if HMD is in desktop display mode
if hmd.getSensor().getDisplayMode() == oculus.DISPLAY_DESKTOP:
	viz.window.setFullscreen(True)
	
# Setup navigation node and link to main view
viz.link(hmd.getSensor(), viz.MainView)
'''
'''
# Setup Oculus Rift HMD
hmd = oculus.Rift()
if not hmd.getSensor():
	sys.exit('Oculus Rift not detected')

# Go fullscreen if HMD is in desktop display mode
if hmd.getSensor().getDisplayMode() == oculus.DISPLAY_DESKTOP:
	viz.window.setFullscreen(True)

# Key commands
KEYS = { 'forward'	: viz.KEY_UP
		,'back' 	: viz.KEY_DOWN
		,'left' 	: viz.KEY_LEFT
		,'right'	: viz.KEY_RIGHT
		,'reset'	: 'r'
		,'camera'	: 'c'
		,'help'		: ' '
}

# Setup heading reset key
vizact.onkeydown(KEYS['reset'], hmd.getSensor().reset)

# Setup navigation node and link to main view
navigationNode = viz.addGroup()
viewLink = viz.link(navigationNode, viz.MainView)
viewLink.preMultLinkable(hmd.getSensor())

MOVE_SPEED = 2.0
def UpdateView():
	yaw,pitch,roll = viewLink.getEuler()
	m = viz.Matrix.euler(yaw,0,0)
	dm = viz.getFrameElapsed() * MOVE_SPEED
	if viz.key.isDown(KEYS['forward']):
		m.preTrans([0,0,dm])
	if viz.key.isDown(KEYS['back']):
		m.preTrans([0,0,-dm])
	if viz.key.isDown(KEYS['left']):
		m.preTrans([-dm,0,0])
	if viz.key.isDown(KEYS['right']):
		m.preTrans([dm,0,0])
	navigationNode.setPosition(m.getPosition(), viz.REL_PARENT)
vizact.ontimer(0,UpdateView)
'''