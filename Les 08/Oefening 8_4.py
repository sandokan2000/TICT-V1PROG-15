hoi = input('Voer een woord in: ')
for karakter in hoi:
    asc = ord(karakter)
    print('Letter: {:1}    ASCII-waarde: {:3}    hexidecimalewaarde: {:x}    binearewaarde: {:b}'.format(karakter, asc, asc, asc))