import rhinoscriptsyntax as rs

def zoomToPoint():
    point = rs.GetPoint();
    pointObj = rs.AddPoint(point);
    rs.SelectObject(pointObj);
    rs.ZoomSelected();
    rs.DeleteObject(pointObj);
    
    
def unselectZoom():
    selObjs = rs.SelectedObjects();
    rs.UnselectObjects(selObjs);
    zoomToPoint();
    rs.SelectObjects(selObjs);
    
unselectZoom();