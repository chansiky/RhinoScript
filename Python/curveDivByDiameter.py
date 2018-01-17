import rhinoscriptsyntax as rs
#needs much improvement

def curveDivByDiameter():
    curve = rs.GetObject("sel curve")
    point = rs.GetPoint("sel point")
    num = rs.GetReal("radius")
    cBool = True
#    ptDir = rs.GetPoint("set Direction:")
    numA= num
    if(cBool):
        numA = num/2
    else:
        numA = num
    circle = rs.AddCircle(point,numA)
    ix = rs.CurveCurveIntersection(curve,circle)
    rs.AddPoint(ix[0][1])
#   or alternatively:
#   rs.AddPoint(ix[0][1])
#   this should get the first intersection curve
#   rs.AddPoint(ix[1][1])
#   this should get the second intersection curve
    arrPt = []
    count = 20
    countConst = count
    #create a check for point by point(x,y,z) value

    while(True != (ix[0][1] in arrPt) and count > 0):
        circle = rs.AddCircle(ix[0][1],num)
        ix = rs.CurveCurveIntersection(curve,circle)
        arrPt.append(rs.AddPoint(ix[0][1]))
        count -= 1
        rs.Prompt(str(countConst-count));
        
    count = 20
    circle = rs.AddCircle(point,numA)
    ix = rs.CurveCurveIntersection(curve,circle)
    while(True != (ix[1][1] in arrPt) and count > 0):
        circle = rs.AddCircle(ix[1][1],num)
        ix = rs.CurveCurveIntersection(curve,circle)
        arrPt.append(rs.AddPoint(ix[1][1]))
        count -= 1
        rs.Prompt(str(countConst-count));

curveDivByDiameter()