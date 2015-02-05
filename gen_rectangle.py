import rhinoscriptsyntax as rs

p0 = [10, 20, 0]
p1 = [11, 20, 0]
p2 = [10, 21, 0]
plane = rs.PlaneFromPoints(p0, p1, p2)

rs.AddPlaneSurface(plane, 20, 30)

#rs.AddMesh([p0, p1, p2], [[0, 1, 2]])
