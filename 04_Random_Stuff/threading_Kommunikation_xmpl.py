import threading								#diese Modul ist im Ordner Liz zu finden
import time

class myFred(threading.Thread):					#Klasse erstellen und Vererbung der Klasse Thread der Methode threading 
	Ergebnis = [0,1]							#Liste anlegen
	def __init__(self, iD, name):				
		threading.Thread.__init__(self)			#Id/name werden nicht verwendet aber veerbete klasse muss initialisiert werden 
		self.iD = iD							
		self.name = name
	
	def run(self):							#Info: gutes Bsp fuer Initialisierung von Klassenvariablen
		i = 0
		while i<10:											
			myLock.acquire()						
			zahl = myFred.Ergebnis[len(myFred.Ergebnis)-2] + myFred.Ergebnis[len(myFred.Ergebnis)-1] 	
											#Laenge der Liste addieren alla Fibonacci
			myFred.Ergebnis.append(zahl)	#Ergebnis zu Liste hinzufügen
			myLock.release()
			i = i+1
		
myLock = threading.Lock()						#blockiert thread bis beendet. 					
t1 = myFred(1,"t1")								#Instanz erstellen mit Uebergabevariable für iD und name
t2 = myFred(2,"t2")

t1.start()										#Threads gehen nacheinander 10x durch die run-Funktion
t2.start()										#Thread2 geht auch 10x durch und erweitert Liste

t1.join()										#warten auf Ende
t2.join()

print(myFred.Ergebnis[15])						#Ausgabe Liste an Stelle 15 aus MyFred Klasse, da beide Threads
												#insgesamt zwanzigmal, Vorteil: Berechnung geht wohl schneller