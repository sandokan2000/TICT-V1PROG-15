zin = input('Voer een zin in: ')
woorden = zin.split()
acroniem = ''
for woord in woorden:
    acroniem = acroniem + woord[0].capitalize()
print(acroniem)

zin = input('Voer een zin in: ')
woorden = zin.split()
acroniem = ''
for woord in woorden:
    acroniem = acroniem + woord[0]
print(acroniem.upper())