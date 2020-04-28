en_de = {"red": "rot", "black": "schwarz", "brown": "braun"}
de_fr = {"rot": "rouge", "grün": "vert", "blau": "bleu", "gelb": "jaune"}

dict = {"en_de": en_de, "de_fr": de_fr}

print("In Deutschland sagt man: " + en_de["red"])

# oder

print("In Deutschland sagt man: " + dict["en_de"]["black"])

