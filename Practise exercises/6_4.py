studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
def gemiddelde_per_student(studentencijfers):
    for student in studentencijfers:
        gemiddelde = sum(student) / len(student)
        LijstGem.append(gemiddelde)
    print(LijstGem)
LijstGem = []
def totaalgemiddelde():
    print(sum(LijstGem)/len(LijstGem))
gemiddelde_per_student(studentencijfers)
totaalgemiddelde()