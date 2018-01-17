import rhinoscriptsyntax as rs

def getAllEndPoints(crvs):
    arrPoints = []
    i = 0
    for crv in crvs:
        arrPoints.append(rs.CurveEndPoint(crv))
        arrPoints.append(rs.CurveStartPoint(crv))
    return arrPoints      

def MaxDist(point,points):
    maxDist = 0;
    for point_i in points:
        distPointToI = rs.Distance(point,point_i)
        if distPointToI > maxDist:
            maxDist = distPointToI
    return maxDist

def pointPairExists():
    #code to be written.  for now, seldup and delete.
    return False

def findClosestEndPoint(point, points):
    closestPtIndex = 0
    dist = MaxDist(point,points)
    i = 0
    for point_i in points:
        distPointToI = rs.Distance(point,point_i)
        if distPointToI < dist and distPointToI != 0:
            dist = distPointToI
            closestPtIndex = i
        i += 1
    return points[closestPtIndex]

def connectClosestPoint(point, points):
    closestPt = findClosestEndPoint(point, points)
    if not pointPairExists():
        rs.AddLine(point,closestPt)

def connectEndpoints(crvs):
    points = getAllEndPoints(crvs)
    for crv in crvs:
        point = rs.CurveEndPoint(crv)
        connectClosestPoint(point,points)
        point = rs.CurveStartPoint(crv)
        connectClosestPoint(point,points)

def main():
    crvs = rs.GetObjects("Select curves to connect:",4,True)
    connectEndpoints(crvs)
    print("Script is incomplete.  Please selDup and delete extra curves")

main();