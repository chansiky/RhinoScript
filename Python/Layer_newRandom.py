import rhinoscriptsyntax as rs
from System.Drawing import Color
import random
def randomcolor():

    red = int(255*random.random())
    green = int(255*random.random())
    blue = int(255*random.random())

    return Color.FromArgb(red,green,blue)
    
    
def text_background_color():
    lay_curr = rs.CurrentLayer()
    col_lay = rs.LayerColor(lay_curr)
    rs.AppearanceColor(12,col_lay)
    

def lay_rand():

    if rs.IsLayer("Temporary"):
        str_rand = str(random.randrange(0, 9999999999))
        print str_rand
        if not rs.IsLayer(str_rand):
            lay_temp = rs.AddLayer(str_rand,randomcolor())
            rs.ParentLayer(lay_temp,"Temporary")
            rs.CurrentLayer(lay_temp)
            return lay_temp
        else:
            lay_rand();
            print "The random already exists, rerandomizing"
    else:
        rs.AddLayer("Temporary",Color.DarkViolet)
        lay_rand();
lay_temp = lay_rand();   

obj_sel = rs.SelectedObjects()

if (obj_sel):
    rs.ObjectLayer(obj_sel,lay_temp)
    rs.UnselectAllObjects()

text_background_color()
#for obj in obj_sel:
#    rs.ObjectLayer(obj,lay_temp)

