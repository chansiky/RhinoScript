import rhinoscriptsyntax as rs

def cutPlate():
    center = rs.GetPoint("center point:")
    
    radius = 250
    
    circle = rs.AddCircle(center,radius)
    rs.AddPlanarSrf(circle)
    rs.DeleteObject(circle)
    
cutPlate()
