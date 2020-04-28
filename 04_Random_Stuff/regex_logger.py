import re
import numpy as np
import matplotlib.pyplot as plt

Liste = []
Out = []
Graph = []

with open("C:\Python\Script_me\Programme\\temp.log") as fh:
    for line in fh:
            Liste.append(line.rstrip())

for log in Liste:
	temp= re.findall(r"[0-9]{2}.[0-9]",log)
	if temp:
		Out.append(temp)

i = 0
while i <= len(Out)-1:
	x = str(Out[i])
	Graph.append(x[2:6])
	i += 1

print(Graph)
print(Graph[1])

#%matplotlib inline


C = np.array(Graph)
print(C, type(C))

plt.plot(C)
plt.show()
