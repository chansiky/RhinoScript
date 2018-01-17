import rhinoscriptsyntax as rs

def sweepMult():
    crvProfiles = rs.GetObjects("select Curves to Sweep", 4);
    #get rail profile
    crvRail = rs.GetObject("select rail to sweep through",4);
    #for each curve in crvProfiles, sweep the curve
    for crv in crvProfiles:
        if(rs.IsCurve(crv)):
            rs.AddSweep1(crvRail,crv);
sweepMult();