import rhinoscriptsyntax as rs

def offsetCrvEndPt(curve,dist):
    startPt = rs.CurveStartPoint(curve)
    endPt = rs.CurveEndPoint(curve)
    startSphere = rs.AddSphere(startPt,dist)
    endSphere = rs.AddSphere(endPt,dist)
    #intersect sphere with end
    tupStart = rs.CurveSurfaceIntersection(curve,startSphere)
    tupEnd = rs.CurveSurfaceIntersection(curve,endSphere)
    
    ptSt = rs.AddPoint(tupStart[0][1])
    ptEn = rs.AddPoint(tupEnd[0][1])
    
    rs.DeleteObject(startSphere)
    rs.DeleteObject(endSphere)
    

    return (ptSt,ptEn)

def offsetCurveOnSurface():
    curve = rs.GetObject("sel curve",4)
    num = 100
    points = rs.DivideCurve(curve,num)
    surface = rs.GetObject("sel surface", 8)
    offset_dist = 150
    offset_ptsA0 = []
    offset_ptsA1 = []
    offset_ptsB0 = []
    offset_ptsB1 = []
    
    rs.EnableRedraw(False)
    for point in points:
        parameter =  rs.SurfaceClosestPoint(surface,point)
        crv = rs.ExtractIsoCurve(surface,parameter, 2)
        #create sphere at end
        try:
            offsetEndPtsA = offsetCrvEndPt(crv[0],offset_dist)
            rs.DeleteObject(crv[0])
        except IndexError:
            offsetEndPtsA = None
            
        try:
            offsetEndPtsB = offsetCrvEndPt(crv[1],offset_dist)
            rs.DeleteObject(crv[1])
        except IndexError:
            offsetEndPtsB = None
        #offset_points.append(offset_point)
        
        if not (offsetEndPtsA is None):
            offset_ptsA0.append(offsetEndPtsA[0]);
            offset_ptsA1.append(offsetEndPtsA[1]);
        if not (offsetEndPtsB is None):
            offset_ptsB0.append(offsetEndPtsB[0]);
            offset_ptsB1.append(offsetEndPtsB[1]);
        
    rs.EnableRedraw(True)
    rs.AddInterpCurve(offset_ptsA0)
    rs.AddInterpCurve(offset_ptsA1)
    rs.AddInterpCurve(offset_ptsB0)
    rs.AddInterpCurve(offset_ptsB1)
    
    #rs.AddInterpCrvOnSrf(surface,offset_ptsA0);
    #rs.AddInterpCrvOnSrf(surface,offset_ptsA1);
    #rs.AddInterpCrvOnSrf(surface,offset_ptsB0);
    #rs.AddInterpCrvOnSrf(surface,offset_ptsB1);

offsetCurveOnSurface()
