getallenrij = [2, 6, 8, 12, 9, 3, 4, 18, 17]
aantal3 = 0
for getal in getallenrij:
    if getal % 3 == 0:
      aantal3 = aantal3 + 1
print('Het aantal getallen deelbaar door 3 is ' + str(aantal3))