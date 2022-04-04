# Using an Arduino with Python LESSON 12: Parameterised Model Design for 3D Graphics.
#  -> Sub Task B - Parameterising a Crosshead Screw.
# https://www.youtube.com/watch?v=DcOT3gtVG8Y
# https://toptechboy.com/

# Internet References:
# https://www.glowscript.org/docs/VPythonDocs/index.html

from vpython import *
import numpy as np

# Focus on 1 screw at the origin.
just1Screw = False
# Use the Lesson 11 drawScrew function definition?
useL11Screw = False

# vPython refresh rate.
vPythonRefreshRate = 100
# XYZ Scale Axis toggle.
showAxis = False

# A place on which to put our things...
canvas(title = "<b><i>Arduino with Python - Parameterising a Crosshead Screw!</i></b>", background = color.cyan, width = 800, height = 600)

# An XYZ axis to help us get our bearings.
if showAxis:
    arrow(color = color.blue, round = True, pos = vector(-0.5, 0, 0), axis = vector(1, 0, 0), shaftwidth = 0.02) # X axis.
    arrow(color = color.blue, round = True, pos = vector(0, -0.5, 0), axis = vector(0, 1, 0), shaftwidth = 0.02) # Y axis.
    arrow(color = color.blue, round = True, pos = vector(0, 0, -0.5), axis = vector(0, 0, 1), shaftwidth = 0.02) # Z axis.

# A bag of small screws for us to draw exactly where we like - this is the Lesson 11 version of this function.
def drawScrew(sPos = vector(0, 0, 0)):
    cylinder(color = color.black, opacity = 1, pos = vector(0, 0, 0.05) + sPos, axis = vector(0, 0, 0.04), radius = 0.06) # Head.
    cylinder(color = color.black, opacity = 1, pos = vector(0, 0, 0) + sPos, axis = vector(0, 0, 0.05), radius = 0.03)    # Shaft.
    cone(color = color.black, opacity = 1, pos = vector(0, 0, 0) + sPos, axis = vector(0, 0, -0.25), radius = 0.03)       # Thread.
    slotAngle = np.random.rand() * np.pi / 2 # An angle between 0 and 90 degrees.
    screwCross1 = box(color = vector(0.8, 0.8, 0.8), opacity = 1, pos = vector(0, 0, 0.0801) + sPos, size = vector(0.1, 0.02, 0.02)) # Cross pt1.
    screwCross1.rotate(angle = slotAngle, axis = vector(0, 0, 1))               # Randomly rotate this part of the cross.
    screwCross2 = box(color = vector(0.8, 0.8, 0.8), opacity = 1, pos = vector(0, 0, 0.0801) + sPos, size = vector(0.1, 0.02, 0.02)) # Cross pt2.
    screwCross2.rotate(angle = slotAngle + np.pi / 2, axis = vector(0, 0, 1))   # Add 90 degrees for the other part of the cross.

# A bag of small screws for us to draw exactly where we like - a fully parameterised version.
def drawScrewFPV(sPos = vector(0, 0, 0), scale = 1, axis = 'z'):
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
    cylinder(color = color.black, opacity = 1, radius = scale * 0.06,
             pos = vector(0, 0, 0) + sPos,
             axis = vector(xScale * 0.04, yScale * 0.04, zScale * 0.04)) # Head.
    cylinder(color = color.black, opacity = 1, radius = scale * 0.03,
             pos = vector(xScale * -0.05, yScale * -0.05, zScale * -0.05) + sPos,
             axis = vector(xScale * 0.05, yScale * 0.05, zScale * 0.05)) # Shaft.
    cone(color = color.black, opacity = 1, radius = scale * 0.03,
         pos = vector(xScale * -0.05, yScale * -0.05, zScale * -0.05) + sPos,
         axis = vector(xScale * -0.25, yScale * -0.25, zScale * -0.25))  # Thread.
    slotAngle = np.random.rand() * np.pi / 2 # An angle between 0 and 90 degrees.
    screwCross1 = box(color = vector(0.8, 0.8, 0.8), opacity = 1,
                      pos = vector(xScale * 0.0301, yScale * 0.0301, zScale * 0.0301) + sPos,
                      size = vector((xScale * 0.02) + (yScale * 0.1)  + (zScale * 0.02),
                                    (xScale * 0.02) + (yScale * 0.02) + (zScale * 0.1),
                                    (xScale * 0.1)  + (yScale * 0.02) + (zScale * 0.02)))    # Cross pt1.
    screwCross1.rotate(angle = slotAngle, axis = vector(xScale, yScale, zScale))             # Randomly rotate this part of the cross.
    screwCross2 = box(color = vector(0.8, 0.8, 0.8), opacity = 1,
                      pos = vector(xScale * 0.0301, yScale * 0.0301, zScale * 0.0301) + sPos,
                      size = vector((xScale * 0.02) + (yScale * 0.1)  + (zScale * 0.02),
                                    (xScale * 0.02) + (yScale * 0.02) + (zScale * 0.1),
                                    (xScale * 0.1)  + (yScale * 0.02) + (zScale * 0.02)))    # Cross pt2.
    screwCross2.rotate(angle = slotAngle + np.pi / 2, axis = vector(xScale, yScale, zScale)) # Add 90 degrees for the other part of the cross.

# Draw a selection of crosshead screws.
if useL11Screw:
    myScrew1 = drawScrew(vector(0.00, 0.00, 0.00))
    if not just1Screw:
        myScrew2 = drawScrew(vector(-1.00, 0.50, -0.50))
        myScrew3 = drawScrew(vector(0.00, 0.50, 0.00))
        myScrew4 = drawScrew(vector(1.00, 0.50, 0.50))
        myScrew5 = drawScrew(vector(-1.00, -0.50, 0.50))
        myScrew6 = drawScrew(vector(0.00, -0.50, 0.00))
        myScrew7 = drawScrew(vector(1.00, -0.50, -0.50))
        myScrew8 = drawScrew(vector(-0.50, 0.00, 0.00))
        myScrew9 = drawScrew(vector(0.50, 0.00, 0.00))
else:
    myScrew1 = drawScrewFPV(vector(0.00, 0.00, 0.00), 0.5, 'z')
    if not just1Screw:
        myScrew2 = drawScrewFPV(vector(-1.00, 0.50, -0.50), 1, 'x')
        myScrew3 = drawScrewFPV(vector(0.00, 0.50, 0.00), 1.5, 'y')
        myScrew4 = drawScrewFPV(vector(1.00, 0.50, 0.50), 2, 'z')
        myScrew5 = drawScrewFPV(vector(-1.00, -0.50, 0.50), -1, 'z')
        myScrew6 = drawScrewFPV(vector(0.00, -0.50, 0.00), -1.5, 'y')
        myScrew7 = drawScrewFPV(vector(1.00, -0.50, -0.50), -2, 'x')
        myScrew8 = drawScrewFPV(vector(-0.50, 0.00, 0.00), -0.5, 'y')
        myScrew9 = drawScrewFPV(vector(0.50, 0.00, 0.00), 0.5, 'y')

# An infinite loop: When is True, True? It is always True!
while True:
    rate(vPythonRefreshRate) # The vPython rate command is obligatory in animation loops.

# EOF
