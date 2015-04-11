import json
import requests
import csv

def isValid(address):
	address = address.split(" ")
	if ((len(address) > 4) and ((address[3] == 'BLOCK') and (address[4] == 'OF'))):
		return True
	return False

def getUrl(address):
	address = address.split(" ")
	if ((address[3] == 'BLOCK') and (address[4] == 'OF')):
		a1 = a2 = address[5:][::-1]
		a1.append(address[0])
		a1 = a1[::-1]
		a2[-1] = address[2]
		a2 = a2[::-1]
		a1 = "+".join(a1) + ','
		a2 = "+".join(a2) + ','

		return a1, a2

def getLatLon(url):
	try:
		#Adds the url to the end of the http request
		r = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=" + url + "+Washington,+DC")
		res = r.json()[u'results']
		if (len(res) > 0):
			latlon = res[0][u'geometry'][u'location']
			lat = latlon[u'lat']
			lon = latlon[u'lng']
			return lat, lon
		else:
			return 'fail', 'fail'
	#prints the int of the status code. Find more at httpstatusrappers.com :)
	except requests.ConnectionError:
		print("failed to connect")

f = open('test.txt', 'w')
count = 0
with open('crime_incidents_2011.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		address = row['BLOCKSITEADDRESS']
		if (isValid(address)):
			a1, a2 = getUrl(address)	
			lat, lon = getLatLon(a1)
			if(lat != 'fail'):
				f.write('%s, %s, %s\n' % (row['OFFENSE'], lat, lon))
			lat, lon = getLatLon(a2)
			if(lat != 'fail'):
				f.write('%s, %s, %s\n' % (row['OFFENSE'], lat, lon))