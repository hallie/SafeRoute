import json
import requests

key = 'AIzaSyCdhFSjCMUQwM-qggTX9wapsVEfDWPQapY'

def getLatLon(url):
	try:
		#Adds the url to the end of the http request
		r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + url + "+Washington,+DC&key=" + key)
		res = r.json()[u'results']
		if (len(res) > 0):
			latlon = res[0][u'geometry'][u'location']
			lat = latlon[u'lat']
			lon = latlon[u'lng']
			print(lat,lon)
			return lat, lon
		else:
			return 'fail', 'fail'
	#prints the int of the status code. Find more at httpstatusrappers.com :)
	except requests.ConnectionError:
		print("failed to connect")

f = open('crimes/theft.txt', 'r')
o = open('crime_lats/theft.txt', 'w')
for line in f:
	lat, lon = getLatLon(line[0:-1])
	o.write(str(lat) + ',' + str(lon) + '\n')
o.close()
f.close()
#print(a1)
#lat, lon = getLatLon(a1)
#print(lat,lon)
#f.write('%s, %s, %s\n' % (row['OFFENSE'], lat, lon))
#f.close()
