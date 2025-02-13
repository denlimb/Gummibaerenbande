#Grundmenü 1, 2, 3, 8-Exit

# match Abfrage

# in cases die Funktionen

# Loop Abfrage Nochmal? Y/N

# Danke Ende
import os
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

def DeniseFunktion():
    print("Habt einen Schönen Tag.")

def SophiesFunktion():
    print("Sophie war hier")

while(abfrage == True):
    print("MENÜ\n________________________\n")
    print("Bitte wähle:\n1 für Denise, 2 für Barbara, 3 für Sophie, 8 für Exit")
    eingabe = input()
    match(eingabe):
        case "1":
            DeniseFunktion()
        case "2":
            BarbarasFunktion()
        case "3":
            SophiesFunktion()
        case "8":
            print("Verlassen wurde eingeleitet")
            abfrage = False
            break
        case _:
            print("Antwort nicht erkannt, wähl was 'gscheids!\n")
            abfrage = True
            continue         
    abfrage2 = True
    print("Noch eine Runde? Ja oder Nein")
    eingabe = input().strip().lower()
    while(abfrage2 == True):
        if eingabe == "ja":
            print("Alles klar, noch eine Runde")
            abfrage2 = False
            abfrage = True
        elif eingabe == "nein":
            abfrage = False
            abfrage2 = False
        else:
            print("Error, Tschüssi")
            abfrage = False
            abfrage2 = False

print("Danke, tüdeldüh")
#Ende Tschüss

   