def inlezen_beginstation(stations):
    begin_bestemming = input('Waar gaat start uw reis? ')
    while begin_bestemming not in stations:
        begin_bestemming = input('Sorry, deze bestemming bestaat niet.\nWaar start uw reis?: ')
    return begin_bestemming

def inlezen_eindstation(stations, begin_bestemming):
    eind_bestemming = input('Wat is uw eind bestemming? ')
    while eind_bestemming not in stations:
        eind_bestemming = input('Dit station bestaat helaas niet.\nWat is uw eind bestemming? ')
    while stations.index(eind_bestemming) - stations.index(begin_bestemming) <= 0:
        eind_bestemming = input('Deze reis is helaas niet mogelijk.\nKies een ander eind bestemming: ')
    return eind_bestemming

def omroepen_reis(stations, begin_station, eind_station):
    nummer_eindstation = stations.index(eind_station) + 1
    nummer_beginstation = stations.index(begin_station) + 1
    aantal_tussenstations = nummer_eindstation - nummer_beginstation
    Prijs_Reis = aantal_tussenstations * 5
    print('Beginstation: ' + begin_station + '\nRangnummer beginstation: ' + str(nummer_beginstation))
    print('Eindstation: ' + eind_station + '\nRangnummer eindstation: ' + str(nummer_eindstation))
    print('Reislengte in stations: ' + str(aantal_tussenstations))
    print('Prijs van de reis: ' + str(Prijs_Reis) + ' euro')
    print('De stations waar je langs komt zijn: ')
    while nummer_beginstation < nummer_eindstation - 1:
        print('- {}'.format(stations[nummer_beginstation]))
        nummer_beginstation += 1
    print('Je stapt uit in: {}'.format(eind_station))

stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
begin_bestemming = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, begin_bestemming)
omroepen_reis(stations, begin_bestemming, eindstation)