from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Input import *
from Rhino.Commands import *
from scriptcontext import doc
import rhinoscriptsyntax as rs

class FloorPlanInRhino3D:
	def __init__(self):
		print ("Start Building 3D Floor Plan!")

	def redraw(self):
		doc.Views.Redraw()

	def clear(self):
		objs = rs.AllObjects()
		rs.DeleteObjects(objs)

	def addWall(self, corners, thickness):
		print ("Building Wall...")
		pts = [ Point3d(x[0],x[1],x[2]) for x in corners]
		#ptsUp = [ Point3d(x[0],x[1],x[2]+10) for x in corners]

		outerWall = PolylineCurve(pts)
		innerWall = outerWall.Offset(Plane.WorldXY, -thickness,
			doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)[0]
		#outerWallUp = PolylineCurve(ptsUp)
		#plane = Plane.WorldXY
		#plane.Translate(Vector3d(0,0,10))
		#innerWallUp = outerWall.Offset(plane, -thickness,
			#doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)[0]
			
		doc.Objects.AddCurve(outerWall)
		doc.Objects.AddCurve(innerWall)
		#doc.Objects.AddCurve(outerWallUp)
		#doc.Objects.AddCurve(innerWallUp)		
			
		#ext = Extrusion.Create(innerWall[0], 10, True)
		#doc.Objects.AddMesh(ext.GetMesh())
		
		suf = Surface.CreateExtrusion(innerWall, Vector3d(0,0,10))
		#doc.Objects.AddSurface(suf)
		sufo = Surface.CreateExtrusion(outerWall, Vector3d(0,0,10))
		#doc.Objects.AddSurface(sufo)
		
		#brep = Brep()
		#brep.AddEdgeCurve(innerWall)
		#brep.AddEdgeCurve(outerWall)
		#Brep.
		#walls = Brep.CreateFromLoft([innerWall,outerWall],Point3d(0,0,0),Point3d(0,0,10),LoftType.Tight,False)
		btmWall = Brep.CreateFromLoft([innerWall,outerWall],Point3d.Unset,Point3d.Unset,LoftType.Tight,False)[0]
		doc.Objects.AddBrep(btmWall)
		upWall = btmWall
		upWall.Translate(0,0,10)
		doc.Objects.AddBrep(upWall)
		inWall = Brep.CreateFromSurface(suf)
		outWall = Brep.CreateFromSurface(sufo)
		doc.Objects.AddBrep(inWall)
		doc.Objects.AddBrep(outWall)
		
		#oWall = Brep.CreateFromLoft([outerWall],Point3d(0,0,0),Point3d(0,0,10),LoftType.Tight,False)[0]
		#doc.Objects.AddBrep(oWall)
		#crvs = rs.AllObjects()
		
		#crvids = rs.GetObjects(message="select curves to loft", filter=rs.filter.curve, minimum_count=2)
		#if not crvids: return
		#rs.AddLoftSrf(object_ids=crvids, loft_type = 3) #3 = tight
		
		#rs.AddLoftSrf(object_ids=crvs, loft_type = 3)
		self.redraw()

	def testCase(self):
		self.clear()

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
		thickness = 0.8
		self.addWall(corners, thickness)

if __name__ == '__main__':
	fp = FloorPlanInRhino3D()
	fp.testCase()