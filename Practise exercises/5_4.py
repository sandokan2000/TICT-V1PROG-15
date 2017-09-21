import datetime
vandaag = datetime.datetime.today()
datum = vandaag.strftime("%a %d %b %Y")
tijd = vandaag.strftime("%H:%m:%S")
naam = input('Geef de naam van de hardloper: ')

outfile = open('hardlopers.txt', 'a')

outfile.write('/n{}, {}, {}'.format(datum, tijd, naam))