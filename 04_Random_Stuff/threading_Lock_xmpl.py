import threading								#diese Modul ist im Ordner Liz zu finden
import time

class myFred(threading.Thread):					#Klasse erstellen und Vererbung der Klasse Thread der Methode threading 
	def __init__(self, iD, name):				#Konstruktor für Initialisierung des Moduls und Variablen 
		threading.Thread.__init__(self)			#Oberklasse Thread wird wird initialisiert
		self.iD = iD							#Initialsierung der Klassenvariablen auf Basis der UebergabeVariablen
		self.name = name
	
	def run(self):								#Das soll passieren und zwar parallel
		myLock.acquire()						#Lock greift
		print("Starte ID:", self.iD, "Name:", self.name)
		print("Wait for:", 3*self.iD, "seconds")
		time.sleep(3*self.iD)
		myLock.release()						#Lock wird geloest
		print("Ende", self.iD)
		print("--->")

		
myLock = threading.Lock()						#blockiert thread bis beendet. 	kommt in run() zum Einsatz
t1 = myFred(1,"t1")								#Instanz erstellen mit Uebergabevariable für iD und name
t2 = myFred(2,"t2")

t1.start()										#Start ist Funktion in Klasse Thread und aktiviert den Thread
t2.start()										#In diesem Fall werden die threads nacheinander ausgeführt, da myLock aktiv

t1.join()										#Wait until thread terminades, Programm geht erst weiter wenn Thread zueende
t2.join()

time.sleep(10)									#warten 10 seconds, denn Programm kann eher zuende sein als thread
print("Beende Main")
