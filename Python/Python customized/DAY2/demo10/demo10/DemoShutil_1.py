import shutil
import os
sourcepath="src/"
source = os.listdir(sourcepath)
print(source)
destination = "desc1/"
for file in source:
    if file.endswith(".txt"):
         shutil.move(sourcepath+file, destination)
