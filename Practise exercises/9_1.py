try:
    bedrag = 4356
    aantal = eval(input('geef het aantal personen: '))
    if aantal < 0:
        print('Negatief getal mag niet')
    else:
        print(bedrag/aantal)
except ZeroDivisionError:
    ('Delen door 0 mag niet')
except NameError:
    ('Het getal moet in cijfers ingevoerd worden!')
except:
    print('onjuiste invoer')