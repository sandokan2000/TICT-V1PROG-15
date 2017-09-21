tabel = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
print(tabel[0])
print(tabel[1])
print(tabel[2])
print()
for rij in range(3):
    for kolom in range(4):
        print(tabel[rij][kolom], end = ' ')
    print()
print()

for rij in range(len(tabel)):
    for kolom in range(len(tabel[rij])):
        print(tabel[rij][kolom], end = ' ')
    print()