import rhinoscriptsyntax as rs

settings = Rhino.DocObjects.ObjectEnumeratorSettings()
ltmp = scriptcontext.doc.Objects.GetObjectList(settings)

id_list = []
for item in ltmp:
    id_list.append(item.Id)

print id_list[0]
print id_list[1]

print 'last'
new_list = rs.BooleanDifference(id_list[0], id_list[1])
for item in new_list:
    print item
