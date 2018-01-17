import rhinoscriptsyntax as rs

def Area_Brep2D():
    points = rs.GetObjects("select points to connect:",rs.filter.point);
    if points: rs.Prompt("points exist")
    findClosestPointPairs();
    
    
def getClosedBrep(str):
    brep = rs.GetObject(str,rs.filter.polysurface);
    if brep == rs.IsBrep.func_closure
    