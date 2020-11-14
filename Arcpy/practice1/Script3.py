import fileinput, arcpy, os

infile = 'c:/temp/points.txt'
fc = 'newpoly3.shp'
arcpy.CreateFeatureclass_management('c:/temp', fc, "POLYGON")
cursor = arcpy.da.InsertCursor(fc, ["Shape@"])
line_array = arcpy.Array()
point = arcpy.Point()
for line in fileinput.input(infile):
    point.ID, point.X, point.Y = line.split()
    line_array.add(point)
polygon = arcpy.Polygon(line_array)
cursor.insertRow([polygon])
fileinput.close()
del cursor


    
    
