import urllib, json
import sys, time

# google maps api key
keyfile = open("z:\\path\\google-maps-api-key.txt") # change this line to the path where your store your API key

apikey = keyfile.read()
keyfile.close()

# Python list of addresses
addresses = [
'245 Fourth St., NW, Atlanta, GA  30332',
'760 Spring St. NW, Atlanta, GA 30308',
'12507 Fourth St., NW, Atlanta, GA 39999',
'1235 N. Brookhaven Cir. NE, Atlanta, GA  30319',
'3032 Knox Ave., Atlanta, GA  30319',
'6257 Magnolia Ridge, Atlanta, GA  30087',
'Georgia Tech',
'Georgia Tech College of Design',
'Georgia Tech College of Architecture',
'Georgia Tech West Architecture Building',
'Georgia Tech East Architecture Building',
'Georgia Tech School of City and Regional Planning',
'Georgia Tech Center for GIS',
'Georgia Tech GIS Center',
'Georgia Tech C-SPAV',
'Georgia Tech Center for Spatial Planning Analytics and Visualization',
'Georgia Tech Center for Quality Growth and Regional Development',
'Georgia Tech Center for Quality Growth'
]

# establish variable names for punctuation marks
quote = '"'
semicolon = ';'

# loop through all addresses in list
for add in addresses:
    # wait 1/10 of second between submissions
    time.sleep(.1)
    prefix = 'https://maps.googleapis.com/maps/api/geocode/json?'
    data = urllib.urlencode({"address" : add, "key": apikey})
    url = prefix+data
    gresp = urllib.urlopen(url)
    # loads json response into Python list and dictionary format
    jresp = json.loads(gresp.read())
    # tests to ensure that SOME address information was returned
    if jresp["status"] == "OK":
        # pulls specific information from Google's response
        lat = jresp['results'][0]['geometry']['location']['lat']
        lon = jresp['results'][0]['geometry']['location']['lng']
        formadd = jresp['results'][0]['formatted_address']
        precision = jresp['results'][0]['geometry']['location_type']
        # prints information to console
        # leading semicolon keeps Excel from removing initial string quote
        # str function converts Python number to string for easier printing
        print (semicolon+
                  quote+add+quote+semicolon+
                  quote+formadd+quote+semicolon+
                  str(lat)+semicolon+
                  str(lon)+semicolon+
                  quote+precision+quote)
                  
# final print statement to emphasize Python indentation as significant
print "Program ends"
