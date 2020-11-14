# class0320
# section 1 Basic strcture in JSON

collegedict = {'COS': 'College of Sciences', 'COE': 'College of Engineering'}
print collegedict['COS']

# section 2 A classic JSON data

jresp0 = {'results': [
                     {'elevation': 282.048217,
                      'location': {'lat': 33.7760026, 'lng': -84.3954736},
                      'resolution': 4.771975994110107},

                     {'elevation': 292.7734375,
                      'location': {'lat': 33.7760026, 'lng': -84.3954736},
                      'resolution': 4.771975994110107}
                    ],
 'status': 'OK'}

# section 3 how to handle JSON

campuslist=[{"areaname":"GT campus","acres":400,"city":"Atlanta","buildings":250},
     {"areaname":"GSU campus","acres":200,"city":"Atlanta","buildings":150},
     {"areaname":"UGA campus","acres":600,"city":"Athens","buildings":450}]

# use a loop to access all items in a list
for c in campuslist:
	print c['areaname'],c['city']

# use a loop with an "if" conditional to choose a specific item or items
for c in campuslist:
    if c['areaname'] == 'GT campus':
        print "GT acres =", c['acres']

# section 4

# json consists of lists and dictionaries
# json objects in Python can be built from the inside outward
lldict1 = {'lat':34, 'lng':-83}
lldict2 = {'lat':35, 'lng':-84}
lldict3 = {'lat':36, 'lng':-85}
gdict1 = {'location':lldict1, 'precision':'street'}
gdict2 = {'location':lldict2, 'precision':'rooftop'}
gdict3 = {'location':lldict3, 'precision':'zip'}
resultlist = [gdict1,gdict2,gdict3]
jresp1 = {'results':resultlist,'status':'OK'}

jresp1['results'][0]['location']['lat'] # for first lat
if jresp1['status'] == 'OK': # check to be sure result is not empty
     for r in jresp1['results']:  # loop to access all lats for an address
          print r['location']['lat']

# section 5

newcampuslist = [{"areaname":"GT campus",
                  "acres":400,
                  "city":"Atlanta",
                  "buildings":250,
                  "location": {"lat":34, "lon":-83}
                  },
                 {"areaname":"UGA campus",
                 "acres":600,
                 "city":"Athens",
                 "buildings":450,
                  "location": {"lat":35, "lon":-84}
                  }
                  ]

for c in newcampuslist:
    if(c["areaname"] == "UGA campus"):
        ugalatitude = c['location']['lat']
print ugalatitude

# section 6

dict1 ={'listbkey': listb, 'listakey': lista}
dict1['listakey']
dict1['listakey'][5]
dict1['listakey'][5][2]
dict2 ={'keyfora': 'Aardvark', 'keyforb': 'Buffalo'}
lista.append(dict2)
print lista





