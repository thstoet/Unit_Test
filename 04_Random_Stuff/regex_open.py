import re

with open("simpsons_phone_book.txt") as fh:
    for line in fh:
        if re.search(r"J.*Neu",line):
            print(line.rstrip())
  
 