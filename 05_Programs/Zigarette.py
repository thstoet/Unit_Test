class Zigarette:
	L = [["H", "J"], [3, 5]]
	kosten = 0
	
	def Liste(self):
		return print("1: %s - %s\n2: %s - %s"%(self.L[0][0],self.L[1][0],self.L[0][1],self.L[1][1]))
	
	def Auswahl(self, wahl):
		try:
			if wahl == "1":
				return self.L[1][0]
			elif wahl == "2":
				return self.L[1][1]
		except ValueError:
			print("Falsche Eingabe")
					
	def Genter(self, a, g):
		if g == "f":
			return 80 - a
		elif g == "m":
			return 60 - a
	
	def Rechner(self, jahre, anzahl, preis):
		self.kosten  = preis * anzahl* jahre*352
		return self.kosten
	
if __name__== "__main__":
	
	myZ = Zigarette()
	
	myZ.Liste()
	wahl = input("Welche Marke?")
	preis = int(myZ.Auswahl(wahl))
	
	anzahl = int(input("Wieviel Zigaretten pro Tag?"))
	
	alter = int(input("Dein Alter bitte."))
	genter = input("(F)rau oder (M)ann?")
	
	jahre = myZ.Genter(alter, genter)
	
	#integer müssen übergeben werden
	result = myZ.Rechner(jahre, anzahl, preis)
	
	#zurück kommt integer	
	print("Es kommen Kosten in Höhe von %s Euro auf dich zu."%result)
	
	
	
	
	
	
	
	