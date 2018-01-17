import rhinoscriptsyntax as rs

#sel objects to sort
#get values of two surfaces to check for tolerance
#prompt the user for tolerance
#sort objects based on the surface areaedit

def getSurfaceArea(message):
    surface = rs.GetObject(message);
    val = rs.SurfaceArea(surface);
    return val[0];

def sortSurfaces(srfs,tol):
    srfToSelect = [];
    i = 0;
    for srf in srfs:
        if rs.SurfaceArea(srf)[0] < tol:
            srfToSelect.append(srf);
            rs.Prompt("Sorting: " + str(i) + "/" + str(len(srfs)));
            i += 1;
    return srfToSelect;

def main():
    srfs = rs.GetObjects("Select objects to sort",24,True,True,False);
    lowVal = getSurfaceArea("Select reference surface 1");
    highVal= getSurfaceArea("Select reference surface 2");
    tol = rs.GetReal("Enter selection tolerance (ref values: (" + str(lowVal) + " , " + str(highVal) + ")");
    rs.Prompt("Sorting Surfaces");
    rs.EnableRedraw(False);
    selsrf = sortSurfaces(srfs,tol);
    i=0;
    rs.SelectObjects(selsrf);
#    for srf in selsrf:
#        rs.SelectObject(srf);
#        rs.Prompt("Selecting: " + str(i) + "/" + str(len(selsrf)));
#        i+=1;
    rs.EnableRedraw(True);

main();
