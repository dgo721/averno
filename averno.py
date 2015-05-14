import viz, vizconnect, vizact, vizinfo, vizproximity, vizjoy

viz.window.setName('AVERNO')
viz.window.setPosition(300,50)

model = {
	'mundo1' : "models/s1/minasec1.obj",
	'mundo2' : "models/s5/Seccion05S.obj",
	'mundo3' : "models/s6/seccion6.obj",
	'mundo4' : "models/Seccion08.obj",
	'mundo5' : "models/s14/Seccion14.obj"
}

item = {
	'gem1' : "box.wrl",
	'gem2' : "box.wrl",
	'gem3' : "models/hierro.obj",
	'gem4' : "models/oro.obj",
	'gem' : "ball.wrl"
}

image = {
	'portada' : "img/Portada_Averno_1024.jpg",
	'nombre' : "img/portada_nombre.png",
	'controles' : "img/controles.jpg",
	'daniel' : "img/daniel.jpg",
	'conant' : "img/conant.jpg",
	'pau' : "img/pau.jpg",
	'diego' : "img/diego.jpg",
	'estanio' : "img/estanio.jpg",
	'hierro' : "img/hierro.jpg",
	'niquel' : "img/niquel.jpg",
	'oro' : "img/oro.jpg"
}

button = {
	'portada_A' : "img/btn_iniciar.jpg",
	'portada_B' : "img/btn_controles.jpg",
	'portada_C' : "img/btn_creditos.jpg",
	'regresar' : "img/btn_regresar.jpg"
}

sound = {
	'chime' : "sound/chime.wav",
	'elevator' : "sound/elevator.wav",
	'deslave' : "sound/deslave.wav",
	'hammer' : "sound/hammer.wav",
	'hammer' : "sound/hammer.wav",
	'dirt' : "sound/dirt.wav",
	'cave' : "sound/cave.wav"
}

ar = viz.add("artoolkit.dle")
collide = True
isActive = [True, False, False, False, False, False, False]
sceneControls = viz.addScene()
sceneDaniel = viz.addScene()
sceneConant = viz.addScene()
scenePau = viz.addScene()
sceneDiego = viz.addScene()

def Diego():
	#Menu principal
	global current_scene
	current_scene = 5
	bgTexture = viz.add(image['diego'])
	quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = sceneDiego)
	quad_bgtexture.texture(bgTexture)
	quad_bgtexture.setScale(12.8,10.24,0)
	quad_bgtexture.setPosition(0.5, 0.5)
	viz.scene(sceneDiego)
	
	#Botones de interaccion
	btn_atras= viz.addButton(scene = sceneDiego)
	btn_atras.setPosition(0.60,0.05)
	btn_atras.setScale(7,1.6)
	btn_atras.downpicture(button['regresar'])
	btn_atras.uppicture(button['regresar'])
	
	#Botones de interaccion
	btn_sig = viz.addButton(scene = sceneDiego)
	btn_sig.setPosition(0.87,0.05)
	btn_sig.setScale(7,1.6)
	btn_sig.downpicture(button['portada_A'])
	btn_sig.uppicture(button['portada_A'])
	
	vizact.onbuttonup(btn_atras, Pau)
	vizact.onbuttonup(btn_sig, MainMenu)

def Pau():
	#Menu principal
	global current_scene
	current_scene = 4
	bgTexture = viz.add(image['pau'])
	quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = scenePau)
	quad_bgtexture.texture(bgTexture)
	quad_bgtexture.setScale(12.8,10.24,0)
	quad_bgtexture.setPosition(0.5, 0.5)
	viz.scene(scenePau)
	
	#Botones de interaccion
	btn_atras= viz.addButton(scene = scenePau)
	btn_atras.setPosition(0.60,0.05)
	btn_atras.setScale(7,1.6)
	btn_atras.downpicture(button['regresar'])
	btn_atras.uppicture(button['regresar'])
	
	#Botones de interaccion
	btn_sig = viz.addButton(scene = scenePau)
	btn_sig.setPosition(0.87,0.05)
	btn_sig.setScale(7,1.6)
	btn_sig.downpicture(button['portada_A'])
	btn_sig.uppicture(button['portada_A'])
	
	vizact.onbuttonup(btn_atras, Conant)
	vizact.onbuttonup(btn_sig, Diego)

def Conant():
	#Menu principal
	global current_scene
	current_scene = 3
	bgTexture = viz.add(image['conant'])
	quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = sceneConant)
	quad_bgtexture.texture(bgTexture)
	quad_bgtexture.setScale(12.8,10.24,0)
	quad_bgtexture.setPosition(0.5, 0.5)
	viz.scene(sceneConant)
	
	#Botones de interaccion
	btn_atras= viz.addButton(scene = sceneConant)
	btn_atras.setPosition(0.60,0.05)
	btn_atras.setScale(7,1.6)
	btn_atras.downpicture(button['regresar'])
	btn_atras.uppicture(button['regresar'])
	
	#Botones de interaccion
	btn_sig = viz.addButton(scene = sceneConant)
	btn_sig.setPosition(0.87,0.05)
	btn_sig.setScale(7,1.6)
	btn_sig.downpicture(button['portada_A'])
	btn_sig.uppicture(button['portada_A'])
	
	vizact.onbuttonup(btn_atras, Daniel)
	vizact.onbuttonup(btn_sig, Pau)

def Daniel():
	#Menu principal
	global current_scene
	current_scene = 2
	bgTexture = viz.add(image['daniel'])
	quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = sceneDaniel)
	quad_bgtexture.texture(bgTexture)
	quad_bgtexture.setScale(12.8,10.24,0)
	quad_bgtexture.setPosition(0.5, 0.5)
	viz.scene(sceneDaniel)
	
	#Botones de interaccion
	btn_atras= viz.addButton(scene = sceneDaniel)
	btn_atras.setPosition(0.60,0.05)
	btn_atras.setScale(7,1.6)
	btn_atras.downpicture(button['regresar'])
	btn_atras.uppicture(button['regresar'])
	
	#Botones de interaccion
	btn_sig = viz.addButton(scene = sceneDaniel)
	btn_sig.setPosition(0.87,0.05)
	btn_sig.setScale(7,1.6)
	btn_sig.downpicture(button['portada_A'])
	btn_sig.uppicture(button['portada_A'])
	
	vizact.onbuttonup(btn_atras, MainMenu)
	vizact.onbuttonup(btn_sig, Conant)
	
def Controls():
	#Menu principal
	global current_scene
	current_scene = 1
	bgTexture = viz.add(image['controles'])
	quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = sceneControls)
	quad_bgtexture.texture(bgTexture)
	quad_bgtexture.setScale(12.8,10.24,0)
	quad_bgtexture.setPosition(0.5, 0.5)
	viz.scene(sceneControls)
	
	#Botones de interaccion
	btn_atras= viz.addButton(scene = sceneControls)
	btn_atras.setPosition(0.85,0.05)
	btn_atras.setScale(7,1.6)
	btn_atras.downpicture(button['regresar'])
	btn_atras.uppicture(button['regresar'])
	
	vizact.onbuttonup(btn_atras, MainMenu)

def MainMenu():
	#Menu principal
	global current_scene
	current_scene = 0
	isActive[6] = True
	bgTexture = viz.add(image['portada'])
	quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = viz.Scene6)
	quad_bgtexture.texture(bgTexture)
	quad_bgtexture.setScale(12.8,10.24,0)
	quad_bgtexture.setPosition(0.5, 0.5)
	viz.scene(viz.Scene6)
	
	#Botones de interaccion
	btn_juego = viz.addButton(scene = viz.Scene6)
	btn_juego.setPosition(0.75,0.50)
	btn_juego.setScale(8,2.3)
	btn_juego.downpicture(button['portada_A'])
	btn_juego.uppicture(button['portada_A'])
	
	#Botones de interaccion
	btn_controles= viz.addButton(scene = viz.Scene6)
	btn_controles.setPosition(0.75,0.35)
	btn_controles.setScale(8,2.3)
	btn_controles.downpicture(button['portada_B'])
	btn_controles.uppicture(button['portada_B'])
	
	#Botones de interaccion
	btn_creditos = viz.addButton(scene = viz.Scene6)
	btn_creditos.setPosition(0.75,0.20)
	btn_creditos.setScale(8,2.3)
	btn_creditos.downpicture(button['portada_C'])
	btn_creditos.uppicture(button['portada_C'])
	
	vizact.onbuttonup(btn_juego, accionbuttonNewGame)
	vizact.onbuttonup(btn_controles, Controls)
	vizact.onbuttonup(btn_creditos, Daniel)

def setInitialPosition(pos):
	toogleCollide(False)
	viz.MainView.setPosition(pos)
	viz.MainView.setEuler(0,0,0)
	toogleCollide(True)

def accionbuttonNewGame():
	print "Mundo1"
	global current_scene
	current_scene = 6
	isActive[1] = True
	isActive[2] = False
	isActive[3] = False
	isActive[4] = False
	isActive[6] = False
	viz.scene(viz.Scene1)
	setInitialPosition([0,5,0])
	#viz.scene(viz.Scene5)
	#setInitialPosition([218.66688537597656, 5.440362930297852, -89.66780090332031])
	#viz.scene(viz.Scene3)
	#setInitialPosition([130.56468200683594, 5.395919322967529, -30.007774353027344])

def toogleCollide(flag):
	if flag == True and collide == True:
		viz.MainView.collision(viz.ON)
	else:
		viz.MainView.collision(viz.OFF)

def EnterProximity(e):
	if e.sensor == sensorPlane1 and isActive[1] == True:
		print "A Mundo 2"
		isActive[1] = False
		isActive[2] = True
		isActive[3] = False
		isActive[4] = False
		isActive[5] = False
		isActive[6] = False
		elevator_sound.play()
		viz.scene(viz.Scene2)
		setInitialPosition([56.738, 5.44, -3.70])
	elif e.sensor == sensorPlane2 and isActive[2] == True:
		print "A Mundo 3"
		isActive[1] = False
		isActive[2] = False
		isActive[3] = True
		isActive[4] = False
		isActive[5] = False
		isActive[6] = False
		explosion_sound.play()
		viz.scene(viz.Scene3)
		setInitialPosition([130.565, 5.40, -30])
	elif e.sensor == sensorPlane3 and isActive[3] == True:
		print "A Mundo 4"
		isActive[1] = False
		isActive[2] = False
		isActive[3] = False
		isActive[4] = True
		isActive[5] = False
		isActive[6] = False
		cave_sound.play()
		viz.scene(viz.Scene4)
		setInitialPosition([276.37, 5.34, 26.81])
	elif e.sensor == sensorPlane4 and isActive[4] == True:
		print "A Mundo 5"
		isActive[1] = False
		isActive[2] = False
		isActive[3] = False
		isActive[4] = False
		isActive[5] = True
		isActive[6] = False
		dirt_sound.play()
		viz.scene(viz.Scene5)
		setInitialPosition([218.67, 5.44, -89.67])
	elif e.sensor == sensorPlane5 and isActive[5] == True:
		print "A menu principal"
		isActive[1] = False
		isActive[2] = False
		isActive[3] = False
		isActive[4] = False
		isActive[5] = False
		isActive[6] = True
		viz.MainWindow.stereo(viz.OFF)
		MainMenu()

def ExitProximity(e):
    print "De vuelta", e.sensor

def enterGem(e):    
	if e.sensor == sensorGem31:
		ETsubWindow.visible(True)
	elif e.sensor == sensorGem51:
		NQsubWindow.visible(True)
	elif e.sensor == sensorGem52:
		HRsubWindow.visible(True)
	elif e.sensor == sensorGem53:
		OROsubWindow.visible(True)
	chime_sound.play()
	
def exitGem(e):    
	if e.sensor == sensorGem31:
		ETsubWindow.visible(False)
	elif e.sensor == sensorGem51:
		NQsubWindow.visible(False)
	elif e.sensor == sensorGem52:
		HRsubWindow.visible(False)
	elif e.sensor == sensorGem53:
		OROsubWindow.visible(False)

def returntoMenu():
	print "MenuPrincipal"
	isActive[1] = False
	isActive[2] = False
	isActive[3] = False
	isActive[4] = False
	isActive[5] = False
	isActive[6] = True
	viz.MainWindow.stereo(viz.OFF)
	MainMenu()
	
def displaySubWindow(e):
	ARsubWindow.visible(True)

def removeSubWindow(e):
	ARsubWindow.visible(False)

speed = 0.125

def UpdateJoystick():
	x,y,z = joy.getPosition()
	twist = joy.getTwist()
	rx,ry,rz = joy.getRotation()
	if abs(x) > 0.2:
		viz.MainView.move([x*speed,0,0],viz.BODY_ORI)
	if abs(y) > 0.2:
		viz.MainView.move([0,0,-y*speed],viz.BODY_ORI)
	if abs(z) > 0.2:
		viz.MainView.move([0,-z*speed,0],viz.BODY_ORI)
	if abs(twist) > 0.2:
		viz.MainView.setEuler([twist,0,0],viz.BODY_ORI,viz.REL_PARENT)
	if abs(ry) > 0.2:
		viz.MainView.setEuler([0,ry,0],viz.HEAD_ORI,viz.REL_PARENT)
	if abs(rx) > 0.2:
		viz.MainView.setEuler([rx,0,0],viz.BODY_ORI,viz.REL_PARENT)
	if abs(rz) > 0.2:
		viz.MainView.setEuler([0,0,rz],viz.BODY_ORI,viz.REL_PARENT)
	if current_scene == 0:
		if joy.isButtonDown(1):
			accionbuttonNewGame()
		elif joy.isButtonDown(2):
			Daniel()
		elif joy.isButtonDown(3):
			Controls()
	elif current_scene == 1:
		if joy.isButtonDown(2):
			MainMenu()
	elif current_scene == 2:
		if joy.isButtonDown(1):
			Conant()
		elif joy.isButtonDown(2):
			MainMenu()
	elif current_scene == 3:
		if joy.isButtonDown(1):
			Pau()
		elif joy.isButtonDown(2):
			Daniel()
	elif current_scene == 4:
		if joy.isButtonDown(1):
			Diego()
		elif joy.isButtonDown(2):
			Conant()
	elif current_scene == 5:
		if joy.isButtonDown(1):
			MainMenu()
		elif joy.isButtonDown(2):
			Pau()
	elif current_scene == 6:
		if joy.isButtonDown(2):
			returntoMenu()

vizact.ontimer(0, UpdateJoystick)

current_scene = 0

ARscene = viz.addScene()
ARsubWindow = viz.addWindow(pos = [0,1], size = [0.25,0.25])
ARsubView = viz.addView()
ARsubView.setScene(ARscene)
ARsubWindow.setView(ARsubView)

cam = ar.addWebCamera(window = ARsubWindow)

ARitem = viz.addChild(item['gem3'], scene=ARscene)
mark1 = cam.addMatrixMarker(0,width = 1000)
viz.link(mark1, ARitem)

#AR2item = viz.addChild(item['gem4'], scene=ARscene)
#mark2 = cam.addMarker("ar\patt.hiro")
#viz.link(mark2, AR2item)

ARsubWindow.visible(False)

ETscene = viz.addScene()
ETsubWindow = viz.addWindow(pos = [0,1], size = [0.25,0.50])
ETsubView = viz.addView()
ETsubView.setScene(ETscene)
ETsubWindow.setView(ETsubView)

ETbgTexture = viz.add(image['estanio'])
ET_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = ETscene)
ET_bgtexture.texture(ETbgTexture)
ET_bgtexture.setScale(12.8,10.24,0)
ET_bgtexture.setPosition(0.5, 0.5) #Centro de pantalla
ETsubWindow.visible(False)

NQscene = viz.addScene()
NQsubWindow = viz.addWindow(pos = [0,1], size = [0.25,0.50])
NQsubView = viz.addView()
NQsubView.setScene(NQscene)
NQsubWindow.setView(NQsubView)

NQbgTexture = viz.add(image['niquel'])
NQ_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = NQscene)
NQ_bgtexture.texture(NQbgTexture)
NQ_bgtexture.setScale(12.8,10.24,0)
NQ_bgtexture.setPosition(0.5, 0.5) #Centro de pantalla
NQsubWindow.visible(False)

HRscene = viz.addScene()
HRsubWindow = viz.addWindow(pos = [0,1], size = [0.25,0.50])
HRsubView = viz.addView()
HRsubView.setScene(HRscene)
HRsubWindow.setView(HRsubView)

HRbgTexture = viz.add(image['hierro'])
HR_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = HRscene)
HR_bgtexture.texture(HRbgTexture)
HR_bgtexture.setScale(12.8,10.24,0)
HR_bgtexture.setPosition(0.5, 0.5) #Centro de pantalla
HRsubWindow.visible(False)

OROscene = viz.addScene()
OROsubWindow = viz.addWindow(pos = [0,1], size = [0.25,0.50])
OROsubView = viz.addView()
OROsubView.setScene(OROscene)
OROsubWindow.setView(OROsubView)

ORObgTexture = viz.add(image['oro'])
ORO_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = OROscene)
ORO_bgtexture.texture(ORObgTexture)
ORO_bgtexture.setScale(12.8,10.24,0)
ORO_bgtexture.setPosition(0.5, 0.5) #Centro de pantalla
OROsubWindow.visible(False)


#################################################################
#################################################################

#Escenario1
mine1 = viz.addChild(model['mundo1'], scene = viz.Scene1)
plane1 = viz.addChild(item['gem'], scene = viz.Scene1)
plane1.setScale(2.5,2.5,2.5)
plane1.setPosition(22,5,-1)
plane1.visible(False)
btn_regresa1 = viz.addButton(scene = viz.Scene1)
btn_regresa1.setPosition(0.9,0.1)
btn_regresa1.setScale(4,1.5)
btn_regresa1.downpicture(button['regresar'])
btn_regresa1.uppicture(button['regresar'])

gem11 = viz.addChild(item['gem1'], scene = viz.Scene1)
gem11.setScale(2.5,2.5,2.5)
gem11.setPosition(-4,3,15)

gem12 = viz.addChild(item['gem2'], scene = viz.Scene1)
gem12.setScale(2.5,2.5,2.5)
gem12.setPosition(4,3,15)

gem13 = viz.addChild(item['gem3'], scene = viz.Scene1)
gem13.setScale(2.5,2.5,2.5)
gem13.setPosition(15,5,4)

gem14 = viz.addChild(item['gem4'], scene = viz.Scene1)
gem14.setScale(2.5,2.5,2.5)
gem14.setPosition(-2,4,-12)

vizact.onbuttonup(btn_regresa1, returntoMenu)

#################################################################
#################################################################

#Escenario2 [56.73809051513672, 5.440362930297852, -3.700538396835327]
mine2 = viz.addChild(model['mundo2'], scene = viz.Scene2)
plane2 = viz.addChild(item['gem'], scene = viz.Scene2)
plane2.setScale(2.5,2.5,2.5)
plane2.setPosition(123,5,-24)
plane2.visible(False)
btn_regresa2 = viz.addButton(scene = viz.Scene2)
btn_regresa2.setPosition(0.9,0.1)
btn_regresa2.setScale(4,1.5)
btn_regresa2.downpicture(button['regresar'])
btn_regresa2.uppicture(button['regresar'])

gem21 = viz.addChild(item['gem1'], scene = viz.Scene2)
gem21.setScale(2.5,2.5,2.5)
gem21.setPosition(87,5,-4)
gem21.visible(False)

vizact.onbuttonup(btn_regresa2, returntoMenu)

#################################################################
#################################################################

#Escenario3 [130.56468200683594, 5.395919322967529, -30.007774353027344]
mine3 = viz.addChild(model['mundo3'], scene = viz.Scene3)
plane3 = viz.addChild(item['gem'], scene = viz.Scene3)
plane3.setScale(2.5,2.5,2.5)
plane3.setPosition(192,5,-8)
plane3.visible(False)
btn_regresa3 = viz.addButton(scene = viz.Scene3)
btn_regresa3.setPosition(0.9,0.1)
btn_regresa3.setScale(4,1.5)
btn_regresa3.downpicture(button['regresar'])
btn_regresa3.uppicture(button['regresar'])

gem31 = viz.addChild(item['gem1'], scene = viz.Scene3)
gem31.setScale(2.5,2.5,2.5)
gem31.setPosition(161,4,-33)
deslave_sound = gem31.playsound(sound['deslave'])

vizact.onbuttonup(btn_regresa3, returntoMenu)

#################################################################
#################################################################

#Escenario4 [276.3779602050781, 5.342123508453369, 26.81155014038086]
mine4 = viz.addChild(model['mundo4'], scene = viz.Scene4)
plane4 = viz.addChild(item['gem'], scene = viz.Scene4)
plane4.setScale(2.5,2.5,2.5)
plane4.setPosition(335,5,-3)
plane4.visible(False)
btn_regresa4 = viz.addButton(scene = viz.Scene4)
btn_regresa4.setPosition(0.9,0.1)
btn_regresa4.setScale(4,1.5)
btn_regresa4.downpicture(button['regresar'])
btn_regresa4.uppicture(button['regresar'])

gem41 = viz.addChild(item['gem'], scene = viz.Scene4)
gem41.setScale(2.5,2.5,2.5)
gem41.setPosition(324,5,10)
gem41.visible(False)

vizact.onbuttonup(btn_regresa4, returntoMenu)

##################################################################
#################################################################

#Escenario5 [218.66688537597656, 5.440362930297852, -89.66780090332031]
mine5 = viz.addChild(model['mundo5'], scene = viz.Scene5)
plane5 = viz.addChild(item['gem'], scene = viz.Scene5)
plane5.setScale(2.5,2.5,2.5)
plane5.setPosition(325,5,-60)
plane5.visible(False)
btn_regresa5 = viz.addButton(scene = viz.Scene5)
btn_regresa5.setPosition(0.9,0.1)
btn_regresa5.setScale(4,1.5)
btn_regresa5.downpicture(button['regresar'])
btn_regresa5.uppicture(button['regresar'])

gem51 = viz.addChild(item['gem1'], scene = viz.Scene5)
gem51.setScale(2.5,2.5,2.5)
gem51.setPosition(245,3,-97)

canvas51 = viz.addGUICanvas()
canvas51.alignment(viz.ALIGN_CENTER)
viz.MainWindow.setDefaultGUICanvas(canvas51)
info51 = vizinfo.InfoPanel('AVERNO', align=viz.ALIGN_RIGHT_TOP, icon=False)
info51.setTitle( 'Ejemplo' )
info51.setPanelVisible(False)
canvas51.setRenderWorld([600,500],[3,viz.AUTO_COMPUTE])
canvas51.setPosition([gem51.getPosition()[0],gem51.getPosition()[1]+0.5,gem51.getPosition()[2]])
canvas51.setEuler(0,0,0)

gem52 = viz.addChild(item['gem1'], scene = viz.Scene5)
gem52.setScale(2.5,2.5,2.5)
gem52.setPosition(295,3,-110)

canvas52 = viz.addGUICanvas()
canvas52.alignment(viz.ALIGN_CENTER)
viz.MainWindow.setDefaultGUICanvas(canvas52)
info52 = vizinfo.InfoPanel('AVERNO', align=viz.ALIGN_RIGHT_TOP, icon=False)
info52.setTitle( 'Ejemplo' )
info52.setPanelVisible(False)
canvas52.setRenderWorld([600,500],[3,viz.AUTO_COMPUTE])
canvas52.setPosition([gem52.getPosition()[0],gem52.getPosition()[1]+0.5,gem52.getPosition()[2]])
canvas52.setEuler(0,0,0)

gem53 = viz.addChild(item['gem1'], scene = viz.Scene5)
gem53.setScale(2.5,2.5,2.5)
gem53.setPosition(328,4,-73)

canvas53 = viz.addGUICanvas()
canvas53.alignment(viz.ALIGN_CENTER)
viz.MainWindow.setDefaultGUICanvas(canvas53)
info53 = vizinfo.InfoPanel('AVERNO', align=viz.ALIGN_RIGHT_TOP, icon=False)
info53.setTitle( 'Ejemplo' )
info53.setPanelVisible(False)
canvas53.setRenderWorld([600,500],[3,viz.AUTO_COMPUTE])
canvas53.setPosition([gem53.getPosition()[0],gem53.getPosition()[1]+0.5,gem53.getPosition()[2]])
canvas53.setEuler(0,0,0)

vizact.onbuttonup(btn_regresa5, returntoMenu)

#################################################################
#################################################################

#Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(viz.ON)

#Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

#Sensor boundary
sensorGem12 = vizproximity.addBoundingBoxSensor(gem12,scale=[6,4,6])
sensorGem13 = vizproximity.addBoundingBoxSensor(gem13,scale=[6,4,6])
########################################################################
sensorGem21 = vizproximity.addBoundingBoxSensor(gem13,scale=[6,4,6])
########################################################################
sensorGem31 = vizproximity.addBoundingBoxSensor(gem31,scale=[6,4,6])
########################################################################

########################################################################
sensorGem51 = vizproximity.addBoundingBoxSensor(gem51,scale=[6,4,6])
sensorGem52 = vizproximity.addBoundingBoxSensor(gem52,scale=[6,4,6])
sensorGem53 = vizproximity.addBoundingBoxSensor(gem53,scale=[6,4,6])
########################################################################
sensorPlane1 = vizproximity.addBoundingBoxSensor(plane1,scale=[10,8,8])
sensorPlane2 = vizproximity.addBoundingBoxSensor(plane2,scale=[10,10,10])
sensorPlane3 = vizproximity.addBoundingBoxSensor(plane3,scale=[10,10,10])
sensorPlane4 = vizproximity.addBoundingBoxSensor(plane4,scale=[10,10,10])
sensorPlane5 = vizproximity.addBoundingBoxSensor(plane5,scale=[10,10,10])

#Add Sensor
########################################################################
manager.addSensor(sensorGem12)
manager.addSensor(sensorGem13)
####################################
manager.addSensor(sensorGem21)
####################################
manager.addSensor(sensorGem31)
####################################

####################################
manager.addSensor(sensorGem51)
manager.addSensor(sensorGem52)
manager.addSensor(sensorGem53)
####################################
manager.addSensor(sensorPlane1)
manager.addSensor(sensorPlane2)
manager.addSensor(sensorPlane3)
manager.addSensor(sensorPlane4)
manager.addSensor(sensorPlane5)


#OnENTER
manager.onEnter(sensorGem12,displaySubWindow)
manager.onEnter(sensorGem13,displaySubWindow)
#############################################
manager.onEnter(sensorGem21,deslave_sound.play())
#############################################
manager.onEnter(sensorGem31,enterGem)
#############################################

#############################################
manager.onEnter(sensorGem51,enterGem)
manager.onEnter(sensorGem52,enterGem)
manager.onEnter(sensorGem53,enterGem)
#############################################
manager.onEnter(sensorPlane1,EnterProximity)
manager.onEnter(sensorPlane2,EnterProximity)
manager.onEnter(sensorPlane3,EnterProximity)
manager.onEnter(sensorPlane4,EnterProximity)
manager.onEnter(sensorPlane5,EnterProximity)

#OnEXIT
manager.onExit(sensorGem31,exitGem)
manager.onExit(sensorGem51,exitGem)
manager.onExit(sensorGem52,exitGem)
manager.onExit(sensorGem53,exitGem)
manager.onExit(sensorGem12,removeSubWindow)
manager.onExit(sensorGem13,removeSubWindow)

manager.setDebug(viz.OFF)
vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

MainMenu()

chime_sound = viz.addAudio(sound['chime'])
elevator_sound = viz.addAudio(sound['elevator'])
explosion_sound = viz.addAudio(sound['deslave'])
hammer_sound = viz.addAudio(sound['hammer'])
dirt_sound = viz.addAudio(sound['dirt'])
cave_sound = viz.addAudio(sound['cave'])

viz.MainView.eyeheight(4.75)
#viz.MainView.setPosition(-65,5,8)
toogleCollide(True)

joy = vizjoy.add()

viz.go()

print "MenuPrincipal"

#vizact.ontimer(0,UpdateJoystick)
