cijferICOR = 7
cijferPROG = 8
cijferCSN = 7.5
gemiddelde = ((cijferICOR + cijferPROG + cijferCSN)/3)
beloning = 30 * gemiddelde * 3
overzicht = ['Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning op van ' + str(beloning)]
print(overzicht)