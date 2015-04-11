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

offs = {
		'SEX ABUSE' : [],
		'MOTOR VEHICLE THEFT': [],
		'BURGLARY': [],
		'HOMICIDE': [],
		'ASSAULT W/DANGEROUS WEAPON': [],
		'ARSON': [],
		'THEFT F/AUTO': [],
		'ROBBERY': [],
		'THEFT/OTHER': []
	   }
off_names = ['SEX ABUSE', 'MOTOR VEHICLE THEFT', 'BURGLARY', 'HOMICIDE', 'ASSAULT W/DANGEROUS WEAPON', 'ARSON', 'THEFT F/AUTO', 'ROBBERY', 'THEFT/OTHER']
off_files = ['sex_abuse', 'motor_vehicle_theft', 'burglary', 'homocide', 'assualt', 'arson', 'auto_theft', 'robbery', 'theft']

with open('crime_incidents_2011.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		address = row['BLOCKSITEADDRESS']
		if (isValid(address)):
			a1, a2 = getUrl(address)
			offs[row['OFFENSE']].append(a1)
			offs[row['OFFENSE']].append(a2)
			
for i in range(len(off_names)):
	f = open('crimes/' + off_files[i] + '.txt', 'w')
	for urls in offs[off_names[i]]:
		f.write(urls + '\n')
	f.close()