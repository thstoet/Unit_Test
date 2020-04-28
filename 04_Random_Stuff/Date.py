import time
import datetime

# Anwendung, um Differenz zu bilden

start = time.time()
time.sleep(1)
end = time.time()

print(end-start)
print("Laenge Skript: ", end-start)

#-----------------------------------------------

print(datetime.datetime.now().strftime("%a %H:%M:%S - %d.%m.%Y")) # favoriten Variante

#-----------------------------------------------

print(datetime.date.today().strftime("%a - %d.%m.%Y"))