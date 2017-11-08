import csv
with open('artikel.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('artikelnummer', 'artikelcode', 'naam', 'voorraad', 'prijs'))
    while True:
        artikelnummer = input('Wat is uw artikelnummer? ')
        if artikelnummer == '':
            break
        artikelcode = input('Geef de artikel code: ')
        naam = input('Geef de naam van het artikel door: ')
        voorraad = input('Aantal arikelen nog in voorraad: ')
        prijs = input('Geef de prijs van het product: ')
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))