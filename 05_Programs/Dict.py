class Dict:
	def __init__(self, wrd_de, wrd_en):
		self.word_de=wrd_de
		self.word_en=wrd_en

if __name__ == "__main__":
	
	Liste=(Dict("hund","dog"), Dict("katze", "cat"))
	
	print(Liste[0].word_de)
	
	user=input("Bitte übersetzen?")
	
	if user == Liste[0].word_en:
		print("Correct")
	else:
		print("Falsch")
	
	
	
	
	