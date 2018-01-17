import rhinoscriptsyntax as rs

layer_names = rs.LayerNames()
x = 0
for name in layer_names:
    x = 0
    for name_child_test in layer_names:
        if rs.IsLayerChildOf(name,name_child_test):
            x += 1
    if x > 0:
        print name