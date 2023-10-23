import time
from os import system

def clear ():
  system('clear')

print("System Start up Commencing")

def loading (clear):
  clear()
  print("=========================================")
  time.sleep(0.01)
  print("|               ARDos                   |")
  time.sleep(0.01)
  print("| ------                                |")
  time.sleep(0.01)
  print("|          Version 4.1.2                |")
  time.sleep(0.01)
  print("|                                       |")
  time.sleep(0.01)
  print("|                                       |")
  time.sleep(0.01)
  print("|               |                       |")
  time.sleep(0.01)       
  print("|                                       |")
  time.sleep(0.01)
  print("|                                       |")
  time.sleep(0.01)
  print("=========================================")
  time.sleep(0.5)
  clear()
  print("=========================================")

  print("|               ARDos                   |")
  
  print("| ------                                |")
 
  print("|          Version 4.1.2                |")

  print("|                                       |")
  
  print("|                                       |")
 
  print("|               /                       |")
     
  print("|                                       |")

  print("|                                       |")
 
  print("=========================================")
  time.sleep(0.5)   
  clear()
  print("=========================================")
 
  print("|               ARDos                   |")
 
  print("| ------                                |")
  
  print("|          Version 4.1.2                |")
  
  print("|                                       |")

  print("|                                       |")
  
  print("|               -                       |")
     
  print("|                                       |")
 
  print("|                                       |")

  print("=========================================")
  time.sleep(0.5)
  clear()
  print("=========================================")

  print("|               ARDos                   |")
 
  print("| ------                                |")
 
  print("|          Version 4.1.2                |")
 
  print("|                                       |")

  print("|                                       |")

  print("|               \                       |")
     
  print("|                                       |")

  print("|                                       |")

#boot start up
time.sleep(3)
inp=""
def startupchoice(inp):
    print("press 'b' for bios")
    print("press 's' for system boot up")
    print("press 'i' for sys info")
    
    inp=input("enter choice here: ")

startupchoice(inp)

if inp=="b":
    clear()
    import platform 
    my_system = platform.uname()
    print(f"System: {my_system.system}")
    print(f"Node Name: {my_system.node}")
    print(f"Release: {my_system.release}")
    print(f"Version: {my_system.version}")
    print(f"Machine: {my_system.machine}")
    print(f"Processor: {my_system.processor}")
clear()
time.sleep(10)
startupchoice(inp)

if inp=="s":
    loading(clear)