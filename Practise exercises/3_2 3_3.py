janee = ['Ja', 'ja']
aw = False
leeftijd = eval(input('Je leeftijd: '))
nederlands = input('Ben je in bezit van een nederlands paspoort(ja of nee): ')

if leeftijd >= 18 and nederlands in janee:
    print('U mag stemmen!')
else:
    print('U mag niet stemmen')
