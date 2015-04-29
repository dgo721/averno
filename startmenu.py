import viz, vizact, vizcam, vizinfo, random, vizjoy

viz.go()

def accionbuttonNewGame():
	viz.scene(viz.Scene1)
	viz.MainView.setPosition([0,1.82,0])

def returntoMenu():
	viz.scene(viz.Scene2)
	viz.MainWindow.stereo(viz.OFF)

def UpdateJoystick():
	x,y,z = joy.getPosition()
	twist = joy.getTwist()
	rx,ry,rz = joy.getRotation()
	if joy.isButtonDown(1):
		accionbuttonNewGame()
	if joy.isButtonDown(2):
		returntoMenu()
	if abs(x) > 0.2:
		viz.MainView.move([x*0.1,0,0],viz.BODY_ORI)
	if abs(y) > 0.2:
		viz.MainView.move([0,0,-y*0.1],viz.BODY_ORI)
	if abs(z) > 0.2:
		viz.MainView.move([0,-z*0.1,0],viz.BODY_ORI)
	if abs(twist) > 0.2:
		viz.MainView.setEuler([twist,0,0],viz.BODY_ORI,viz.REL_PARENT)
	if abs(ry) > 0.2:
		viz.MainView.setEuler([0,ry,0],viz.HEAD_ORI,viz.REL_PARENT)
	if abs(rx) > 0.2:
		viz.MainView.setEuler([rx,0,0],viz.BODY_ORI,viz.REL_PARENT)
	if abs(rz) > 0.2:
		viz.MainView.setEuler([0,0,rz],viz.BODY_ORI,viz.REL_PARENT)

#Escenario
mine = viz.addChild("models/AbernoL04.obj", scene = viz.Scene1)
btn_regresa = viz.addButtonLabel("regresar", scene = viz.Scene1)
btn_regresa.setPosition(0.9,0.1)
	
vizact.onbuttonup(btn_regresa, returntoMenu)

#GUI inicial
bgTexture = viz.add("img/Portada_Averno_1024.jpg")
quad_bgtexture = viz.addTexQuad(parent = viz.SCREEN, scene = viz.Scene2)
quad_bgtexture.texture(bgTexture)
quad_bgtexture.setScale(12.8,10.24,0) #Escala a pantalla completa
quad_bgtexture.setPosition(0.5, 0.5) #Centro de pantalla
viz.scene(viz.Scene2) #Mostrar escena 2

#Botones de interaccion
btn_newGame = viz.addButton(scene = viz.Scene2)
btn_newGame.setPosition(0.75,0.75)
btn_newGame.setScale(8,2.3)
btn_newGame.downpicture("img/button_down_Dojo.png")
btn_newGame.uppicture("img/button_up_Dojo.png")

#Botones de interaccion
btn_credits = viz.addButton(scene = viz.Scene2)
btn_credits.setPosition(0.75,0.60)
btn_credits.setScale(8,2.3)
btn_credits.downpicture("img/button_down_Dojo.png")
btn_credits.uppicture("img/button_up_Dojo.png")
	
vizact.onbuttonup(btn_newGame, accionbuttonNewGame)

joy = vizjoy.add()

vizact.ontimer(0,UpdateJoystick)