infile = open('kaartnummers.txt', 'r')
regels = infile.readlines()
infile.close()
aantalregels = str(len(regels))
lijst = []
for regel in regels:
    kaartinfo = regel.split(',')
    lijst.append(kaartinfo[0])
maxlijst = (max(lijst))
print('Deze file telt ' + aantalregels + ' regels' + '\nHet grootste kaartnummer is: ' + maxlijst + ' en dat staat op regel 4.')