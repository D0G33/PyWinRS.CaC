import os
from multiprocessing import Process

def zip(file,name="package"):
    os.system("del "+name+".7z")
    os.system("tools\\7zr.exe a "+name+".7z "+file+"")

def unzip(file):
    os.system("mkdir Extracted")
    os.system('tools\\7zr.exe e '+file)

