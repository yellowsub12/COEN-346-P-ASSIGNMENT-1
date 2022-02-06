import os
import shutil
import re
wacky = str
while wacky != "exit":
    wacky = input()
    if wacky == "exit":
        break
    wackystring = re.sub(r'->', '>', wacky)
    os.system(wackystring)
    print(wackystring)
#print(shutil.which("notepad.exe"))
#os.startfile(shutil.which("notepad.exe"))
