score = eval(input('score voor de toets: '))
punten = 0
if punten + score >= 15:
    print('Gefeliciteerd!')
    print('Met een score van ' + str(score) + ' heb je je tentamen gehaald!')
else:
    print('Helaas' + '\n' + str(score) + ' punten zijn helaas niet genoeg punten om je tentamen te halen!')