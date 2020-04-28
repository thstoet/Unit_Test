import re

Liste = ["2019-05-01 16:28:54,593:DEBUG:Temperatur Jakob: 37.4 Grad","2019-05-012 16:28:54,593:DEBUG:Temperatur Jakob: 36.9 Grad","2019-05-03 16:28:54,593:DEBUG:Temperatur Jakob: 37.0 Grad"]

Out = []
Graph = []

for log in Liste:
	temp= re.findall(r" [0-9]{2}.[0-9] ",log)
	Out.append(temp)

i = 0
while i <= len(Out)-1:
	x = str(Out[i])
	Graph.append(x[3:7])
	i += 1

print(Graph)
print(Graph[1])
