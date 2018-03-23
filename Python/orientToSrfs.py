import rhinoscriptsyntax as rs

def orient_to_srfs():
  objToOri = rs.GetObject("select object to orient")
  ref_srf = rs.GetObject("select a reference surface",8)
  target_srfs = rs.GetObjects("select surfaces to orient objects to",8)
  
  lstRefPts = getOrientationPts(ref_srf)
  
  for srf in target_srfs:
      lstTarPts = getOrientationPts(srf)
      objCopy = rs.CopyObject(objToOri)
      rs.OrientObject(objCopy,lstRefPts,lstTarPts)

def getOrientationPts(ref_srf):
    ptO = EvaluateSurfaceParam(ref_srf,0.5,0.5)
    ptU = EvaluateSurfaceParam(ref_srf,1,0.5)
    ptV = EvaluateSurfaceParam(ref_srf,0.5,1)
    
    pt_O = rs.AddPoint(ptO)
    pt_U = rs.AddPoint(ptU)
    pt_V = rs.AddPoint(ptV)
    
    rs.ObjectColor(pt_O,(255,0,0))
    rs.ObjectColor(pt_U,(0,255,0))
    rs.ObjectColor(pt_V,(0,0,255))
    
    lstPts = []
    lstPts.append(ptO)
    lstPts.append(ptU)
    lstPts.append(ptV)
    return lstPts

def EvaluateSurfaceParam(ref_srf,u_val,v_val):
    normalized = (u_val, v_val)
    parameter = rs.SurfaceParameter(ref_srf, normalized)
    
    print "Surface parameter: ", parameter
    
    return rs.EvaluateSurface(ref_srf,parameter[0],parameter[1])

orient_to_srfs()