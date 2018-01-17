import rhinoscriptsyntax as rs




def lineClosestPoints():
    points = rs.GetObjects("select points to connect:",rs.filter.point);
    if points: rs.Prompt("points exist")
    findClosestPointPairs();
    



lineClosestPoints()
    

    