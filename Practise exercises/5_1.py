def tempratuur(gradenC):
    gradenF = gradenC* 1.8 +32
    return gradenF
def table():
    for gradenC in range(-30, 50, 10):
        print('{:5} {:3}'.format(tempratuur(gradenC), gradenC))
table()

