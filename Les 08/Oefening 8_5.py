import random

def diceprob(invoersom):
    aantalworpensom = 0
    aantalworpen = 0
    while aantalworpensom < 100:
        aantalogen1 = random.randrange(1, 7)
        aantalogen2 = random.randrange(1, 7)
        som = aantalogen1 + aantalogen2
        if som == invoersom:
            aantalworpensom += 1
        aantalworpen += 1
    print('Het aantal benodigde worpen om 100 keer {} te gooien is {}'.format(somaantalogen, aantalworpen))

somaantalogen = eval(input('Hoeg groot is de som: '))

diceprob(somaantalogen)