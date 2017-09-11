getallenrij = [2, 5, 7, 9, 12, 24, 97, 3]
zoekgetal = eval(input('Zoek getal: '))
gevonden = False
for getal in getallenrij:
    if zoekgetal == getal:
        gevonden = True
if gevonden == True:
    print('Het getal is aanwezig in de getallenrij')
else:
    print('Het getal is niet aanwezig in de getallenrij')