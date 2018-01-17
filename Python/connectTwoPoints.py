import rhinoscriptsyntax as rs

def connectTwoPoints():
    pts = rs.GetObjects("select points")

    rs.AddLine(pts[0], pts[1])

connectTwoPoints()