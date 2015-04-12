crimes = ['arson', 'auto_theft', 'homicide', 'sex_assault', 'theft']

for crime in crimes:
	text = open('crime_lats/' + crime + '.txt', 'r')
	js = open('crime_js/' + crime + '.txt', 'w')
	
	js.write('var %s = [\n' % (crime))
	
	for line in text:
		lat, lon = line.split(',')
		if (lat == 'fail'):
			print True
		else:
			js.write('\t[%s, %s],\n' % (lat, lon[0:-1]))
	
	js.write(']')
	
	text.close()
	js.close()