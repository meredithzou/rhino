import rhinoscriptsyntax as rs

p0 = [10, 20, 0]
p1 = [11, 20, 0]
p2 = [10, 21, 0]
plane = rs.PlaneFromPoints(p0, p1, p2)

pol0 = rs.AddPlaneSurface(plane, 20, 30)
#pol1 = rs.AddMesh([[40,30,0],[20,30,0],[35,50,0]],[[0,1,2]])

pol1 = rs.AddSrfPt([[40,30,0],[35,50,0],[20,30,0]])


curve = rs.AddCurve([[0,0,0],[0,0,10]])

pol2 = rs.ExtrudeSurface(pol0, curve)
pol3 = rs.ExtrudeSurface(pol1, curve)

#rs.BooleanDifference(pol2, pol3, True)

rs.DeleteObject(pol0)
rs.DeleteObject(pol1)
