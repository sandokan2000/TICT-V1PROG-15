name = input('Your name: ')
leeftijd = eval(input('Hello '+ name + ', what is your age: '))
if leeftijd >= 18:
    print(name + ',' + ' you are old enough to vote')
else:
    print('Sorry ' + name + ',' + ' you are not old enough to vote')
print('Goodbye ' + name)