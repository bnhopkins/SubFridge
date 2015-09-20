#!/usr/bin/python
from SimpleCV import *
from SimpleCV.DrawingLayer import DrawingLayer
import os

img = Image("../../sampleimages/color.jpg")
lineL = DrawingLayer((img.width,img.height))
a = (20,20)
b = (20,100)
c = (100,100)
d = (100,20)
lineL.line(a,b,alpha=128,width=5)
lineL.line(b,c,alpha=128)
lineL.line(c,d, antialias=True)
lineL.line(d,a,color=Color.PUCE)
lineL.line(a,c,color=Color.PLUM, alpha=52)
lineL.line(b,d,width=5)
img.addDrawingLayer(lineL)
temp = img.applyLayers()
print "line: %s" % temp.save(temp=True)
img.clearLayers()

linesL = DrawingLayer((img.width,img.height))
a = (20,20)
b = (20,100)
c = (100,100)
d = (100,20)
pts = (a,b,c,d,a)
linesL.lines(pts,alpha=128)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
linesL.lines(pts,color=Color.BEIGE,width=10)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
linesL.lines(pts,antialias=True)
img.addDrawingLayer(linesL)
temp = img.applyLayers()
print "lines: %s" % temp.save(temp=True)
img.clearLayers()

rectTR = DrawingLayer((img.width,img.height))
tr = (150,50)
wh = (200,100)
rectTR.rectangle(tr,wh,color=Color.BLUE)
tr = (170,70)
rectTR.rectangle(tr,wh,color=Color.PUCE, width=5)
tr = (190,90)
rectTR.rectangle(tr,wh,color=Color.FORESTGREEN, alpha=128,filled=True)
tr = (210,110)
rectTR.rectangle(tr,wh,color=Color.GREEN,filled=True)
img.addDrawingLayer(rectTR)
temp = img.applyLayers()
print "rectTR: %s" % temp.save(temp=True)
img.clearLayers()

rectC = DrawingLayer((img.width,img.height))
cxy = (img.width/2,img.height/2)
wh = (200,100)
rectC.centeredRectangle(cxy,wh,color=Color.BLUE)
wh = (180,80)
rectC.centeredRectangle(cxy,wh,color=Color.PUCE, width=5)
wh = (160,60)
rectC.centeredRectangle(cxy,wh,color=Color.FORESTGREEN, alpha=128,filled=True)
wh = (140,40)
rectC.centeredRectangle(cxy,wh,color=Color.GREEN,filled=True)
img.addDrawingLayer(rectC)
temp = img.applyLayers()
print "rectC: %s" % temp.save(temp=True)
img.clearLayers()

polyL = DrawingLayer((img.width,img.height))
a = (50,img.height-50)
b = (250,img.height-50)
c = (150,50)
pts = (a,b,c)
polyL.polygon(pts,alpha=128)
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
polyL.polygon(pts,antialias=True,width=3,alpha=210,filled=True,color=Color.LIME)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
polyL.polygon(pts,color=Color.BEIGE,width=10)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
polyL.polygon(pts,antialias=True,width=3,alpha=210)
img.addDrawingLayer(polyL)
temp = img.applyLayers()
print "poly: %s" % temp.save(temp=True)
img.clearLayers()

circleL = DrawingLayer((img.width,img.height))
c = (img.width/2,img.height/2)
r = 150
circleL.circle(c,r,color=Color.RED,filled=True)
r = 130
circleL.circle(c,r,color=Color.ORANGE,alpha=128,filled=True)
r = 110
circleL.circle(c,r,color=Color.YELLOW,alpha=128,width=10)
r = 100
circleL.circle(c,r,color=Color.GREEN)
r = 90
circleL.circle(c,r,color=Color.BLUE,alpha=172)
img.addDrawingLayer(circleL)
temp = img.applyLayers()
print "circle: %s" % temp.save(temp=True)
img.clearLayers()

ellipseL = DrawingLayer((img.width,img.height))
cxy = (img.width/2,img.height/2)
wh = (200,100)
ellipseL.ellipse(cxy,wh,color=Color.BLUE)
wh = (180,80)
ellipseL.ellipse(cxy,wh,color=Color.PUCE, width=5)
wh = (160,60)
ellipseL.ellipse(cxy,wh,color=Color.FORESTGREEN, alpha=128,filled=True)
wh = (140,40)
ellipseL.ellipse(cxy,wh,color=Color.GREEN,filled=True)
img.addDrawingLayer(ellipseL)
temp = img.applyLayers()
print "ellipse: %s" % temp.save(temp=True)
img.clearLayers()

bez = DrawingLayer((img.width,img.height))
a = (20,20)
b = (img.width-20,20)
c = (img.height-20,img.width-20)
d = (20,img.height-20)
e = (img.width/2,img.height/2)
pts = (a,b,c,d,e)
bez.bezier(pts,30)
img.addDrawingLayer(bez)
#translate over and down 10
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
bez.bezier(pts,5,color=Color.RED)
img.addDrawingLayer(bez)
pts = map(lambda x: ((x[0]+10),(x[1]+10)),pts)
bez.bezier(pts,30,color=Color.GREEN, alpha=128)
img.addDrawingLayer(bez)
temp = img.applyLayers()
print "bez: %s" % temp.save(temp=True)
img.clearLayers()

words = DrawingLayer((img.width,img.height))
words.setDefaultColor(Color.RED)
pos = (30,30)
words.setFontSize(30)
words.text("THIS IS BIG",pos)
pos = (50,50)
words.setFontSize(10)
words.text("THIS IS SMALL",pos)
pos = (70,70)
words.setFontSize(20)
words.text("THIS IS medium",pos)
pos = (90,90)
words.setFontBold(True)
words.text("THIS IS bold",pos)
pos = (110,110)
words.setFontItalic(True)
words.text("THIS IS italic",pos)
pos = (130,130)
words.setFontUnderline(True)
words.text("THIS IS underline",pos)
words.setFontBold(False)
words.setFontItalic(False)
words.setFontUnderline(False)
pos = (150,150)
words.text("THIS IS PUCE, YES PUCE",pos,color=Color.PUCE)
pos = (170,170)
words.text("This is magical text",pos,color=Color.PLUM,alpha=128)
pos = (190,190)
words.ezViewText("Can you read this better?",pos)
img.addDrawingLayer(words)
temp = img.applyLayers()
print "words: %s" % temp.save(temp=True)
img.clearLayers()

#Now lets do some layer stuff
img.addDrawingLayer(lineL)
img.addDrawingLayer(circleL)
img.addDrawingLayer(bez)
img.addDrawingLayer(words)
temp = img.applyLayers([0,2,3])
print "layers: %s" % temp.save(temp=True)
img.clearLayers()

#now lets do some blanket alpha work
lineL.setLayerAlpha(128)
circleL.setLayerAlpha(128)
bez.setLayerAlpha(128)
words.setLayerAlpha(128)
img.addDrawingLayer(lineL)
img.addDrawingLayer(circleL)
img.addDrawingLayer(bez)
img.addDrawingLayer(words)
temp = img.applyLayers()
print "flatlayers: %s" % temp.save(temp=True)
img.clearLayers()

sprites = DrawingLayer((img.width,img.height))
sprites.sprite("../../sampleimages/logo.png",(0,0),alpha=128, rot=45,scale=1.5)
mySprite = Image("../../sampleimages/logo.png").toPygameSurface()
sprites.sprite(mySprite,(100,100),alpha=128, rot=45,scale=1.5)
sprites.sprite(mySprite,(200,0))
sprites.sprite(mySprite,(0,200), rot=45,scale=1)
img.addDrawingLayer(sprites)
temp = img.applyLayers()
print "sprites: %s" % temp.save(temp=True)
img.clearLayers()