import random as rnd

lengde = 5
bredde = 5
tallListe = []
totalListe = []
x = 0
y = 0

# Generer tall og legg dem til i totalListe
for i in range(lengde):
    for j in range(bredde):
        tallListe.append(f'{rnd.randint(0, 10)}\t')
    print("".join(tallListe))
    totalListe.append(tallListe)
    tallListe = []

def hvorGå():
    global x
    global y
    """ print(f"x: {x}, y: {y}") """
    
    if x == 4:
        høyre = 0
    else:
        høyre = int(totalListe[y][x+1].strip())
    
    if y == 4:
        ned = 0
    else:
        ned = int(totalListe[y+1][x].strip())

    """ print(f"høyre: {høyre}, ned: {ned}") """
        
    if høyre > ned:
        print("Høyre")
        x += 1
    elif høyre < ned:
        print("Ned")
        y += 1
    else:
        print("Høyre")
        x += 1
            
            
while x <= 4 and y <= 4:
    hvorGå()