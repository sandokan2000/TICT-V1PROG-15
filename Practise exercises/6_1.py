def seizoen():
    maand = ['Januari', 'Februari', 'Maart', 'April', 'Mei', 'Juni', 'Juli', 'Augustus', 'September', 'Oktober', 'Novermber', 'December']
    Maand_Input = input('Geef een maand: ')
    if Maand_Input in maand:
        if maand.index == 3 or maand.index == 4 or maand.index == 5:
            print('Deze maand valt in de lente')
        if maand.index == 6 or maand.index == 7 or maand.index == 8:
            print('Deze maand valt in de zomer')
        if maand.index == 9 or maand.index == 10 or maand.index == 11:
            print('Deze maand valt in de herfst')
        if maand.index == 12 or maand.index == 1 or maand.index == 2:
            print('Deze maand valt in de winter')
    else:
        print('Er is geen juiste maand ingevoerd:')
        seizoen()
seizoen()