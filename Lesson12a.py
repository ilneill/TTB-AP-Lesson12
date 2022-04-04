# Using an Arduino with Python LESSON 12: Parameterised Model Design for 3D Graphics.
#  -> Sub Task A - Parameterising a Simple LED.
# https://www.youtube.com/watch?v=DcOT3gtVG8Y
# https://toptechboy.com/

# Internet References:
# https://www.glowscript.org/docs/VPythonDocs/index.html

import time
from vpython import *

# Focus on 1 LED at the origin.
just1LED = False
# Use the Lesson 11 Small LED class definition?
useL11LED = False

# vPython refresh rate.
vPythonRefreshRate = 100
# LED on/off period in seconds.
ledFlashPeriod = 1
# XYZ Scale Axis toggle.
showAxis = True

# A place on which to put our things...
canvas(title = "<b><i>Arduino with Python - Parameterising a Simple LED!</i></b>", background = color.cyan, width = 800, height = 600)

# An XYZ axis to help us get our bearings.
if showAxis:
    arrow(color = color.blue, round = True, pos = vector(-0.5, 0, 0), axis = vector(1, 0, 0), shaftwidth = 0.02) # X axis.
    arrow(color = color.blue, round = True, pos = vector(0, -0.5, 0), axis = vector(0, 1, 0), shaftwidth = 0.02) # Y axis.
    arrow(color = color.blue, round = True, pos = vector(0, 0, -0.5), axis = vector(0, 0, 1), shaftwidth = 0.02) # Z axis.

# A simple LED - this is the Lesson 11 version of this class.
class smallLED():
    def __init__(self, smallLEDPos = vector(0, 0, 0), offColor = color.gray(0.5)):
        self.smallLEDPos = smallLEDPos
        self.offColor = offColor
        self.ledDome = sphere(color = self.offColor, opacity = 1, radius = 0.1, pos = vector(0, 0, 0.15) + self.smallLEDPos)
        self.ledBody = cylinder(color = self.offColor, opacity = 1, pos = vector(0, 0, 0.15) + self.smallLEDPos, axis = vector(0, 0, -0.1), radius = 0.1)
        self.ledBase = cylinder(color = self.offColor, opacity = 1, pos = vector(0, 0, 0.05) + self.smallLEDPos, axis = vector(0, 0, -0.05), radius = 0.125)
        cylinder(color = color.white, opacity = 1, pos = vector(-0.05, 0, 0) + self.smallLEDPos, axis = vector(0, 0, -0.25), radius = 0.01)
        cylinder(color = color.white, opacity = 1, pos = vector(0.05, 0, 0) + self.smallLEDPos, axis = vector(0, 0, -0.30), radius = 0.01)
    def update(self, smallLEDColor = "default"):
        if smallLEDColor == "default":
            self.color = self.offColor
        else:
            self.color = smallLEDColor
        self.ledDome.color = self.color
        self.ledBody.color = self.color
        self.ledBase.color = self.color

# A simple LED - a fully parameterised version.
class simpleLED():
    def __init__(self, simpleLEDPos = vector(0, 0, 0), offColor = color.gray(0.5), scale = 1, axis = 'z'):
        # Set the XYZ axis scaling.
        if axis.lower() == 'x':
            xScale = scale
            yScale = zScale = 0 # Ensure the other axis scales are zero.
        elif axis.lower() == 'y':
            yScale = scale
            xScale = zScale = 0 # Ensure the other axis scales are zero.
        else: # If not 'x' or 'y', assume 'z'.
            zScale = scale
            xScale = yScale = 0 # Ensure the other axis scales are zero.
        # The LED off color that is used later.
        self.offColor = offColor
        # The LED colored parts - initially set to white so that the blended compound object color looks right.
        ledDome = sphere(color = color.white, opacity = 0.95, radius = scale * 0.1, shininess = 0.25, 
                         pos = vector(xScale * 0.20, yScale * 0.20, zScale * 0.20) + simpleLEDPos)
        ledBulb = simple_sphere(color = color.white, opacity = 1 , radius = scale * 0.08,  shininess = 0.75,
                                pos = vector(xScale * 0.20, yScale * 0.20, zScale * 0.20) + simpleLEDPos)
        ledBody = cylinder(color = color.white, opacity = 0.95, radius = scale * 0.1, shininess = 0.25, 
                           pos = vector(xScale * 0.05, yScale * 0.05, zScale * 0.05) + simpleLEDPos,
                           axis = vector(xScale * 0.15, yScale * 0.15, zScale * 0.15))
        # The LED base is initially set to a very light gray so that it is always a bit darker than the rest of the LED.
        ledBase = cylinder(color = color.gray(0.90), opacity = 0.95, radius = scale * 0.125, shininess = 0.25,
                           pos = vector(0, 0, 0) + simpleLEDPos,
                           axis = vector(xScale * 0.05, yScale * 0.05, zScale * 0.05))
        # The LED legs.
        cylinder(color = color.white, opacity = 1, radius = scale * 0.01,
                 pos = vector((xScale * 0.025) + (yScale * -0.05) + (zScale * -0.05),
                              (xScale * -0.05) + (yScale * 0.025) + (zScale * 0),
                              (xScale * 0)     + (yScale * 0)     + (zScale * 0.025)) + simpleLEDPos,
                 axis = vector(xScale * -0.25, yScale * -0.25, zScale * -0.25))
        cylinder(color = color.white, opacity = 1, radius = scale * 0.01,
                 pos = vector((xScale * 0.025) + (yScale * 0.05)  + (zScale * 0.05),
                              (xScale * 0.05)  + (yScale * 0.025) + (zScale * 0),
                              (xScale * 0)     + (yScale * 0)     + (zScale * 0.025)) + simpleLEDPos,
                 axis = vector(xScale * -0.30, yScale * -0.30, zScale * -0.30))
        # Combine the LED colored parts into a single object.
        self.simpleLED = compound([ledDome, ledBulb, ledBody, ledBase], color = self.offColor) # We want to change the color of these parts simultaneously.
    def update(self, simpleLEDColor = "off"):
        if simpleLEDColor == "off":
            self.simpleLED.emissive = False
            self.simpleLED.color = self.offColor
        else:
            self.simpleLED.emissive = True
            self.simpleLED.color = simpleLEDColor

# Draw a selection of simple LEDs.
if useL11LED:
    myLED1 = smallLED(vector(0.00, 0.00, 0.00), color.white)
    if not just1LED:
        myLED2 = smallLED(vector(-1.00, 0.50, -0.50), color.gray(0.5))
        myLED3 = smallLED(vector(0.00, 0.50, 0.00), color.gray(0.5))
        myLED4 = smallLED(vector(1.00, 0.50, 0.50), color.gray(0.5))
        myLED5 = smallLED(vector(-1.00, -0.50, 0.50), color.gray(0.5))
        myLED6 = smallLED(vector(0.00, -0.50, 0.00), color.gray(0.5))
        myLED7 = smallLED(vector(1.00, -0.50, -0.50), color.gray(0.5))
        myLED8 = smallLED(vector(-0.50, 0.00, 0.00), color.green)
        myLED9 = smallLED(vector(0.50, 0.00, 0.00), color.black)
else:
    myLED1 = simpleLED(vector(0.00, 0.00, 0.00), color.white, 0.5, 'z')
    if not just1LED:
        myLED2 = simpleLED(vector(-1.00, 0.50, -0.50), color.gray(0.5), 1, 'x')
        myLED3 = simpleLED(vector(0.00, 0.50, 0.00), color.gray(0.5), 1.5, 'y')
        myLED4 = simpleLED(vector(1.00, 0.50, 0.50), color.gray(0.5), 2, 'z')
        myLED5 = simpleLED(vector(-1.00, -0.50, 0.50), color.gray(0.5), -1, 'z')
        myLED6 = simpleLED(vector(0.00, -0.50, 0.00), color.gray(0.5), -1.5, 'y')
        myLED7 = simpleLED(vector(1.00, -0.50, -0.50), color.gray(0.5), -2, 'x')
        myLED8 = simpleLED(vector(-0.50, 0.00, 0.00), color.green, -0.5, 'y')
        myLED9 = simpleLED(vector(0.50, 0.00, 0.00), color.black, 0.5, 'y')

ledToggle = 0 # LED on/off toggle.
startTime = time.time()
# An infinite loop: When is True, True? It is always True!
while True:
    rate(vPythonRefreshRate) # The vPython rate command is obligatory in animation loops.
    timeNow = time.time()
    elapsedTime = timeNow - startTime
    if elapsedTime >= ledFlashPeriod:
        startTime = timeNow
        ledToggle = (ledToggle + 1) % 2 # Using modulo 2 maths to toggle the LED on/off variable between 0 and 1.
        if ledToggle == 0:
            # Set the LEDs to their off color, which is the default if no color is passed.
            myLED1.update()
            if not just1LED:
                myLED2.update()
                myLED3.update()
                myLED4.update()
                myLED5.update()
                myLED6.update()
                myLED7.update()
                myLED8.update()
                myLED9.update()
        else:
            # Set the LEDs to their on color.
            myLED1.update(color.magenta)
            if not just1LED:
                myLED2.update(color.red)
                myLED3.update(color.green)
                myLED4.update(color.blue)
                myLED5.update(color.yellow)
                myLED6.update(color.orange)
                myLED7.update(color.purple)
                myLED8.update(color.red)
                myLED9.update(color.white)
# EOF
