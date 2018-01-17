import rhinoscriptsyntax as rs

obj_get = rs.GetObject("select object on layer to rename:",0,True)
lay_name = rs.ObjectLayer(obj_get)
lay_new_name = rs.GetString('Layer name is currently: "' + lay_name + '".  Enter new name or Esc to cancel')

if obj_get:
    if lay_new_name:
        rs.RenameLayer(lay_name,lay_new_name)
        print 'layer name change changed to "'+ lay_new_name + '".'
    else:
        print "layer name change cancelled."