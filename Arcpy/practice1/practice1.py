
import os
import arcpy as ap

# substitute your individual z drive (or other) path
#    to the location to which you copied the class0920 folder
workingdir = "z:\\bdrummond\\class0920"

# sets Python working directory
os.chdir(workingdir)

# sets default arcpy workspace
ap.env.workspace = workingdir

# uses Clip_analysis tool
ap.Clip_analysis("roads.shp", "georgia.shp", "garoads.shp")
# use Google to search for "arcgis desktop clip" to get help for clip
# find the section named Syntax and review the clip command's syntax

# uses Buffer_analysis tool
ap.Buffer_analysis("garoads.shp", "roadbuff1.shp", "10000 METERS")
# use Google to search for "arcgis desktop buffer" to review buffer syntax

# adds optional dissolve parameter, with empty strings for omitted parameters
ap.Buffer_analysis("garoads.shp", "roadbuff2.shp", "10000 METERS", "", "", "ALL")

# adds optional dissolve parameter by specifying parameter name
ap.Buffer_analysis("garoads.shp", "roadbuff3.shp", "10000 METERS", dissolve_option="All")

# uses Buffer_analysis tool and stores result
bresult = ap.Buffer_analysis("garoads.shp", "roadbuff4.shp", "10000 METERS")

print bresult
# also try bresult. to see a list of bresult properties

# prints messages from last tool execution
print ap.GetMessages()

# gets a complex result from GetCount
roadresult = ap.GetCount_management("roads.shp")
print roadresult

# uses getOutput to pull the actual count as a string
# int function converts to an integer
roadcount = (roadresult.getOutput(0))
print roadcount

# prints messages from last tool execution
print ap.GetMessages()

# prints the last message only
print ap.GetMessage(ap.GetMessageCount()-1)
# prints the maximum serverity among messages
print ap.GetMaxSeverity()

# uses Exists function to test if file exists
ap.Exists("utm83.prj")

# creates a complex arcpy spatial reference object
utmfile = "utm83.prj"
sref = ap.SpatialReference(utmfile)
# try to print object; can't access except for it's methods
print sref
# list an object's properties and methods
dir(sref)
# show a property's type
type(sref.longitude)
# identify a method
type(sref.setZDomain)

# pulls property values of the spatial reference object
sref.name
sref.centralMeridian
sref.falseEasting

# in interpreter, type an object name plus a period to see properties
sref.

# lists all feature classes in current directory
ap.ListFeatureClasses()
for fc in ap.ListFeatureClasses():
	print fc

# list feature classes with wildcard
ap.ListFeatureClasses("g*.*")

# lists only point feature classes
ap.ListFeatureClasses("", "point")

# list all fields
for f in ap.ListFields("garoads.shp"):
	print f.name


# list only string fields
for f in ap.ListFields("garoads.shp", "", "STRING"):
	print f.name

# describe the attributes of a dataset
desc = ap.Describe("garoads.shp")
desc.dataType
desc.name
desc.Basename
desc.file
desc.dataType
desc.path

# Accessing geometry with cursors

# Access the length of each feature
fc = 'garoads.shp'
cursor = ap.da.SearchCursor(fc,["SHAPE@LENGTH"])
length = 0
for row in cursor: length = length + row[0]
print length

# Access a tuple with centroid x and y coordinates
# Note: a tuple is like a list, but it can not be altered
with ap.da.SearchCursor(fc,["SHAPE@XY"]) as cursor:
 	for row in cursor:
 		print row[0]



# Access each polyline's oid and individual points
with ap.da.SearchCursor(fc,["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "\nOID: ", row[0]
        for point in row[1].getPart(0):
            print point.X, point.Y


# try these command line commands to understand the complex data structure
row
point
row[0]
row[1]
row[1].getPart(0)
row[1].getPart(0)[0]
row[1].getPart(0)[0].X
row[1].getPart(0)[0].Y
row[1].getPart(0)[0].Z

# handles multiple parts
fc = 'hawaii.shp'
with ap.da.SearchCursor(fc,["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "\n\n\nOID: ", row[0]
        partnum = 0
        for part in row[1]:
            print "\nPart number ", partnum
            for point in row[1].getPart(partnum):
                print point.X, point.Y
            partnum = partnum + 1

# separate standalone program
# copy and paste into new script window
# creates polygon shapefile and reads coordinates from text file
import fileinput, arcpy, os

infile = 'points2.txt'
fc = 'newpoly2.shp'
ap.CreateFeatureclass_management('c:/temp/class08', fc, "POLYGON")
cursor = ap.da.InsertCursor(fc, ["Shape@"])
line_array = ap.Array()
point = ap.Point()
for line in fileinput.input(infile):
    point.ID, point.X, point.Y = line.split()
    line_array.add(point)
polygon = ap.Polygon(line_array)
cursor.insertRow([polygon])
fileinput.close()
del cursor

