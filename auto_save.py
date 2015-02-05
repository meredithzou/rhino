import rhinoscriptsyntax as rs
import Rhino
import scriptcontext

settings = Rhino.DocObjects.ObjectEnumeratorSettings()
ltmp = scriptcontext.doc.Objects.GetObjectList(settings)

rs.SelectObjects(ltmp)

pathh = "Z:\\automatic2.obj"
command_line = '_-export "{0}" _Enter _Enter _Enter'.format(pathh)
print command_line
rs.Command(command_line)
