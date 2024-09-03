import random as rnd

lengde = 5
bredde = 5
tallListe = []
totalListe = []
x = 0
y = 0
besøkte_posisjoner = []

# ANSI escape-koder for farger
def fargelegg(text, farge):
    farger = {
        "rød": "\033[91m",
        "grønn": "\033[92m",
        "slutt": "\033[0m"
    }
    return f"{farger[farge]}{text}{farger['slutt']}"

# Generer tall og legg dem til i totalListe
for i in range(lengde):
    for j in range(bredde):
        tallListe.append(f'{rnd.randint(0, 10)}\t')
    totalListe.append(tallListe)
    tallListe = []

def hvorGå():
    global x
    global y
    
    if x < 4:
        høyre = int(totalListe[y][x+1].strip())
    else:
        høyre = -1  # Sett til en lav verdi når x er 4 for å unngå å gå utenfor matrisen
    
    if y < 4:
        ned = int(totalListe[y+1][x].strip())
    else:
        ned = -1  # Sett til en lav verdi når y er 4 for å unngå å gå utenfor matrisen
        
    if høyre > ned:
        x += 1
    elif høyre < ned:
        y += 1
    else:
        x += 1

# Funksjon for å skrive ut totalListe med fargelegging
def skrivUtTotalListe():
    for i in range(lengde):
        for j in range(bredde):
            if (i, j) in besøkte_posisjoner:
                print(fargelegg(totalListe[i][j], "grønn"), end="")
            elif i == y and j == x:
                print(fargelegg(totalListe[i][j], "rød"), end="")
            else:
                print(totalListe[i][j], end="")
        print()

# Hovedløkken
while x < 5 and y < 5:
    skrivUtTotalListe()
    besøkte_posisjoner.append((y, x))
    if x == 4 and y == 4:
        break
    hvorGå()
    print()