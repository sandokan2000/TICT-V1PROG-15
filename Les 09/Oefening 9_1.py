try:
    numlist = [100, 101, 0, '103', 104]
    index = int(input('Geef een index: '))
    print(100/numlist[index])
except ValueError:
    print('Je moet een heel getal invoeren')
except ZeroDivisionError:
    print('Deze index behoort tot het getal nul en er kan niet door nul gedeeld worden')
except TypeError:
    print('De lijist bevat een niet-nummeriek element')
except IndexError:
    print('Je moet een getal tussen de -5 en 4 invullen')