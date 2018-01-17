import rhinoscriptsyntax as rs;

def massOffset():
    crvs = rs.GetObjects("Select curves to offset:",4);
    ptDir = rs.GetPoint("Select direction of offset:");
    dist = rs.GetReal("Offset distance:");
    arrCrvs = [];
    i = 0;
    for crv in crvs:
        arrCrvs[i] = rs.OffsetCurve(crv,ptDir,dist);
        i += 1;

def massOffsetBothSidesFill():
    crvs = rs.GetObjects("Select curves to offset:",4,True,True);
    ptDir = rs.GetPoint("Select direction of offset:");
    ptDirOp = rs.GetPoint("Select direction of the opposite side for offset:");
    dist = rs.GetReal("Offset distance:");
    arrCrvs = [];
    arrCrvsOp = [];
    arrCrvsStartClose = [];
    arrCrvsEndClose = [];
    i = 0;
    rs.EnableRedraw(False);
    for crv in crvs:
        arrCrvs.append(rs.OffsetCurve(crv,ptDir,dist));
        arrCrvsOp.append(rs.OffsetCurve(crv,ptDirOp,dist));
        arrCrvsStartClose.append(rs.AddLine(rs.CurveEndPoint(arrCrvs[i]),rs.CurveEndPoint(arrCrvsOp[i])));
        arrCrvsEndClose.append(rs.AddLine(rs.CurveStartPoint(arrCrvs[i]),rs.CurveStartPoint(arrCrvsOp[i])));
        i += 1;
    rs.EnableRedraw(False);

massOffsetBothSidesFill();