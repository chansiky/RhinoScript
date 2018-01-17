import rhinoscriptsyntax as rs

def main():
    pts = rs.GetObjects("select points you want to add sphere to: ", 1,True,True);
    rad = rs.GetReal("radius of spheres");
    for pt in pts:
        rs.AddSphere(pt,rad);

main();