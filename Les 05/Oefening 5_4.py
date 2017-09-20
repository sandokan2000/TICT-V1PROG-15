weekdag = 'dinsdag'
dag = 25
maand = 'maart'
uur = 14
minuten = 15
print('{} {} {}' .format(weekdag, dag, maand))
print('{} {} {} om {}.{}' .format(weekdag, dag, maand, uur, minuten))

for i in range(1,8):
    print(i, i**2, 2**i)
    
for i in range(1, 8):
    print('{} {:2} {:3}'.format(i, i**2, 2**i))