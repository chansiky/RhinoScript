import rhinoscriptsyntax as rs

def selLayerSelected():
    objs = rs.GetObjects("Select objects on layers to select:",0,True,True)
    arrLay = []
    rs.EnableRedraw(False)
    for obj in objs:
        try:
            lay = rs.ObjectLayer(obj)
            arrLay.append(lay)
        except Exception:
            pass
    for lay in arrLay:
        try:
            rs.SelectObjects(rs.ObjectsByLayer(lay))
        except Exception:
            pass
    rs.EnableRedraw(True)
    
    rs.GetPoint(

selLayerSelected()