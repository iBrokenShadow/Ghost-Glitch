#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
-------------------------------------------------------------
This tool is solely made by Broken Shadow
Contact for any Issues: Telegram  : https://t.me/iBrokenShadow
                      : Instagram : https://www.instagram.com/iBrokenShadow/
                      : Github    : https://github.com/iBrokenShadow
visit https://ibrokenshadow.com
-------------------------------------------------------------

README : Make Sure to read ReadMe File first: 
Bugs and Improvements will be done post reporting


----------------WORKING & METHODOLOGY----------------
It's a Wi-Fi Hacking Automated Tool, that can be used in suck many cases

+ To Enable or Disable Monitor Mode (With Inbuilt Functions)
+ TO Catch all wifi Networks on 2.4Ghz / 5Ghz or Both and then Make them in a categorized Manner to get most details out of them possible,
  it then convert it to CSV and add WPS info if they have WPS enabled and if it's locked or not

+ Then Select a Network and it'll show all the details for that Specific BSSID, then you can start monitoring that and , It'll then Start 
  De-authentication attack, with all connecetd clients sperately, and when Handshake get captured , it'll automatically stop and ask for further options
  you can also not opt for deauthentication attack and perform any other way possible to get handhsake while this tool keeps capturing the packets 

+ More Features are getting added while I'm working on this
"""

# iBrokenShadow 
# Made by Broken Shadow

import psutil
import subprocess
import time
import sys
import os
from utils.X_requirement import check_installation
requirements_satisfied = check_installation()


# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

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
    
def is_run_with_sudo():
    return os.geteuid() == 0

if is_run_with_sudo() == False:
    run(["figlet", "ERROR !!!"])
    print(R+ "\n\nPlease run with sudo privileges...\n\n")
    print("\n") ; input("Press Any Key to quit..") ; print(GR)
    sys.exit()

# REQUIREMENTS
def requirements():
    try: 
        if requirements_satisfied == False: sys.exit(0)
    except KeyboardInterrupt: sys.exit(0)
    except: sys.exit(0)



def exit_pause():
    print("\n" + O) ; input("Press Any Key to quit...") ; exit()

def Del_Current_Line():
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def Del_Pre_Line():
    print("\033[F\033[K", end="", flush=True)

def clear_lines(num_lines):
    # Clear lines from the current line up to num_lines lines above
    for _ in range(num_lines):
        sys.stdout.write("\033[F")  # Move cursor to the beginning of the previous line
        sys.stdout.write("\033[K")  # Clear the line
    sys.stdout.flush()
    
# CLEAR SCREEN
def clear():
    subprocess.run("clear")



######################################################################################
# RETURN ALL INTERFACE NAMES TO A VARIABLE
def list_connected_interfaces():
    global iterate ; iterate = 0
    output = subprocess.run(['airmon-ng'], capture_output=True, text=True).stdout
    connected_interfaces = []
    for line in output.split('\n')[2:]:
        columns = line.split()
        if len(columns) >= 4:
            connected_interfaces.append(columns[1])
            iterate += 1
    return connected_interfaces


def get_interface_info():
    output = subprocess.run(['airmon-ng'], capture_output=True, text=True).stdout
    interface_info = []
    for line in output.split('\n')[2:]:
        columns = line.split()
        if len(columns) >= 4:
            phy_info = columns[0]
            interface_name = columns[1]
            driver = columns[2]
            chipset = ' '.join(columns[3:])
            interface_info.append((phy_info, interface_name, driver, chipset))
    return interface_info


def list_Interface():
    print(O + "Connected interfaces:\n")
    print("No.   PHY   Interface       Driver      Chipset")
    print("------------------------------------------------"+ GR)
    
    interface_info = get_interface_info()
    counter = 1
    
    for phy_info,interface, driver, chipset in interface_info:
        if is_monitor_mode_enabled(interface) == True:
            print(P+ f"{counter}.    {phy_info:<7}{interface:<15}{driver:<12}{chipset}" + GR)
            print(W+ f"\t\t\t   (Monitor Mode Already Enabled on \"{interface}\")" + GR)
            counter += 1
        else:
            print(P+ f"{counter}.    {phy_info:<7}{interface:<15}{driver:<12}{chipset}" + GR)
            counter += 1


####################################################################################
# SIMPLE ANIMATION
def loading_animation(text, TimeDelay):
    chars = "/—\|"  # Characters for the animation
    start_time = time.time()
    while time.time() - start_time < TimeDelay:
        for char in chars:
            sys.stdout.write('\r' + text + char)
            sys.stdout.flush() ; time.sleep(0.05)
            
# SMART LOAD
def SmartLoading():
    char = '.'
    start_time = time.time()
    i = 0
    while time.time() - start_time < 1:
        print(char) ; time.sleep(0.1) ; i += 1
    clear_lines(i)
    
    

            

# ENABLE MONITOR MODE (IWCONFIG & AIRMON-NG)
def Enable_Monitor_Mode(interface):
    global modeOFmonitor
    def enable_monitor_mode_iwconfig(interface):
        i = 0
        while i<2:
            subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
            if i==1: print(W + "\t[+] Interface", interface, "Turned Down...") ; time.sleep(1)

            subprocess.run(["sudo", "iwconfig", interface, "mode", "monitor"], check=True)
            if i==1: print("\t[+] Interface", interface, "Mode Changed...") ; time.sleep(1)

            subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
            if i==1: print("\t[+] Interface", interface, "Turned UP...") ; time.sleep(1)

            subprocess.run(["sudo", "airmon-ng", "check", "kill"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if i==1: print("\t[+] All Pending process killed..." + GR) ; time.sleep(1)
            if i==1: sys.stdout.write("\033[F\033[K" * 4)

            if i==1: 
                print(f"Monitor Mode Enabled on {interface}\n")
                subprocess.run(["iwconfig", interface])
                print("-----" *5) ; print("\n")
            i = i+1
                
    def enable_monitor_mode_airmonNG(interface):
        print(W)
        processCHECK = subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
        interface = interface + "mon"
            
        time.sleep(0.5) ; clear() ; bann_text() ; SmartLoading()
        print(O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR)

        print(f"Monitor Mode Enabled on {interface}\n")
        subprocess.run(["iwconfig", interface])
        print("-----" *5) ; print("\n")
            
    
    # MAIN ASE
    try:
        enable_monitor_mode_airmonNG(interface)
        modeOFmonitor = 0
        print(R + "\nSome Running processes can cause issue (Kill Them): ~[sudo airmon-ng check kill]~" + G)
        
    except subprocess.CalledProcessError as e:
        time.sleep(0.5) ; clear() ; bann_text() ; SmartLoading()
        print(O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR)
        
        enable_monitor_mode_iwconfig(interface) ; modeOFmonitor = 1
        print(R + "\nEnable Network Services: ~[sudo service NetworkManager start]~" + G)
        
    except KeyboardInterrupt:
        print("\n\n\nERROR: BYE") ; ReportError() ; exit_pause()
    except Exception as e:
        clear() ; print(f"ERROR: {1}") ; ReportError() ; exit_pause()




# MONITOR MODE DISABLE
def disable_monitor_mode(interface):
    global modeOFmonitorDisable
    def disable_monitor_mode_iwconfig(interface):
        texxt = "Turning Monitor Mode Off on : " + interface + " "
        loading_animation(texxt, 1.5) ; Del_Current_Line()

        subprocess.run(["sudo", "ifconfig", interface, "down"], check=True)
        print(W+"\t[+] Interface", interface, "Turned Down...") ; time.sleep(1)

        subprocess.run(["sudo", "iwconfig", interface, "mode", "managed"], check=True)
        subprocess.run(["sudo", "iwconfig", interface, "mode", "managed"], check=True)
        print("\t[+] Interface", interface, "Mode Changed...") ; time.sleep(1)

        subprocess.run(["sudo", "ifconfig", interface, "up"], check=True)
        print("\t[+] Interface", interface, "Turned UP...") ; time.sleep(1)

        subprocess.run(["sudo", "service", "NetworkManager", "start"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("\t[+] Network Manager service started..."+GR) ; time.sleep(1)
        sys.stdout.write("\033[F\033[K" * 4)

        clear() ; bann_text()
        print(f"Monitor Mode Disabled on : {interface}\n")
        time.sleep(1) ; print("-----" *5)
        subprocess.run(["iwconfig", interface])
        print("-----" *5) ; print("\n")
                    
    def disable_monitor_mode_airmonNG(interface):
        print(W)
        processCHECK = subprocess.run(["sudo", "airmon-ng", "stop", interface], check=True)
        interface = interface[:-3]
            
        time.sleep(0.5) ; clear() ; bann_text() ; SmartLoading()
        print(O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR)

        print(f"Monitor Mode Disabled on : {interface}\n")
        subprocess.run(["iwconfig", interface])
        print("-----" *5) ; print("\n")
        
        
    
    # MAIN ASE
    try:
        disable_monitor_mode_airmonNG(interface)
        modeOFmonitor = 0
        
    except subprocess.CalledProcessError as e:
        time.sleep(0.5) ; clear() ; bann_text() ; SmartLoading()
        print(O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR)
            
        disable_monitor_mode_iwconfig(interface) ; modeOFmonitor = 1
        
    except Exception as e:
        clear() ; print(f"ERROR: {e}") ; ReportError() ; exit_pause()
    except KeyboardInterrupt:
        print("\n\n\nERROR: BYE") ; ReportError() ; exit_pause()


        
        
        

# Check if Monitor Mode is already Enabled
def is_monitor_mode_enabled(interface):
    try:
        result = subprocess.run(["iwconfig", interface], capture_output=True, text=True)
        if "Mode:Monitor" in result.stdout:
            return True
        else:
            return False
    except subprocess.CalledProcessError as e:
        print(R+ f"Error checking monitor mode for {interface}: {e}" + GR)
        return False

# USER RESPONSE ON DISBALING MONITOR MODE
def DoIdisable(interface):
    try:
        user_input = input(P + "(( Disable Monitor Mode? (y/n) ))  "+GR) ; Del_Pre_Line()
        if len(user_input) != 1:
            print(R+ "ERROR! Input must be a single character...")
            exit_pause()
            
        # Process the input here
        if user_input.lower() == 'y':
            # IF MONITOR MORE IS ALREADY DISABLED THERE
            monitor_mode_enabled = is_monitor_mode_enabled(interface)
            if monitor_mode_enabled == False:
                loading_animation("Wait... ", 1.5) ; Del_Current_Line()
                print(O + f"Monitor Mode is already Disabled on interface : {interface}\n", GR)
                
                time.sleep(1) ; print("-----" *5)
                subprocess.run(["iwconfig", interface])
                print("-----" *5) ; exit_pause()
            else:
                disable_monitor_mode(interface)
                interface = interface[:-3]
            
    except ValueError as e:
        print(R+ "Error:", e) ; print(GR) ; ReportError() ; 
        exit_pause()
    


def runDumpFile(res, ghz, path, selected_interface):
    clear() ; bann_text()
    print(O+ f"[[ Selected interface: \"{selected_interface}\" ]]\n.\n." + GR)
    i = 1 ; j = 1 ; k = 1
    while i == 1:
        if j == 1:
            check = is_monitor_mode_enabled(selected_interface)
            if check == True: 
                if k == 1:
                    loading_animation(f"Airodump-ng Starting on {ghz}... ", 1.5) ; Del_Current_Line()
                    dumpFile = path + "utils/B_handleDumpAirodump-ng.py"
                    subprocess.run(['sudo', 'python', dumpFile, selected_interface, res, path])
                    exit ; k=k+1
                    
            else: 
                loading_animation("Turning On Monitor Mode! Wait... ", 1)
                Del_Current_Line()
                Enable_Monitor_Mode(selected_interface) ; j = 2
                if modeOFmonitor == 0: selected_interface = selected_interface + "mon"
                time.sleep(1)

        elif j == 2: 
            if k == 1:
                dumpFile = path + "utils/B_handleDumpAirodump-ng.py"
                subprocess.run(['sudo', 'python', dumpFile, selected_interface, res, path])
                exit ; k=k+1



#######################################################################################################
#
#######################################################################################################
# MAIN FUNCTION
try:
    requirements() ; bann_text() # ; global selected_interface
    # Get path exact name where the script is stored
    path = os.path.abspath(os.path.dirname(__file__)) + "/"
    connected_interfaces = list_connected_interfaces()

    if connected_interfaces:
        loading_animation("Searching Intefaces ", 1) ; clear()
        bann_text() ; list_Interface()
        
        i = 0 ; looped = 0
        while i == 0:
            try:
                # print(iterate)  ; input()
                # If only one interface then automatically choose 1st one
                if iterate == 1: 
                    choice = 1 ; print(O+ "\n")
                    loading_animation("Selecting Interface Automatically... ", 1.8)
                    
                    
                else: choice = int(input("\n\nSelect an interface by number: ")) ; print(GR)
                
                if 1 <= choice <= len(connected_interfaces):
                    selected_interface = connected_interfaces[choice - 1]
                    break
                else:
                    clear() ; bann_text() ; time.sleep(0.4) ; print(R)
                    print("Invalid choice!!! Please select a valid interface number.")
                    input("\nPress any key to start again... ") ; print(GR)
                    clear() ; bann_text() ; SmartLoading() ; list_Interface()

            except ValueError:
                clear() ; bann_text() ; time.sleep(0.4) ; print(R)
                print("Invalid input. Please enter a number.")
                input("\nPress any key to start again... ") ; print(GR)
                clear() ; bann_text() ;  SmartLoading() ; list_Interface()
                
                
        # Start Loop to Ask Options      
        i = 0 ; looped = 0
        while i == 0:
            clear()
            bann_text()
            if looped == 1: SmartLoading()
            
            print(O+ f"[[ Selected interface: \"{selected_interface}\" ]]\n" + P)

                # OPTION to Turn on Monitor Mode or Turn it Off or Dump
            print("1. Turn ON Monitor Mode")
            print("2. Turn OFF Monitor Mode")
            print("3. Start Dumping Targets on 2.4Ghz")
            print("4. Start Dumping Targets on 5.0Ghz")
            print("5. Start Dumping Targets on Both Channels" + GR)

            try:
                res = int(input("\nResponse : "))
                if res == 1:
                    clear() ; bann_text()
                    print(O+ f"[[ Selected interface: \"{selected_interface}\" ]]\n.\n." + GR)

                    # Turn on monitor mode
                    monitor_mode_enabled = is_monitor_mode_enabled(selected_interface)
                    if monitor_mode_enabled:
                        loading_animation("Wait... ", 1.5) ; Del_Current_Line()
                        print(O+ f"Monitor Mode is already enabled on interface : {selected_interface}\n" + GR)
                        
                        time.sleep(1) ; print("-----" *5)
                        subprocess.run(["iwconfig", selected_interface])
                        print("-----" *5) ; 
                        
                        time.sleep(0.5)
                        print(R + "\n\nEnable Network Services: ~[sudo service NetworkManager start]~\n" + G)
                        DoIdisable(selected_interface) ; exit_pause()

                    texxt = "Enabling Monitor Mode on " + selected_interface + " "
                    loading_animation(texxt, 1.5) ; Del_Current_Line()

                    Enable_Monitor_Mode(selected_interface) ; time.sleep(0.5)
                    if modeOFmonitor == 0: selected_interface = selected_interface + "mon"
                    exit_pause() ; i = 1

                # Turn off monitor mode
                elif res == 2:
                    clear() ; bann_text()
                    print(O+ f"[[ Selected interface: \"{selected_interface}\" ]]\n.\n." + GR)
                    disable_monitor_mode(selected_interface)
                    selected_interface = selected_interface[:-3] ; exit_pause() ; i = 1
                
                # Start Dumping program (Start Dumping Targets)
                elif res == 3:
                    runDumpFile("bg", "2.4Ghz", path, selected_interface) ; i = 1
                elif res == 4:
                    runDumpFile("a", "5.0Ghz", path, selected_interface) ; i = 1
                elif res == 5:
                    runDumpFile("abg", "Both Channels", path, selected_interface) ; i = 1

                
                # IF user enters invalid option
                else:
                    clear() ; bann_text() ; time.sleep(0.4) ; print(R)
                    print("Invalid choice!!! Please select a valid interface number.")
                    input("\nPress any key to start again... ") ; looped = 1 ; print(GR)
                    
            except ValueError:
                clear() ; bann_text() ; time.sleep(0.4) ; print(R)
                print("Invalid input. Please enter a number.")
                input("\nPress any key to start again... ") ; looped = 1 ; print(GR)
        # LOOP ENDS
        

    else:
        bann_text()
        print(R+ "\n\nNo connected interfaces found." + GR)
        exit_pause()


except KeyboardInterrupt:
    time.sleep(0.3) ; ReportError() ; sys.exit()


# # Define variables to pass to the second script
# variables_to_pass = ['Hello', 'World', 42, True]

# # Run the second script and pass variables to it
# subprocess.run(['python', 'second_script.py'] + [str(variable) for variable in variables_to_pass])
#---------------------------------------------------------------
# # Retrieve the variables passed from the first script
# variables_passed = sys.argv[1:]

# # Print the variables
# for idx, var in enumerate(variables_passed, start=1):
#     print(f"Variable {idx}: {var}")
