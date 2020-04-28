
# Open a file path = "/var/www/html/" dirs = os.listdir( path )
#  This would print all the files and directories for file in dirs: print file

import sys
import os
import re
from os import rename, listdir

#V1
old_file = os.path.join("directory", "a.txt")
new_file = os.path.join("directory", "b.kml")
os.rename(old_file, new_file)


#V2
badprefix = "cheese_"
fnames = listdir('.')

for fname in fnames:
    if fname.startswith(badprefix*2):
        rename(fname, fname.replace(badprefix, '', 1))


#V3
def rename_files(path, pattern, replacement):
    for filename in os.listdir(path):
        if re.search(pattern, filename):
            new_filename = re.sub(pattern, replacement, filename)
            new_fullname = os.path.join(path, new_filename)
            old_fullname = os.path.join(path, filename)
            os.rename(old_fullname, new_fullname)
            print('Renamed: ' + old_fullname + ' to ' + new_fullname)


