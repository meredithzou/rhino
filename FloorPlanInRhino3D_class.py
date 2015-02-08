from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Input import *
from Rhino.Commands import *
from scriptcontext import sc
import rhinoscriptsyntax as rs


"""
class FloorPlanInRhino3D:
    def __init__(self):
        print ("Hello Ming!")

	def redraw(self):
		sc.Views.Redraw()

	def clear(self):
		objs = rs.AllObjects()
		rs.DeleteObjects(objs)

	def addWall(self, corners, thickness):
		pts = [ Point3d(x) for x in corners]

		outerWall = PolylineCurve(pts)
		innerWall = outerWall.Offset(Plane.WorldXY, -thickness,
			sc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)

		doc.Objects.AddCurve(outerWall)
		print len(innerWall)

	def testCase(self):
		print ("Hello in TestCase")
		clear()

		corners = [
		[0,0,0]
		,[10,0,0]
		,[10,5,0]
		,[15,5,0]
		,[15,20,0]
		,[11,20,0]
		,[11,18,0]
		,[4,18,0]
		,[4,20,0]
		,[0,20,0]
		,[0,0,0]
		]
		thickness = 1.0
		addWall(corners, thickness)

		redraw()
"""
"""
if __name__ == '__main__':
	fp = FloorPlanInRhino3D()
	fp.testCase()
"""

"""
def redraw():
    sc.Views.Redraw()

def clear():
    objs = rs.AllObjects()
    rs.DeleteObjects(objs)

def addWall(self, corners, thickness):
    pts = [ Point3d(x) for x in corners]

    outerWall = PolylineCurve(pts)
    innerWall = outerWall.Offset(Plane.WorldXY, -thickness,
    sc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)

    sc.Objects.AddCurve(outerWall)
    print len(innerWall)

def testCase(self):
    print ("Hello in TestCase")
    clear()
    
    corners = [
    [0,0,0]
    ,[10,0,0]
    ,[10,5,0]
    ,[15,5,0]
    ,[15,20,0]
    ,[11,20,0]
    ,[11,18,0]
    ,[4,18,0]
    ,[4,20,0]
    ,[0,20,0]
    ,[0,0,0]
    ]
    thickness = 1.0
    addWall(corners, thickness)
    redraw()

print ("Hello Ming")

if __name__ == '__main__':
    print( "Hello Ming")
    testCase()

""""""
def redraw():
    sc.Views.Redraw()

def clear():
    objs = rs.AllObjects()
    rs.DeleteObjects(objs)

def addWall(self, corners, thickness):
    pts = [ Point3d(x) for x in corners]

    outerWall = PolylineCurve(pts)
    innerWall = outerWall.Offset(Plane.WorldXY, -thickness,
    sc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)

    sc.Objects.AddCurve(outerWall)
    print len(innerWall)

def testCase(self):
    print ("Hello in TestCase")
    clear()
    
    corners = [
    [0,0,0]
    ,[10,0,0]
    ,[10,5,0]
    ,[15,5,0]
    ,[15,20,0]
    ,[11,20,0]
    ,[11,18,0]
    ,[4,18,0]
    ,[4,20,0]
    ,[0,20,0]
    ,[0,0,0]
    ]
    thickness = 1.0
    addWall(corners, thickness)
    redraw()

print ("Hello Ming")

if __name__ == '__main__':
    print( "Hello Ming")
    testCase()

""""""
def redraw():
    sc.Views.Redraw()

def clear():
    objs = rs.AllObjects()
    rs.DeleteObjects(objs)

def addWall(self, corners, thickness):
    pts = [ Point3d(x) for x in corners]

    outerWall = PolylineCurve(pts)
    innerWall = outerWall.Offset(Plane.WorldXY, -thickness,
    sc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)

    sc.Objects.AddCurve(outerWall)
    print len(innerWall)

def testCase(self):
    print ("Hello in TestCase")
    clear()
    
    corners = [
    [0,0,0]
    ,[10,0,0]
    ,[10,5,0]
    ,[15,5,0]
    ,[15,20,0]
    ,[11,20,0]
    ,[11,18,0]
    ,[4,18,0]
    ,[4,20,0]
    ,[0,20,0]
    ,[0,0,0]
    ]
    thickness = 1.0
    addWall(corners, thickness)
    redraw()

print ("Hello Ming")

if __name__ == '__main__':
    print( "Hello Ming")
    testCase()

"""