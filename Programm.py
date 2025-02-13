#Grundmenü 1, 2, 3, 8-Exit

# match Abfrage

# in cases die Funktionen

# Loop Abfrage Nochmal? Y/N

# Danke Ende
import time

def BarbarasFunktion():
    time.sleep(1)
    print("\33[31m->   :\\33[0m")
    time.sleep(1)
    print("\33[32m->  :)\33[0m")
    time.sleep(1)
    print("\33[34m-> :D\33[0m")
    #Barbaras Code

abfrage = True

while(abfrage == True):
    print("Bitte wählen:\n1 für Denise \n2 für Barbara \n3 für Sophie \n8 für Exit")
    eingabe = input()
    #Input
    match(eingabe):
        case "1":
            #Funktion
            abfrage
            break
        case "2":
            BarbarasFunktion()
            abfrage
            break
        case "3":

            abfrage = False

abfrage2 = True
while(abfrage2 == True):
    #Nochmal?? If/else
    break

#Ende Tschüss
