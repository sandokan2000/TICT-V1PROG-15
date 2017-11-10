invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
lijst = invoer.split('-')
lijst.sort()
print('Lijst gesorteerd: ' + str(lijst))
print('Grootste getal is: ' + str(lijst[-1])+ ' Kleinste getal in lijst: ' + str(lijst[0]))