import pandas as pd

Mesovita = pd.read_csv("files/orders.csv")

def Dan(broj): 
    if broj == 1:
        return "Ponedeljak"
    if broj == 2:
        return "Utorak"
    if broj == 3:
        return "Sreda"
    if broj == 4:
        return "Cetvrtak"
    if broj == 5:
        return "Petak"
    if broj == 6:
        return "Subota"
    if broj == 7:
        return "Nedelja"

niz = [0] * 8

for i in Mesovita["order_dow"]:
    niz[i] += 1

mojMax = 0
mojIndex = 0

for i in range(0, 8):
   if niz[i] > mojMax:
       mojMax = niz[i]
       mojIndex = i
niz[mojIndex] = 0

tvojMax = 0
tvojIndex = 0

for i in range(0, 8):
   if niz[i] > tvojMax:
       tvojMax = niz[i]
       tvojIndex = i
print("Najposeceniji dani su: " + str(Dan(tvojIndex+1)) + " i " + str(Dan(mojIndex+1)))
