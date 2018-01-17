import rhinoscriptsyntax as rs

def scaleY():
    objs = rs.GetObjects();
    if objs:
        for obj in objs:
            if obj:
                objCen = rs.SurfaceAreaCentroid(obj);
                if objCen: 
                    objCenPoint = rs.AddPoint(objCen[0]);
                    rs.ScaleObject(obj,objCenPoint,(1,2,1));
                    rs.DeleteObject(objCenPoint);
    

scaleY();
