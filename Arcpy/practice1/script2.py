

fc = 'hawaii.shp'

with arcpy.da.SearchCursor(fc,["OID@", "SHAPE@"]) as cursor:
    for row in cursor:
        print "\n\n\nOID: ", row[0]
        partnum = 0
        for part in row[1]:
            print "\nPart number ", partnum
            for point in row[1].getPart(partnum):
                print point.X, point.Y
            partnum = partnum + 1

