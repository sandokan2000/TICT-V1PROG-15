s = 'voorbeeld'
print(s.capitalize())
print(s)
print(s.count('e'))
print(s.find('e'))
print(s.replace('e', 'a'))
s = 'VoOrBeElD'
print(s.lower())
print(s.upper())
s = 'dit is een voorbeeld'
print(s.split())
s = 'dit-is-een-voorbeeld'
print(s.split('-'))
prod = 'morels'
cost = 139
wght = 1/2
total = cost * wght
print(prod, cost, wght, total)
print(prod, cost, wght, total, sep='; ')
pets = ['kees', 'sander', 'henk']
for pet in pets:
    print(pet, end=', ')