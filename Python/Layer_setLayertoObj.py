import rhinoscriptsyntax as rs

def text_background_color():
    lay_curr = rs.CurrentLayer()
    col_lay = rs.LayerColor(lay_curr)
    rs.AppearanceColor(12,col_lay)
    
    
obj_sel = rs.GetObject("select object to set current layer",0,True)
lay_sel = rs.ObjectLayer(obj_sel)
rs.CurrentLayer(lay_sel)
    
text_background_color()