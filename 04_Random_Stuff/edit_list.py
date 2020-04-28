Liste1=["img-1","img-2"]
Liste2 =[]

for file_name in Liste1:
	Liste2.append(file_name.replace("-", "_",1))
print(Liste1)
print(Liste2)