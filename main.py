#the find(pattern, path) function is a snippet code from StackOverflow

import os
import shutil
import re
import fnmatch
userInput = str
loopInt=1

def name_host() :
    open_file = open("file.txt", "r")
    name = open_file.readline()
    host = open_file.readline()
    name = name[:-1]
    host = host[:-1]
    return name + "@" + host + "$"
    open_file.close()

def read_path():
    open_file = open("file.txt", "r")
    temp = open_file.readline()
    temp = open_file.readline()
    path = open_file.readline()
    path = path[5::]
    return path
    open_file.close()

def sort_path():
    string_path = read_path()
    count = 0
    for char in string_path:
        if char == ",":
            count = count + 1
    count = count + 1
    path_array = [0] * count
    j = 0
    h = 0
    i = 0
    first_char = string_path[0]
    for letter in string_path:
        if letter == "," and i == 0:
            path_array[j] = first_char + string_path[:-1]
            h = i
            i = i + 1
            j = j + 1
        elif letter == "," :
            path_array[j] = string_path[h+1:i]
            h = i
            i = i + 1
            j = j + 1
        else:
            i = i + 1
            continue

    path_array[j] = string_path[h+1:i]
    return str(path_array[2])


#This function finds an .exe file in a given path/directory, warning, may give too many results
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


#actual loop where commands are given until 'exit' is typed to stop the program
while loopInt>0:
    shell_name = name_host()
    os.system("cd " + sort_path())
    print(read_path()) #to remove for submission. Only here for testing purpose
    userInput = input(shell_name + " ")
    if userInput == "exit":
        break


    if ".exe" in userInput: 
        pattern = "(.*?).exe"
        substring = re.search(pattern, userInput).group(1)
        substringA = substring+".exe"
        if find(substringA, read_path()) == "[]":
                print("This executable file hasn't been found in the path! Start again!")
                continue
        elif find(substringA, read_path()) != "[]":
                print("Executable file provided found at " + find(substring, read_path()))
                substringB = find(substringA, read_path()) 
        userInputstringA = re.sub(r'->', '>', substringB)
        os.system(userInputstringA)
    


    else:
        userInputstring = re.sub(r'->', '>', userInput)
        os.system(userInputstring)

