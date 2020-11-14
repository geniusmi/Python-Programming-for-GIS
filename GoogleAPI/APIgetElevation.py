
# imports extra code modules
import urllib, json

# location is West Architecture room 358
latlon = "33.7759494,-84.3960213"

# Substitute your own Google Maps API key for xxxxx
API_KEY = "xxxxx"

prefix = 'https://maps.googleapis.com/maps/api/elevation/json?'
data = urllib.urlencode({"locations" : latlon, "key" : API_KEY})
url = prefix+data

# submits the URL and stores the results
gresp = urllib.urlopen(url)
# converts the results to Python data
jresp = json.loads(gresp.read())

# checks to be sure a valid result was returned
if jresp["status"] == "OK":
    # loops through to print single or multiple results
    for r in jresp["results"]:
        print
        print "lat =                 ", r["location"]["lat"]
        print "lon =                 ", r["location"]["lng"]
        print "elevation (meters) =  ", r["elevation"]
        print "elevation (feet) =    ", r["elevation"]*3.048006096
        print "resolution (meters) = ", r["resolution"]

# the actual json output (variable name: jresp) will look like this:
#
#
# {u'results': [{u'elevation': 282.30126953125,
#                u'location': {u'lat': 33.7759494, u'lng': -84.3960213},
#                u'resolution': 4.771975994110107}],
#  u'status': u'OK'}

