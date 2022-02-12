#Program written by Ali Turkman (40111059), Mattieu Pourrat (40089209) and Zeineb Ben Mami (40024877) 
#find() function code snippet from StackOverflow
import os
import re
import fnmatch
import threading

#first string that designates what will be user string
userInput = str
#loop integer to keep while loop going until exit command breaks it
loopInt=1

#path used to find the file.txt that will be given, integral for both functions below
absolute_path = os.getcwd()

#reads the file.txt file provided to acquire the host name that will be used in the shell
def name_host() :
    open_file = open(absolute_path + "/file.txt", "r")
    name = open_file.readline()
    host = open_file.readline()
    name = name[:-1]
    host = host[:-1]
    open_file.close()
    return name + "@" + host + "$"
    

#reads the file.txt file provided to acquire the PATH from which many paths are given
def read_path():
    open_file = open(absolute_path + "/file.txt", "r")
    temp = open_file.readline()
    temp = open_file.readline()
    path = open_file.readline()
    path = path[5::]
    open_file.close()
    return path
    

#This function finds an .exe file in a given path/directory, searches all subdirectories warning, may give too many results
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#Detects the word 'cd' to do cd function. Meaning program doesn't call on bash cd function
def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

shell_name = name_host()
path_string = read_path()
#the string.split(‘,’) function is used to divide the PATH provided into different usable paths to navigate, and stores every path in an array.
value = path_string.split(',')

#actual loop where commands are given until 'exit' is typed to stop the program
while loopInt>0:
    userInput = input(shell_name + " ")
    if userInput == "exit":
        break
        

#If no path is given, then the program will assume it’s a universal .exe file that can be ran from anywhere (like notepad.exe) and will run it. 
#If the user wants to rule a local .exe file then they should use ./file.exe as expected with regular terminals.
    if ".exe" in userInput: 
        pattern = "(.*?).exe"
        substring = re.search(pattern, userInput).group(1)
        substringA = substring+".exe"

        i=0
        #It will run it into every PATH provided and will output which path holds the file.exe named. 
        while i<len(value):
            if find(substringA, value[i]) != []:
                print("Executable file provided found at " + str(find(substringA, value[i])))
                os.chdir(value[i])
                userInputstringA = re.sub(r'->', '>', value[i])
                os.system(userInputstringA)
                if "&" in userInput:
                    t1 = threading.Thread(target=os.system, args=(substringA,))
                    t1.start()
                else:
                    t2 = threading.Thread(target=os.system, args=(substringA,))
                    t2.start()
                    t2.join()
                break
            #If no path is given, then the program will assume it’s a universal .exe file that can be ran from anywhere (like notepad.exe) and will run it. 
            else: 
                i+=1   
                if i==len(value): 
                    if "&" in userInput:
                        t1 = threading.Thread(target=os.system, args=(substringA,))
                        t1.start()
                    else:
                        t2 = threading.Thread(target=os.system, args=(substringA,))
                        t2.start()
                        t2.join()
             
 
    #Detects cd input, then navigates to directory there after splitting cd [directory] input
    elif findWholeWord('cd')(userInput) != None:
        userInputstring = re.sub(r'->', '>', userInput)
        os.chdir(userInputstring.split()[1])
    
   #uses regular expressions to transform -> and ->> into > and >> which are actually bash/command functions
    else:
        userInputstring = re.sub(r'->', '>', userInput)
        if "&" in userInput:
            t1 = threading.Thread(target=os.system, args=(userInputstring,))
            t1.start()
        else:
            t2 = threading.Thread(target=os.system, args=(userInputstring,))
            t2.start()
            t2.join()

  
