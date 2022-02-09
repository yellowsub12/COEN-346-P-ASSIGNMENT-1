from glob import escape
import os

def read_file() :
    counter = 0
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

def echo(string1) :
    return string1

def main():
    shell_name = read_file()
    command = str
    while command != "exit":
        command = input(shell_name + " ")
        if "echo" in command:
            a = command[6:-1:1]
            print(shell_name + " " + echo(a))
        elif "exit" in command:
            break

