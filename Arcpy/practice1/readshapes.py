# reading shapefile shapes and records

import shapefile



sf = shapefile.Reader("c:/temp/class06/states.shp")
shapes = sf.shapes()

# read shapes
# Georgia happens to be shape 42 in the list
shapes[42].shapeType
shapes[42].bbox
s = shapes[42]
print s.bbox
print s.parts
print s.points
print s.points[0]

# read records and fields

fields = sf.fields
records = sf.records()
for r in records:
    print r[0:3]
r = record[42]
print r



                      