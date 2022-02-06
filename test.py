import os
import shutil
import re


wacky = input()

wackystring = re.sub(r'->', '>', wacky)
os.system(wackystring)
print(wackystring)
#print(shutil.which("notepad.exe"))

#os.startfile("C:\Documents and Settings\flow_model\flow.exe")