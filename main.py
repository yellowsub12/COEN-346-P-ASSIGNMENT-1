#the find(pattern, path) function is a snippet code from StackOverflow

import os
import pwd
import shutil
import re
import fnmatch
userInput = str
loopInt=1

def name_host() :
    open_file = open("file.txt", "r")
    name = open_file.readline()
    host = open_file.readline()
    path = open_file.readline()
    name = name[:-1]
    host = host[:-1]
    path = path[:-1]
    prompt = name + host
    return name + "@" + host + "$"
    open_file.close()

def read_path():
    open_file = open("file.txt", "r")
    temp = open_file.readline()
    temp = open_file.readline()
    path = open_file.readline()
    path = path[:-1]
    return path
    open_file.close()

#This function finds an .exe file in a given path/directory, warning, may give too many results
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    print(result)
    return result

find('*.exe', '/home/yaqub/HelloWorld/')

#actual loop where commands are given until 'exit' is typed to stop the program
while loopInt>0:
    shell_name = name_host()
    userInput = input(shell_name + " ")
    if userInput == "exit":
        break


    if ".exe" in userInput: 
        pattern = "(.*?).exe"
        substring = re.search(pattern, userInput).group(1)
        substringA = "./"+substring+".exe"
        print(substringA)
        userInputstringA = re.sub(r'->', '>', substringA)
        os.system(userInputstringA)
    


    else:
        userInputstring = re.sub(r'->', '>', userInput)
        os.system(userInputstring)



#print(shutil.which("notepad.exe"))
#os.startfile(shutil.which("notepad.exe"))
