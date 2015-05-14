import viz, vizconnect, vizact, vizinfo, vizjoy, vizproximity, oculus

viz.window.setName('AVERNO')
viz.window.setPosition(300,50)
#viz.window.setBorder(viz.BORDER_FIXED)
viz.go()
#vizconnect.go('configOculus.py')

model = {
	'mundo1' : "models/AbernoD.obj",
	'mundo2' : "models/AbernoL04.obj",
	'mundo3' : "models/AbernoD.obj",
	'mundo4' : "models/AbernoL04.obj",
	'mundo5' : "models/AbernoD.obj",
	'mundo6' : "models/AbernoL04.obj",
	'mundo7' : "models/AbernoD.obj",
	'mundo8' : "models/AbernoL04.obj",
	'mundo9' : "models/AbernoD.obj",
	'mundo10' : "models/AbernoL04.obj",
	'mundo11' : "models/AbernoD.obj",
	'mundo12' : "models/AbernoL04.obj",
	'mundo13' : "models/AbernoD.obj",
	'mundo14' : "models/AbernoL04.obj"
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
	viz.scene(viz.VizScene(1))
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

def EnterGem(e,info):
	print e.sensor
	info.setPanelVisible(True)
	chime_sound.play()

#################################################################
#################################################################

gemLev1 = [item['gem'], item['gem']]
gemPosLev1 = [[-30,4], [-20,4]]
planeLev1 = [item['gem']]
planePosLev1 = [[10,5]]

#Escenario1
mine1 = viz.addChild(model['mundo1'], viz.VizScene(1))
plane11 = viz.addChild(planeLev1[0], viz.VizScene(1))
plane11.setPosition(planePosLev1[0][0], planePosLev1[0][1])
btn_regresa1 = viz.addButtonLabel("regresar", scene = viz.Scene1)
btn_regresa1.setPosition(0.9,0.1)

gem11 = viz.addChild(gemLev1[0], viz.VizScene(1))
gem11.setPosition(gemPosLev1[0][0],gemPosLev1[0][1])
canvas11 = viz.addGUICanvas()
canvas11.alignment(viz.ALIGN_CENTER)
viz.MainWindow.setDefaultGUICanvas(canvas11)
info11 = vizinfo.InfoPanel('AVERNO', align=viz.ALIGN_RIGHT_TOP, icon=False)
info11.setTitle( 'Ejemplo' )
info11.setPanelVisible(False)
canvas11.setRenderWorld([600,500],[3,viz.AUTO_COMPUTE])
canvas11.setPosition([gem11.getPosition()[0],gem11.getPosition()[1]+0.5,gem11.getPosition()[2]])
canvas11.setEuler(0,0,0)

gem12 = viz.addChild(gemLev1[1], scene = viz.VizScene(1))
gem12.setPosition(gemPosLev1[1][0],gemPosLev1[1][1])
canvas12 = viz.addGUICanvas()
canvas12.alignment(viz.ALIGN_CENTER)
viz.MainWindow.setDefaultGUICanvas(canvas12)
info12 = vizinfo.InfoPanel('AVERNO', align=viz.ALIGN_RIGHT_TOP, icon=False)
info12.setTitle('Ejemplo')
info12.setPanelVisible(False)
canvas12.setRenderWorld([600,500],[3,viz.AUTO_COMPUTE])
canvas12.setPosition([gem12.getPosition()[0],gem12.getPosition()[1]+0.5,gem12.getPosition()[2]])
canvas12.setEuler(0,0,0)

vizact.onbuttonup(btn_regresa1, returntoMenu)

#################################################################
#################################################################



#Create proximity manager
manager = vizproximity.Manager()
manager.setDebug(viz.ON)

#Add main viewpoint as proximity target
target = vizproximity.Target(viz.MainView)
manager.addTarget(target)

sensorGem11 = vizproximity.addBoundingBoxSensor(gem11,scale=[6,4,6])
sensorGem12 = vizproximity.addBoundingBoxSensor(gem12,scale=[6,4,6])
manager.onEnter(sensorGem11,EnterGem,info11)
manager.onEnter(sensorGem12,EnterGem,info12)

vizact.onbuttonup(btn_regresa1, returntoMenu)

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