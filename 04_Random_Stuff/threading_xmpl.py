import threading								#diese Modul ist im Ordner Liz zu finden
import time


#Es wird die Klasse myFred erstellt damit mehrere Instanzen erstellt werden können, die dann parallel ablaufen

class myFred(threading.Thread):					#Klasse erstellen und Vererbung der Klasse Thread der Methode threading 
	def __init__(self, iD, name):				#Konstruktor für Initialisierung des Moduls und Variablen 
		threading.Thread.__init__(self)			#Oberklasse Thread wird wird initialisiert
		self.iD = iD							#Initialsierung der Klassenvariablen auf Basis der UebergabeVariablen
		self.name = name
	
	def run(self):								#Das soll passieren und zwar parallel, diese Meothode muss run() heißen!!!
		print("Starte ID:", self.iD, "Name:", self.name)
		print("Wait for:", 3*self.iD, "seconds")
		print("--->")
		time.sleep(3*self.iD)
		print("Ende", self.iD)

t1 = myFred(1,"t1")								#Instanz erstellen mit Uebergabevariable für iD und name
t2 = myFred(2,"t2")

t1.start()										#Start ist Funktion in Klasse Thread und aktiviert den Thread
t2.start()										#In diesem Fall wird gleichzeitug aktiviert mit unterschiedlichen Laufzeiten

time.sleep(10)									#warten 10 seconds, denn Programm kann eher zuende sein als thread
print("Beende Main")
