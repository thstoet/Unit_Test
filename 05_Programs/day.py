from datetime import datetime
import time

en_de = {"Monday" : "Montach","Tuesday" : "Dienstach","Wednesday":"Medig", "Thursday":"Donschtig","Friday":"Freitach","Saturday":"Sonnabend","Sunday":"Sonntach"}

print("Hey Bruder! Du sagst mir Datum. Ich sag dir Tag!\n")
print("Sagst du Datum!\n")
y = int(input("Jahr: "))
m = int(input("Monat: "))
t = int(input("Tag: "))

print("\nGib mir 5 Sekunden.\n")
for i in range(0,5):
	time.sleep(1)
	print(i+1)
time.sleep(1)

date = datetime(y, m, t)
x = date.strftime("%A")

print("\nResultat: %s. Üsch schwööör!"%(en_de[x]))






