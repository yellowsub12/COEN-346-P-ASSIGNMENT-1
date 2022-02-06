import os
import pwd
import shutil
import re
wacky = str
#main function
while wacky != "exit":
    wacky = input()
    if wacky == "exit":
        break

    if "./" and ".exe" in wacky: 
        pattern = "./(.*?).exe"
        substring = re.search(pattern, wacky).group(1)
        substringA = substring+".exe"
        print(substringA)
        shutil.copy(str(shutil.which(substring)), str(pwd) )
       # os.startfile(shutil.which("notepad.exe"))
        wackystring = re.sub(r'->', '>', wacky)
        os.system(wackystring)

    else:
        wackystring = re.sub(r'->', '>', wacky)
        os.system(wackystring)

#To find .exe file here, warning, gives too many results, should be integrated to main
import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    print(result)
    return result
find('*.exe', '/home/usr/HelloWorld/')

#If you enter ./example.exe, this can root out example and throw example.exe to the filer locator 
wacky = input()
if "./" and ".exe" in wacky: 
        pattern = "./(.*?).exe"
        substring = re.search(pattern, wacky).group(1)
        substringA = substring+".exe"
        print(substringA)
        print(shutil.which(substringA))

#MISC
#print(shutil.which("notepad.exe"))
#os.startfile(shutil.which("notepad.exe"))
