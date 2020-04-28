import random
import ast

# In der Liste "eintraege" werden an jeder ListenStelle zwei strings an die Klasse Entry uebergeben (deutsch, englisch),
# welche dort im Konstruktor instanziert (de, eng) werden.
# Somit wird realisiert, dass mehrere Begriffe (z.b Hallo, hello) auf einem Listeneintrag stehen

class Entry:
    def __init__(self, deutsch, englisch):
        self.de = deutsch
        self.eng = englisch
    def toString(self):
        return self.de + " - " + self.eng   # Wird an Liste zurückgegeben
    def to_deutsch_DB(self):
        return self.de
    def to_englisch_DB(self):
        return self.eng


eintraege = [Entry("Hallo", "hello"), Entry("Hund", "dog"), Entry("Auto", "car")]

# es werden neue Vokabeln an Klasse Entry uebergeben und in Liste appended

def eingabe():
    while True:
        deutsch = input("Deutsches Wort: ")
        if deutsch == "#fertsch":
            return                                      # break auch möglich
        englisch = input("Englisches Wort: ")
        if englisch == "#fertsch":
            return
        eintraege.append(Entry(deutsch, englisch))

# Zeilenweise auslesen


def einlesen():
    while True:
        f_d = open("vokabel_deutsch_DB.txt")
        f_e = open("vokabel_englisch_DB.txt")
        for line in f_d:                                # txt werden zwilenweise eingelesen
            deutsch = line.rstrip()                     # rstrip() Methode fur saberes einlesen
            for lino in f_e:
                englisch = lino.rstrip()
                eintraege.append(Entry(deutsch, englisch))
                break                                       # damit wieder von lino in line gesprungen wird
        f_d.close()
        f_e.close()
        return

# Zeilenweise in separate Dokumente schreiben

def speichern():
    for i in range(0, 3):       # erste drei Default Listeneintraege löschen, damit diese nicht gespeichert werden
        eintraege.pop(i)
    f_d = open("vokabel_deutsch_DB.txt", "w")       # w steht für Dokument beschreiben
    f_e = open("vokabel_englisch_DB.txt", "w")
    for eintrag in eintraege:                       # abgeschaut von printall(), nur de komplett aus liste lesen
        f_d.write(eintrag.to_deutsch_DB() + "\n")
    for eintrag in eintraege:
        f_e.write(eintrag.to_englisch_DB() + "\n")  # \n damit in txt zeilenweise gespeichert wird
    f_d.close()
    f_e.close()

    eintraege[0:2] = []

    deutsch = "Hallo"
    englisch = "hello"
    eintraege.append(Entry(deutsch, englisch))
    deutsch = "Hund"
    englisch = "dog"
    eintraege.append(Entry(deutsch, englisch))
    deutsch = "Auto"
    englisch = "car"
    eintraege.append(Entry(deutsch, englisch))

# Es wird per Zufall ein Listeneintrag ausgewählt und die Eingabe (word) mit KlassenVariable (de, eng) verglichen

def abfrage():
    while True:
        i = random.randint(0, len(eintraege)-1)     # (-1) weil: Laenge ist 3, Listeneintraege gehen aber nur von 0-2
        word = input("Englische Übersetzung von " + eintraege[i].de + ": ")

        # geiler Zugriff auf Klasse ueber Liste z.B.: eintraege[2].de = Auto

        if word == "#fertsch":
            return
        if eintraege[i].eng == word:                # Vergleich von Eingabe mit eng bei Listenindex i
            print("korrekt!")
        else:
            print("leider falsch. Richtige Antwort: " + eintraege[i].eng)

def printall():
    for eintrag in eintraege:
        print(eintrag.toString())


while True:
    befehl = input("Befehl: ")
    if befehl == "eingabe":
        eingabe()
    elif befehl == "abfrage":
        abfrage()
    elif befehl == "beenden":
        break
    elif befehl == "ausgabe":
        printall()
    elif befehl == "einlesen":
        einlesen()
    elif befehl == "speichern":
        speichern()
    else:
        print("keine bekannte Ausgabe. Tippe: eingabe, abfrage, ausgabe oder beenden")

print("FIN")