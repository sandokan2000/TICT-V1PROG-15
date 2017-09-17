def standaardprijs(afstandKM):
    if afstandKM > 0 and afstandKM <= 50:
        prijskaartje = afstandKM * 0.80
    if afstandKM > 50:
        prijskaartje = afstandKM * 0.60 + 15
        #bij 51km heel raar antwoord
    if afstandKM <= 0:
        prijskaartje = 0
    return prijskaartje

def ritprijs(leeftijd, weekendrit, afstandKM):
    if (leeftijd < 12 and weekendrit in janee) or (leeftijd >= 65 and weekendrit in janee):
        tebetalenprijs = 0.65 * standaardprijs(afstandKM)
    if (leeftijd >= 12 and weekendrit in janee and leeftijd < 65):
        tebetalenprijs = 0.6 * standaardprijs(afstandKM)
    if (leeftijd < 12 and weekendrit in neeja) or (leeftijd >= 65 and weekendrit in neeja):
        tebetalenprijs = 0.7 * standaardprijs(afstandKM)
    if (leeftijd >= 12 and weekendrit in neeja and leeftijd < 65):
        tebetalenprijs = standaardprijs(afstandKM)
    return str(tebetalenprijs)

neeja = ['nee', 'Nee']
janee = ['ja', 'Ja']
afstandKM = eval(input('Hoeveel kilometer moet u reizen? '))
weekendrit = input('Reist u in het weekend(ja of nee)? ')
leeftijd = eval(input('Wat is uw leeftijd? '))
print('Uw kaartje kost ' + ritprijs(leeftijd, weekendrit, afstandKM) + ' euro.')