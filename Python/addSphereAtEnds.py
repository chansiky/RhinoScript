import rhinoscriptsyntax as rs

SPHERE_RADIUS = 25;

def addSphereAtEnds():
    objs = rs.GetObjects("select lines to convert to lights:",rs.filter.curve);
    if objs:
        rs.Prompt("got Objects");
        rs.EnableRedraw(False);
        for obj in objs:
            rs.Prompt("Adding Sphere for obj " + str(obj));
            endPoint = rs.CurveEndPoint(obj);
            startPoint = rs.CurveStartPoint(obj);
            rs.AddSphere(endPoint,SPHERE_RADIUS);
            rs.AddSphere(startPoint,SPHERE_RADIUS);
        rs.EnableRedraw(True);

def addVertLineAtMid():
    objs = rs.GetObjects("select lines you want to add a vertical line at mid", rs.filter.curve);
    vector1 = rs.VectorCreate((0,0,0),(0,0,200));
    
    if objs:
        for obj in objs:
            midPoint = rs.CurveMidPoint(obj);
            midPointMoved = midPoint;
            rs.MoveObject(midPointMoved,vector1);
            rs.AddLine(midPoint,midPointMoved);

#addVertLineAtMid();
#rs.Prompt("hello world");
addSphereAtEnds();