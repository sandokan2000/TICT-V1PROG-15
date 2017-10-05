som = 0
getallen = 0
while True:
    getal = eval(input('geef getal: '))
    if getal == 0:
        break
    else:
        som = som + getal
        getallen = getallen + 1
print('Aantal getallen: ' + str(getallen) + '\nSom van de getallen: ' + str(som))