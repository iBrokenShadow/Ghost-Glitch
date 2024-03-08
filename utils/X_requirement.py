#!/usr/bin/env python3
import os
import subprocess
import sys


# Console colors
W = '\033[0m'  # white (normal)
R = '\033[31m'  # red
G = '\033[32m'  # green
O = '\033[33m'  # orange
B = '\033[34m'  # blue
P = '\033[35m'  # purple
C = '\033[36m'  # cyan
GR = '\033[37m'  # gray

def print_banner():
    os.system("clear")
    logo = """ 
░██████╗░██╗░░██╗░█████╗░░██████╗████████╗░░░░░░░██████╗░██╗░░░░░██╗████████╗░█████╗░██╗░░██╗
██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝░░░░░░██╔════╝░██║░░░░░██║╚══██╔══╝██╔══██╗██║░░██║
██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░█████╗██║░░██╗░██║░░░░░██║░░░██║░░░██║░░╚═╝███████║
██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░╚════╝██║░░╚██╗██║░░░░░██║░░░██║░░░██║░░██╗██╔══██║
╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░░░░╚██████╔╝███████╗██║░░░██║░░░╚█████╔╝██║░░██║
░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

    """
    print(R + logo + W)
    
    
def footer_banner():
    header = "\n\n\n\t-------------------------------------------------------------"
    header2 = "\t-------------------------------------------------------------"
    MainHeader = "\tREPORT ANY ERROR FOR FIXES (Thanks for your Contribution)"
    mainMessage = """
        Given Contacts : Telegram  : https://t.me/iBrokenShadow
                       : Instagram : https://www.instagram.com/iBrokenShadow/
                       : Github    : https://github.com/iBrokenShadow
    """
    Terrr2 = "\tThanks! visit https://ibrokenshadow.com"
    
    try:
        print(C + header + W)
        print(R + MainHeader + W)
        print(W + mainMessage + W)
        print(G + Terrr2 + W)
        print(C + header2 + W)
        input("\n\nPress Enter to close!")
    except KeyboardInterrupt:
        sys.exit(0)
    
    

def check_files_existence():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    script_dir_back = script_dir[:-5]
    
    files = [
        os.path.join(script_dir_back, "ghost-glitch.sh"),
        os.path.join(script_dir_back, "ghost-glitch.py"),
        os.path.join(script_dir_back, "README.md"),
        os.path.join(script_dir, "B_handleDumpAirodump-ng.py"),
        os.path.join(script_dir, "B_handleDumpAirodump-ng.py"),
        os.path.join(script_dir, "C_captureHandshake.py"),
        os.path.join(script_dir, "X_requirement.py")
    ]
    missing_files = []

    for file in files:
        if not os.path.isfile(file):
            missing_files.append(file)

    if missing_files:
        print_banner()
        print("\033[91m\n\n--------------------------------------------------------------")
        print("\033[91mERROR: The following files are missing:\n")
        for missing_file in missing_files:
            print("--> ", missing_file)
        print("\nScript will make issues without the presence of all needed files!")
        print("--------------------------------------------------------------")
        print("\033[32m")
        print("Download All Files Now from given Repo:\nhttps://github.com/iBrokenShadow/Ghost-Glitch\n")
        print("\033[0m")  # Reset color
        footer_banner()
        exit(1)

check_files_existence()

def check_installation():
    
    try:
        script_dir = os.path.dirname(os.path.realpath(__file__))
        script_dir_back = script_dir[:-5]
        main_file = os.path.join(script_dir_back, "ghost-glitch.py")
        
        # # Check if lsb_release command is available
        # subprocess.run(["lsb_release"], check=True)

        # Check the distribution ID
        distribution = subprocess.run(["lsb_release", "-si"], capture_output=True, text=True, check=True).stdout.strip()

        # Define the list of Debian-based distributions
        debian_based = ["Debian", "Kali", "Ubuntu", "Parrot"]

        # Check if the distribution is Debian-based
        if distribution not in debian_based:
            print_banner()
            print("\033[91m\n\nERROR:\n\nThis script is intended to run on (Debian - Ubuntu - KaliLinux - ParrotOS) systems only.")
            print("We'll soon release it on Other Distros\n")
            print("\033[0m")  # Reset color
            footer_banner()
            return False

        # Define required packages
        required_packages = ["figlet", "mdk4", "aircrack-ng", "python3", "lsb-release"]

        # Initialize variable to store missing packages
        missing_packages = []

        # Check if required packages are installed
        for package in required_packages:
            result = subprocess.run(["dpkg", "-s", package], capture_output=True, text=True)
            if result.returncode != 0:
                missing_packages.append(package)

        # If there are missing packages, display error with missing packages highlighted
        if missing_packages:
            print_banner()
            print("\033[91m\n\n--------------------------------------------------------------")
            print("\033[91mError: Some required packages are not installed:\n")
            for package in missing_packages:
                print(f" - {package}")
            print("--------------------------------------------------------------\n")
            print("\033[0m")  # Reset color
            footer_banner()
            return False

        # Run the Python file
        # subprocess.run(["python3", main_file])
        return True

    except subprocess.CalledProcessError:
        print_banner()
        print("\033[91m\n\nERROR:\n\nlsb_release command not found. This script requires lsb_release to run.\n")
        print("\033[0m")  # Reset color
        footer_banner()
        return False

    except KeyboardInterrupt:
        return False



if __name__ == "__main__":
    if not check_installation():
        exit(1)