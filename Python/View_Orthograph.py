import rhinoscriptsyntax as rs
##changes needed create points based on cplane(get rid of as many 
def Orthographic_Cplane():
    cpln_current = rs.ViewCPlane()
    Bool_Osnap = rs.Osnap()
    point = cpln_current.Origin
    if Bool_Osnap:
        rs.Osnap(False)
    
    rs.Command("_Circle 0,0,0 ")
    
    #
    rs.EnableRedraw(False)
    #
    Circle = rs.LastCreatedObjects()
    if Bool_Osnap:
        rs.Osnap(True)
        
        
    if Circle is None:
            #
        rs.EnableRedraw(True)
    #
        return
            
    if not rs.IsObject(Circle):
        rs.EnableRedraw(True)
        return
    
        
    rs.Command("_Point 0,0,1 ")
    pt_pos = rs.LastCreatedObjects()
    rs.Command("_Point 0,0,-1 ") 
    pt_neg = rs.LastCreatedObjects()
    
    pt_cam = rs.ViewCamera()
    
    dist_pos = rs.Distance(pt_cam,pt_pos)
    dist_neg = rs.Distance(pt_cam,pt_neg)
    
    print pt_cam
    
    Disk = rs.AddPlanarSrf(Circle)
    rs.UnselectAllObjects()
    rs.SelectObjects(Disk)
    
    if dist_pos>dist_neg:
        rs.Command("OrientCameraToSrf _f 0,0,0 _pause")
    else:
        rs.Command("OrientCameraToSrf 0,0,0 _pause")
        
        
    rs.DeleteObjects((pt_pos,pt_neg,Circle,Disk))
    
    rs.ViewProjection(None,1)


Orthographic_Cplane()
rs.EnableRedraw(True)