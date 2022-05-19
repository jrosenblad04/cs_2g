from cmu_graphics import *
bb = Rect(200, 200, 50, 50)
speed = Label(int(10), 200, 50)
def onKeyHold(keys):
    bb.centerX += speed
    if(bb.left >= 400):
        bb.right = 0
def onKeyPress(keys):
    if(keys == 'up'):
        speed.value += 5
    elif(keys == 'down'):
        speed.value -= 5
cmu_graphics.run()