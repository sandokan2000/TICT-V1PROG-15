lijst = eval(input("Geef lijst met minimaal 10 strings: "))
letter = []
for woord in lijst:
    if len(woord) ==4:
        letter.append(woord)
print(letter)