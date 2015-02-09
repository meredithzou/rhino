import sys
for directory in sys.path:
    print directory
    
sys.path.append("/cygdrive/c/Program Files/Rhinoceros 5 (64-bit)/Plug-ins/IronPython/Lib")
sys.path.append("/cygdrive/c/Users/zoum/AppData/Roaming/McNeel/Rhinoceros/5.0/Plug-ins/IronPython (814d908a-e25c-493d-97e9-ee3861957f49)/settings/lib")
sys.path.append("/cygdrive/c/Users/zoum/AppData/Roaming/McNeel/Rhinoceros/5.0/scripts")
print("---------------------------")
for directory in sys.path:
    print directory
    
print("---------------------------")
import rhinoscriptsyntax as rs

p0 = [10, 20, 0]
p1 = [11, 20, 0]
p2 = [10, 21, 0]
plane = rs.PlaneFromPoints(p0, p1, p2)

rs.AddPlaneSurface(plane, 20, 30)