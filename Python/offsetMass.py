import rhinoscriptsyntax as rs;

def massOffset():
    crvs = rs.GetObjects("Select curves to offset:",4);
    ptDir = rs.GetPoint("Select direction of offset:");
    dist = rs.GetReal("Offset distance:");
    for crv in crvs:
        rs.OffsetCurve(crv,ptDir,dist);
        
massOffset();