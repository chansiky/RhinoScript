import rhinoscriptsyntax as rs

def boolUnionList(objs):
    for obj in objs:
        rs.Prompt(obj);


def massBoolUnion():
    objs = rs.GetObjects("select objects to union:",rs.filter.polysurface);
    if objs:
        rs.Prompt("got Objects");
        boolUnionList(objs);


massBoolUnion();