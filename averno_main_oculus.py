import viz, vizconnect, vizact, vizinfo, vizjoy, vizproximity, oculus, ctypes
from modelscene import ModelScene

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

viz.window.setName('AVERNO')
viz.window.setPosition(300,50)
#viz.window.setBorder(viz.BORDER_FIXED)
viz.go()
#vizconnect.go('configOculus.py')

model = {
	'mundo1' : "models/AbernoD.obj",
	'mundo2' : "models/AbernoL04.obj"
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

chime_sound = viz.addAudio(sound['chime'])

collide = True
isActive = [True, False, False, False, False, False, False]
current_scene = 0

if len(model) > 5:
	for m in range(0, len(model)-6):
		viz.addScene()
	viz.addScene()

#OCULUS: viz.MainView.setPosition(-62,0,8)
def setInitialPosition():
	toogleCollide(False)
	viz.MainView.setPosition(-62,5,8)
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
	viz.scene(viz.VizScene(0))
	setInitialPosition()

def toogleCollide(flag):
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
	print e.sensor
	model1.setGemInfoPanelStatus(e.sensor)
	chime_sound.play()

#vizact.ontimer(0,UpdateMovement)

print "ESCENA-"
gemLev1 = [item['gem'], item['gem']]
gemPosLev1 = [[-30,4], [-20,4]]
gemcount1 = len(gemLev1)
planeLev1 = [item['gem']]
planePosLev1 = [[10,5]]
nextScene1 = [viz.VizScene(2)]
model1 = ModelScene(model['mundo1'], viz.VizScene(1), gemLev1, gemPosLev1, gemcount1, planeLev1 , planePosLev1, nextScene1, chime_sound, chime_sound)

gemLev2 = [item['gem'], item['gem']]
gemPosLev2 = [[-30,4], [-20,4]]
gemcount2 = len(gemLev2)
planeLev2 = [item['gem']]
planePosLev2 = [[10,5]]
nextScene2 = [viz.VizScene(1)]
model2 = ModelScene(model['mundo2'], viz.VizScene(2), gemLev2, gemPosLev2, gemcount2, planeLev2 , planePosLev2, nextScene2, chime_sound, chime_sound)

#Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(viz.ON)

#Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

listaGems1 = model1.getGemSensorList()

for i in listaGems1:
	manager.addSensor(i)
	manager.onEnter(i, model1.enterGem)
	
#listaPlanes1 = model1.getPlaneSensorList()
'''
for i in listaPlanes1:
	manager.onEnter(i, model1.enterPlane(manager))
'''
vizact.onbuttonup(model1.getReturnButton(), returntoMenu)
vizact.onbuttonup(model2.getReturnButton(), returntoMenu)

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

vizact.onkeydown('d',manager.setDebug,viz.TOGGLE)

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

viz.MainView.eyeheight(4.75)
#viz.MainView.setPosition(-65,5,8)
toogleCollide(True)

print "MenuPrincipal"