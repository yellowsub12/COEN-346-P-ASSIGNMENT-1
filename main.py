import os
import re
import fnmatch
userInput = str
loopInt=1

absolute_path = os.getcwd()

def name_host() :
    open_file = open(absolute_path + "/file.txt", "r")
    name = open_file.readline()
    host = open_file.readline()
    name = name[:-1]
    host = host[:-1]
    open_file.close()
    return name + "@" + host + "$"
    

def read_path():
    open_file = open(absolute_path + "/file.txt", "r")
    temp = open_file.readline()
    temp = open_file.readline()
    path = open_file.readline()
    path = path[5::]
    open_file.close()
    return path
    

#This function finds an .exe file in a given path/directory, warning, may give too many results
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

shell_name = name_host()
path_string = read_path()
value = path_string.split(',')

#actual loop where commands are given until 'exit' is typed to stop the program
while loopInt>0:
    userInput = input(shell_name + " ")
    if userInput == "exit":
        break

    if ".exe" in userInput: 
        pattern = "(.*?).exe"
        substring = re.search(pattern, userInput).group(1)
        substringA = substring+".exe"
        i=0
        while i<len(value):
            if find(substringA, value[i]) != []:
                print("Executable file provided found at " + str(find(substringA, value[i])))
                os.chdir(value[i])
                print(os.getcwd())
                userInputstringA = re.sub(r'->', '>', value[i])
                os.system(userInputstringA)
            i+=1        
 #      userInputstringA = re.sub(r'->', '>', value[i])
 #      os.system(userInputstringA)

    elif findWholeWord('cd')(userInput) != None:
        userInputstring = re.sub(r'->', '>', userInput)
        userInputstringA = re.sub(r'\W.', ' ', userInputstring)
        os.chdir(userInputstringA.split()[1])
    
    else:
        userInputstring = re.sub(r'->', '>', userInput)
        os.system(userInputstring)
