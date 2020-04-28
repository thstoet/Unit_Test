import os


old_file = os.path.join("directory", "a.txt")
new_file = os.path.join("directory", "b.kml")
os.rename(old_file, new_file)

from os import rename, listdir 

badprefix = "cheese_" 
fnames = listdir('.') 

for fname in fnames: 
	if fname.startswith(badprefix*2): 		
		rename(fname, fname.replace(badprefix, '', 1))
		
import os
items = os.listdir(".")

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
print(newlist)
'''
def find(str, ch): 
  index = 0 
  while index < len(str): 
    if str[index] == ch: 
      return index 
    index = index + 1 
  return -1 
 
 import string
  >>> fruit = "banana" 
>>> index = string.find(fruit, "a") 
>>> print index 
1 
'''