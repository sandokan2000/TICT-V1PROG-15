while True:
    woord = input('Vul een woord in: ')
    if len(woord) == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(woord))
        break
    else:
        print('{} heeft {} letters'.format(woord, len(woord)))