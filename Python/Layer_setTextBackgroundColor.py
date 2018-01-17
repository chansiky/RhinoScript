import rhinoscriptsyntax as rs
from System.Drawing import Color

def text_background_color():
    lay_curr = rs.CurrentLayer()
    col_lay = rs.LayerColor(lay_curr)
    rs.AppearanceColor(12,col_lay)
    
text_background_color()

