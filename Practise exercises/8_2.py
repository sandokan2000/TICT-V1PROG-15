import random
def monopolyworp():
    worp1 = random.randint(1,6)
    worp2 = random.randint(1,6)
    samen = worp1+worp2
    if worp1 == worp2:
        print(str(worp1) + ' + ' + str(worp2) + ' = ' + str(samen) + ' (dubbel)')
        monopolyworp2()
    else:
        print(str(worp1) + ' + ' +  str(worp2) + ' = ' + str(samen))





def monopolyworp2():
    worp3 = random.randint(1, 6)
    worp4 = random.randint(1, 6)
    samen2 = worp4 + worp3
    if worp3 == worp4:
        print(str(worp3) + ' + ' + str(worp4) + ' = ' + str(samen2) + ' (dubbel)')
        monopolyworp3()
    else:
        print(str(worp3) + ' + ' + str(worp4) + ' = ' + str(samen2))



def monopolyworp3():
    worp5 = random.randint(1, 6)
    worp6 = random.randint(1, 6)
    samen3 = worp5 +worp6
    if worp5 == worp6:
        print(str(worp5) + ' + ' + str(worp6) + ' = ' + str(samen3) + ' (direct naar de gevangenis)')
    else:
        print(str(worp5) + ' + ' + str(worp6) + ' = ' + str(samen3))

    monopolyworp()