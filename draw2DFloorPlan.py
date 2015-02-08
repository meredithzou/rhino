"""
import rhinoscriptsyntax as rs
import Rhino

plane = rs.WorldXYPlane()

obj = rs.AddRectangle( plane, 5.0, 15.0 )


obj = rs.GetObject("Select a curve", rs.filter.curve)

if rs.IsCurve(obj):

    obj2 = rs.OffsetCurve( obj, [0,0,0], 1.0 )

print obj
print obj2
"""
"""
pts = [[0,0,0], [0,10,0], [10,10,0], [10,0,0]]
rs.AddPolyline(points)

Rhino.Commands(
"""


from Rhino import *
from Rhino.DocObjects import *
from Rhino.Geometry import *
from Rhino.Input import *
from Rhino.Commands import *
from scriptcontext import doc
import rhinoscriptsyntax as rs
 
def RunCommand():
    
  """
  rs, obj_ref = RhinoGet.GetOneObject("Select Curve", False, ObjectType.Curve)
  print obj_ref
  if rs <> Result.Success:
    return rs
  curve = obj_ref.Curve()
  if curve == None:
    return Result.Nothing
  """
  existObjs = rs.AllObjects()
  rs.DeleteObjects(existObjs)

  """
  pts= [
  Point3d(0,0,0)
  ,Point3d(10,0,0)
  ,Point3d(10,10,0)
  ,Point3d(0,10,0)
  ,Point3d(0,0,0)
  ]
  """
  pts= [
  Point3d(0,0,0)
  ,Point3d(10,0,0)
  ,Point3d(10,5,0)
  ,Point3d(15,5,0)
  ,Point3d(15,20,0)
  ,Point3d(11,20,0)
  ,Point3d(11,18,0)
  ,Point3d(4,18,0)
  ,Point3d(4,20,0)
  ,Point3d(0,20,0)
  ,Point3d(0,0,0)
  ]
  
  #curves = curve.Offset(point, Vector3d.ZAxis, 1.0, 
    #doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)
    
  polycurve = PolylineCurve(pts)
  doc.Objects.AddCurve(polycurve)
  
  curves = polycurve.Offset(Plane.WorldXY, -1.0, 
    doc.ModelAbsoluteTolerance, CurveOffsetCornerStyle.Sharp)
 
  for offset_curve in curves:
    doc.Objects.AddCurve(offset_curve)
  
  doc.Views.Redraw()
  return Result.Success
 
if __name__ == "__main__":
  RunCommand()
  
  
