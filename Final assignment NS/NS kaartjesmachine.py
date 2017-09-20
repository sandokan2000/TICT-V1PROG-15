def standaardprijs(afstandKM):
    if afstandKM > 0 and afstandKM <= 50:
        prijskaartje = afstandKM * 0.80
    if afstandKM > 50:
        prijskaartje = afstandKM * 0.60 + 15
    if afstandKM <= 0:
        prijskaartje = 0
    return prijskaartje

def ritprijs(leeftijd, weekendrit, afstandKM):
    if (leeftijd < 12 and weekendrit in ja) or (leeftijd >= 65 and weekendrit in ja):
        tebetalenprijs = 0.65 * standaardprijs(afstandKM)
    if (leeftijd >= 12 and weekendrit in ja and leeftijd < 65):
        tebetalenprijs = 0.6 * standaardprijs(afstandKM)
    if (leeftijd < 12 and weekendrit in nee) or (leeftijd >= 65 and weekendrit in nee):
        tebetalenprijs = 0.7 * standaardprijs(afstandKM)
    if (leeftijd >= 12 and weekendrit in nee and leeftijd < 65):
        tebetalenprijs = standaardprijs(afstandKM)
    return str(tebetalenprijs)

nee = ['nee', 'Nee']
ja = ['ja', 'Ja']
afstandKM = eval(input('Hoeveel kilometer moet u reizen? '))
weekendrit = input('Reist u in het weekend(ja of nee)? ')
leeftijd = eval(input('Wat is uw leeftijd? '))
print('Uw kaartje kost ' + ritprijs(leeftijd, weekendrit, afstandKM) + ' euro.')