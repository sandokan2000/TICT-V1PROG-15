import csv
with open('artikels.csv', 'r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    duursteartikel = 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > duursteartikel:
            duursteartikel = prijs
            duurstenaam = row['Naam']
    print(duursteartikel, duurstenaam)