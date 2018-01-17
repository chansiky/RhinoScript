import rhinoscriptsyntax as rs

lay_Curr = rs.CurrentLayer()

obj_sel = rs.SelectedObjects()

if (obj_sel):
    rs.ObjectLayer(obj_sel,lay_Curr)
    rs.UnselectAllObjects()