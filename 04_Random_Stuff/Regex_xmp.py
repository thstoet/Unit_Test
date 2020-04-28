import re

# ------------ Nach Wort suchen -----------------

x = re.search("M[ae][iy]er", "Mayer") # findet: Maier, Mayer, Meier, Meyer, Suchbegriff an zweiter Stelle
print(x)

# ------------ mit zahlen -----------------

y = re.search("M[0-9]y", "M8yer") # findet Wort mit Anfang M und Ende y und in Mitte die Zahlen 0-9

print(y)

# ------------ Wort mit leerzeichen -----------------

z = re.search("M[\s]y", "M yer") # findet Wort mit Anfang M und Ende y ohne die Zahlen 0-9

print(z)

# ------------ mit optionalen Zeichen -----------------

k = re.search("M?y", "Mqyer") # findet Wort mit Anfang M und Ende y ohne die Zahlen 0-9

print(k.group('teil1')) # geht aber passt nicht auf das Beispiel