
# class0520.py 

# This is the latitude and longitude of 358 West Architecture
# latlon = "33.7759494,-184.3960213"

# Here are slightly modified json results from a Google Elevation query
jresp = {u'results': [
               {u'elevation': 282.30126953125,
                u'location': {u'lat': 33.7759494, u'lng': -84.3960213},
                u'resolution': 4.771975994110107},

               {u'elevation': 286.95312530126,
                u'location': {u'lat': 33.7759494, u'lng': -84.3960213},
                u'resolution': 6.411010777197599}
                ],
         u'status': u'OK'}

# Here are some commands to type into the interpreter

# jresp["results"]
# jresp["results"][0]
# jresp["results"][1]
# jresp["results"][0]["elevation"]

# for r in jresp["results"]:
#     print r["elevation"]

# jresp["results"][0]["location"]
# jresp["results"][0]["location"]["lat"]

# for r in jresp["results"]:
#     print r["elevation"], r["location"]["lat"], r["location"]["lng"]



# But what if we make a small mistake when typing the longitude?
# latlon = "33.7759494,-184.3960213"

# Here is the result, run with F2
jresp2 = {u'error_message': u"Invalid request. Invalid 'locations' parameter.",
         u'results': [],
         u'status': u'INVALID_REQUEST'}

# Try this command now
# jresp2["results"][0]

