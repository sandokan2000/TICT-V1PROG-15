week = {'ma': 'maandag', 'di':'dindag', 'wo': 'woensdag', 'do': 'donderdag', 'vr': 'vrijdag'}
print(week)

print('ma' in week)

week['di'] = 'dinsdag'
print(week)

week['za'] = 'zaterdag'

for afkorting in week.keys():
    print(afkorting)

for langeNaam in week.values():
    print(langeNaam)

for beide in week.items():
    print(beide)

for afkortingen in week:
    print('afkorting', week[afkorting])

for afkorting in week:
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))
