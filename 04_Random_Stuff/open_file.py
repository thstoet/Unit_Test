# Konsole: script im Ordener strten, in welchem Text file liegt

f = open("text.txt","r")   #'r' nur lesen
print(f.read())
print(f.readline())
print(f.read(1))

b = open("text.txt","r")		# Wie Funktion behandeln
for line in b:
	print(line)
	
	
c = open("text.txt", "a")			# a fügt text hinzu, 'w' überschreibt alles
c.write("\nIch kann schreiben")

# close() gibts auch 