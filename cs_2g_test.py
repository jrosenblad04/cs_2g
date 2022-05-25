from email.mime import image
from re import M
from turtle import width
from cmu_graphics import *
import os
thisFolder = os.path.dirname(os.path.realpath(__file__))
app.width = 600
app.height = 450
app.gravity = 1
app.steps = 30
jumpcounter = Label(0, 0, 0)
Rect(0,0, 600,128, fill = 'navy', border = gradient('slategray','white'), borderWidth = 10)

app.ballsize = 10
player = Circle(100, 380, 10, fill = 'white')
player.vx = 5
player.vy = 0
player.fallMultiplier = 2.5
player.jumpHeight = 15
player.grounded = False

coffee = Image(thisFolder + '/coffee.png', 550, 360, width = 40, height = 40)

snowgroup1 = Group(
)
snowgroup2 = Group(
)
def makeSnow():
    for i  in range(12):
        snowball = Image(thisFolder + '/snowtexture.png', i*50, 400, width = 50, height = 50)
        snowball2 = Image(thisFolder + '/snowtexture.png', (i*50)+300, 400, width = 50, height = 50)
        snowgroup1.add(snowball)
        snowgroup2.add(snowball2)

makeSnow()

Sky1 = Image(thisFolder + '/Sky.png', 0, 128, width = 600, height = 160*1.7)
Sky2 = Image(thisFolder + '/Sky.png', 399, 128, width = 600, height = 160*1.7)
mountain1 = Image(thisFolder + '/Mountains.png', 0, 128, width = 600, height = 160*1.7)
mountain2 = Image(thisFolder + '/Mountains.png', 399, 128, width = 600, height = 160*1.7)
trees1 = Image(thisFolder + '/Forest.png', 0, 128, width = 600, height = 160*1.7)
trees2 = Image(thisFolder + '/Forest.png', 399, 128, width = 600, height = 160*1.7)

def moveMountains (speed):
    mountain1.centerX -= speed
    if (mountain1.right <= 0):
        mountain1.left = 600
    if (mountain1.left >= 0):
        mountain2.right = mountain1.left+1
    else:
        mountain2.left = mountain1.right-1

def moveTrees(speed):
    trees1.centerX -= speed
    if (trees1.right <= 0):
        trees1.left = 600
    if (trees1.left >= 0):
        trees2.right = trees1.left
    else:
        trees2.left = trees1.right

def moveSnow(speed):
    snowgroup1.centerX -= speed
    if (snowgroup1.right <= 0):
        snowgroup1.left = 600
    if (snowgroup1.left >= 0):
        snowgroup2.right = snowgroup1.left
    else:
        snowgroup2.left = snowgroup1.right

def moveSky(speed):
    Sky1.centerX -= speed
    if (Sky1.right <= 0):
        Sky1.left = 600
    if (Sky1.left >= 0):
        Sky2.right = Sky1.left+1
    else:
        Sky2.left = Sky1.right-1

def onStep():
    moveMountains(1)
    moveTrees(4)
    moveSnow(10)
    moveSky(0.5)
    player.toFront()
    coffee.toFront()
    
    if player.grounded == True:
        player.radius += 0.02
    
    player.centerY += player.vy

    if(player.vy <= 0):
        player.vy += app.gravity * player.fallMultiplier
        
    else:
        player.vy += app.gravity
    
    if(player.grounded == True):
        jumpcounter.value = 0
    
    if(player.bottom >= 400):
        player.vy = 0
        player.grounded = True
        player.bottom = 400
    if(player.top <= 128):
        player.top = 129
        player.vy = 0


def onKeyPress(keys):
    if(keys == 'space') and jumpcounter.value < 2:
        player.vy -= 23
        player.grounded = False
        jumpcounter.value += 1

    if(keys  == 'p') and app.paused == False:
        app.paused = True
    else:
        app.paused = False
    
cmu_graphics.run()