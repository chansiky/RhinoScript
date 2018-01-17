import rhinoscriptsyntax as rs

def recursiveOffset(crv,point,dist,count,i):
    if (i < count):
        i += 1;
        crvOff = rs.OffsetCurve(crv,point,dist);
        recursiveOffset(crvOff,point,dist,count,i);

def getCount(midpoint):
    line = rs.GetLine(1,midpoint,"Draw line of offset, with endpoint at offset directionn:");
    ptEnd = line[1];
    ptStart = line[0];
    dist = rs.Distance(ptEnd, ptStart);
    distOffset = rs.GetReal("Offset Distance:");
    count = (dist/distOffset);
    count = int(count);
    return (count,ptEnd,distOffset);

def main():
    crv = rs.GetObject("Select Curve to offset repeatedly:",4);
    ptCrvMid = rs.CurveMidPoint(crv);
    #### Use the following lines to offset by count
    #dir = rs.GetPoint("Direction of Offset:");
    #count = rs.GetInteger("Number of Offsets:");
    tupCount = getCount(ptCrvMid);
    recursiveOffset(crv,tupCount[1],tupCount[2],tupCount[0],0);

main();