import rhinoscriptsyntax as rs
from math import *

#rs.EnableRedraw (False)

rs.AddPoint( [0,0,0] )

rs.AddSphere( [10,0,0], 2)
"""
for i in range(0, 100):
    if (i < 50):
        rs.AddPoint( [sin(i),i,0] )
    else:
        rs.AddSphere( [sin(i),i,0], 1 )
"""
#rs.EnableRedraw (True)

def myFunction(obj, trans):
    rs.MoveObject(obj, trans)
    print("move successful!")

selObj = rs.GetObject("Pick a point from the screen", 1)

myFunction(selObj, [10,0,0] )