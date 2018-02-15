import rhinoscriptsyntax as rs
from System.Drawing import Color
import random

def randomColor():

    red = int(255*random.random())
    green = int(255*random.random())
    blue = int(255*random.random())

    return Color.FromArgb(red,green,blue)

def setObjectToLayer(objs,layerName):
    rs.EnableRedraw(False);
    if not rs.IsLayer(layerName):
        rs.AddLayer(layerName,randomColor());
#        rs.AddLayer(layerName,Color.LightSlateGray);
    for obj in objs:
        rs.ObjectLayer(obj,layerName);
    rs.EnableRedraw(True);

def prompt():    
    objs = rs.GetObjects("select Objects to set to new layer:",0,True,True,False);
    if objs:
        layerName = rs.GetString("layer name:");
        if layerName:
            setObjectToLayer(objs,layerName);

prompt();
