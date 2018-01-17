import rhinoscriptsyntax as rs

def setObjectToLayer(objs,layerName):
    if not rs.IsLayer(layerName):
        rs.AddLayer(layerName);
    for obj in objs:
        rs.ObjectLayer(obj,layerName);

def prompt():    
    objs = rs.GetObjects("select Objects to set to new layer:",0,True,False,True);
    layerName = rs.GetString("layer name:");
    setObjectToLayer(objs,layerName);

prompt();
rs.UnselectAllObjects();