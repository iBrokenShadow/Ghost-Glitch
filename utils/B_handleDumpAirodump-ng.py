#!/usr/bin/python
# -*- coding: UTF-8 -*-

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
    sys.exit(1)


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
    
    
def is_run_with_sudo():
    return os.geteuid() == 0

if is_run_with_sudo() == False:
    print("ERROR!!!\n\nPlease run with sudo privileges...\n\n")
    print("\n") ; time.sleep(0.2) ; ReportError() ; sys.exit(1)

subprocess.run("clear")

# Variables Passed from 1st Program
try:
    interface = sys.argv[1]
    res = sys.argv[2]
    path = sys.argv[3]
except:
    print("NO Interface or Mode or Path Provided!\n\nexample:\n\tsudo python -u \"scriptName.py\" interface-name mode(a/b/g) \"PATH TO ghostglitch.py File\"" )
    print("\n") ; 
    try: input("Press Any Key to quit...")
    except KeyboardInterrupt: time.sleep(0.2) ; ReportError() ; sys.exit(1)
    sys.exit(0)

def exit_pause():
    print("\n") ; input("Press Any Key to quit...")

def Del_Current_Line():
    sys.stdout.write("\r\033[K")
    sys.stdout.flush()

def Del_Pre_Line():
    print("\033[F\033[K", end="", flush=True)

# CLEAR SCREEN
def clear():
    subprocess.run("clear")


# REQUIREMENTS
def requirements():
    print("")


# SIMPLE ANIMATION
def loading_animation(text):
    chars = "/—\|"  # Characters for the animation
    start_time = time.time()
    while time.time() - start_time < 1.5:
        for char in chars:
            sys.stdout.write('\r' + text + char)
            sys.stdout.flush()
            time.sleep(0.05)
            
            
# SMART LOAD
def SmartLoading():
    char = '.'
    start_time = time.time()
    i = 0
    while time.time() - start_time < 1:
        print(char) ; time.sleep(0.1) ; i += 1
    clear_lines(i)
    
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
  
    
def clear_lines(num_lines):
    # Clear lines from the current line up to num_lines lines above
    for _ in range(num_lines):
        sys.stdout.write("\033[F")  # Move cursor to the beginning of the previous line
        sys.stdout.write("\033[K")  # Clear the line
    sys.stdout.flush()
    
    

# MONITOR MODE ENABLE
def enable_monitor_mode(interface):
    x = 0

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
        modeOFmonitor = 0
        
    except subprocess.CalledProcessError as e:
        time.sleep(0.5) ; clear() ; bann_text() ; SmartLoading()
        text = O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR ; SlowType(text)
            
        disable_monitor_mode_iwconfig(interface) ; modeOFmonitor = 1
        
    except Exception as e:
        clear() ; print("\n\n") ; text = f"ERROR: {e}" ; SlowType(text) ; ReportError() ; exit_pause()
    except KeyboardInterrupt:
        SlowType("\n\n\nERROR: BYE") ; ReportError() ; exit_pause()


# Change Interface Name to Ghost        
def change_interface_name(interface, new_name):
    
    def get_next_interface_name(base_name):
        i = 0
        while True:
            if interface.endswith("mon"):
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

    def rename_interface(interface, new_name):
        try:
            subprocess.run(['ip', 'link', 'set', interface, 'down'])
            subprocess.run(['ip', 'link', 'set', interface, 'name', new_name])
            subprocess.run(['ip', 'link', 'set', new_name, 'up'])
        except Exception as e:
            print(f"\n\n\n\nERROR 128: {e}")
            time.sleep(0.2) ; ReportError() ; sys.exit(1)
            
            
    # MAIN ASE
    if interface[:5].lower() == "ghost":
        try:
            next_name = get_next_interface_name(new_name)
            rename_interface(interface, next_name)
            return next_name
        except Exception as e:
            print(f"\n\n\n\nERROR 1689: {e}")
            time.sleep(0.2) ; ReportError() ; sys.exit(1)
    else: return "none"

    




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

#------------------------------------------------------------------------------------------------------
# DUMP BSSIDs command 
def run_airodump(interface, CSVfilePath, wpsFile):
    try:
        command  = ['sudo', 'airodump-ng', interface,
                    '--write', CSVfilePath, '--wps',
                    '--band', res, '--output-format',
                    'csv', '--write-interval', '2']
        command2 = f"wash -i {interface} > {wpsFile} &"
        # Start the airodump-ng process
        process = subprocess.Popen(command)
        process2 = subprocess.Popen(command2, shell=True)
        
        process.wait() ; process2.wait()
        process.kill() ; process2.kill()

    except KeyboardInterrupt:
        process.kill() ; process2.kill()
        process.wait() ; process2.wait()
        backToMain()
    except FileNotFoundError:
        subprocess.run("clear")
        print("Error: airodump-ng command not found...")
        print("Install it and retry!!!")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)

# IGNORE
def backToMain(): a = 1


# Remove all Lines that ain't usefull to show
def remove_after_specific_line(fileWithExtension, specific_line):
    try:
        # Read the input CSV file
        df = pd.read_csv(fileWithExtension)
        
        # Find the index of the specific line
        specific_line_index = df[df.apply(lambda row: row.astype(str).str.contains(specific_line, case=False).any(), axis=1)].index[0]
        
        # Keep only rows up to the specific line index
        df = df.iloc[:specific_line_index]
        
        # Save the truncated DataFrame to the output CSV file
        df.to_csv(fileWithExtension, index=False)

    except FileNotFoundError:
        print(f"Error: File '{fileWithExtension}' not found.")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)

# Extract Usefull Columns and overwrite to the file
def extract_specific_columns(fileWithExtension):
    try:
        # Read the input CSV file, specifying only the columns you want to extract
        df = pd.read_csv(fileWithExtension, usecols=[0,3,4,5,6,7,8,9,13])
        
        # Save the selected columns to the output CSV file
        df.to_csv(fileWithExtension, index=False)

    except FileNotFoundError:
        print(f"Error: File '{fileWithExtension}' not found.")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)



def sort_csv_by_column(csv_file):
    # Read the CSV file into a list of rows
    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        rows = list(csv_reader)

    # Sort the rows based on the 7th column (assuming index 6 since Python is 0-indexed) in descending order
    sorted_rows = sorted(rows[1:], key=lambda x: float(x[6]), reverse=True)  # Convert to float instead of int

    # Write the sorted rows back to the CSV file
    with open(csv_file, 'w', newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(rows[0])  # Write the header row
        csv_writer.writerows(sorted_rows)



# Function to replace single space characters in the last column with "Hidden" in the CSV file
def replace_space_with_hidden(fileWithExtension):
    with open(fileWithExtension, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

        # Modify data
        for row in data:
            if len(row) > 0 and row[-1].strip() == "":  # Check if last element has only one space character
                row[-1] = " ~HIDDEN~"

    with open(fileWithExtension, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)



# last column to 1st || 1st column to second
def reorder_columns(input_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Reorder columns for each row
    for row in data:
        row[:] = row[-1:] + row[:-1]  # Move last element to the first place

    with open(input_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def reorder_columns_8_9(input_file):
    # Define the mapping of column indices
    column_mapping = {
        8: 11,  # New position for the 8th column
        9: 12,  # New position for the 9th column
        10: 8,  # New position for the 11th column
        11: 9   # New position for the 12th column
    }

    # Create a temporary file to hold the reordered data
    temp_file = input_file + '.temp'

    with open(input_file, 'r', newline='') as infile, open(temp_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            reordered_row = [None] * (max(column_mapping) + 1)  # Create an empty row with enough slots
            for old_index, new_index in column_mapping.items():
                reordered_row[new_index] = row[old_index]

            writer.writerow(reordered_row)

    # Replace the original file with the temporary file
    shutil.move(temp_file, input_file)


# ADD Serial numbers at first column
def add_line_numbers(input_file):
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    # Add line numbers starting from 1 for each row, excluding the header
    for index, row in enumerate(data[1:], start=1):
        row.insert(0, index)

    # Add header for the new column
    data[0].insert(0, "SN No.")

    with open(input_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)



# overwrite proper csv to csv file
def overwrite_csv_file(filename):
    # Create a temporary file to store the formatted data
    temp_filename = filename + '.temp'

    with open(filename, 'r') as csvfile, open(temp_filename, 'w', newline='') as temp_csvfile:
        csvreader = csv.reader(csvfile)
        csvwriter = csv.writer(temp_csvfile)

        rows = list(csvreader)

        # Find maximum width for each column
        max_widths = [max(len(cell) for cell in col) for col in zip(*rows)]

        # Write each row with proper formatting
        for row in rows:
            formatted_row = [cell.ljust(width) for cell, width in zip(row, max_widths)]
            csvwriter.writerow(formatted_row)

    # Replace the original file with the temporary file
    shutil.move(temp_filename, filename)


    """
    W = '\033[0m'  # white (normal)
    R = '\033[31m'  # red
    G = '\033[32m'  # green
    O = '\033[33m'  # orange
    B = '\033[34m'  # blue
    P = '\033[35m'  # purple
    C = '\033[36m'  # cyan
    GR = '\033[37m' 
    """
    
    # '\033[0m' '\033[31m' '\033[32m' '\033[33m' '\033[34m' '\033[35m' '\033[36m' '\033[37m' 


# Print CSV file in terminal in proper format
def print_csv_file(filename):
    
    colors = [
        '\033[37m',  # White
        '\033[34m',  # Blue
        '\033[32m',  # Green
        '\033[33m',  # Yellow
        '\033[33m',  # Yellow (same as previous)
        '\033[38;5;208m',  # Orange
        '\033[35m',  # Purple
        '\033[35m',  # Purple (same as previous)
        '\033[31m',  # Red
        '\033[31m',  # Red (same as previous)
        '\033[36m',  # Cyan
    ]
    
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)

        # Find maximum width for each column
        max_widths = [max(len(cell) for cell in col) for col in zip(*rows)]

        # Print first row with white color
        first_row = rows[0]
        formatted_first_row = []
        for j, (cell, width) in enumerate(zip(first_row, max_widths)):
            formatted_cell = f'\033[37m{cell.ljust(width)}\033[0m'  # White color
            formatted_first_row.append(formatted_cell)
        print(' | '.join(formatted_first_row))

        print("\n")
        
        # Print the rest of the rows with proper formatting and color
        for i, row in enumerate(rows[1:], start=1):
            formatted_row = []
            for j, (cell, width) in enumerate(zip(row, max_widths)):
                color_index = j % len(colors)
                formatted_cell = f'{colors[color_index]}{cell.ljust(width)}\033[0m'  # Reset color after each cell
                formatted_row.append(formatted_cell)
            print(' | '.join(formatted_row))
            time.sleep(0.02)

        overwrite_csv_file(filename)




def extract_data(filename, line_number):
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        rows = list(csvreader)

        if line_number <= len(rows):
            line = rows[line_number]  # Adjust for 0-based indexing

            # Copy the entire line
            entire_line = line

            # Copy the second and third elements of the line into two different variables
            second_element = line[1]
            third_element = line[2]
            Eleventh_element = line[10]
            sixth_element = line[5]
            eight_element = line[7]
            six_eight = sixth_element.replace(" ", "") + "-" + eight_element.replace(" ", "")
            

            # Convert the fourth element to an integer
            fourth_element = line[3]

            return entire_line, second_element, third_element, fourth_element, six_eight, Eleventh_element
        else:
            print("Line number exceeds the total number of lines in the CSV file.")
            return None, None, None, None, None, None

# Usage
# line_number = int(input("Enter the line number (1-indexed): "))
# entire_line, second_element, third_element, fourth_element = extract_data(filename, line_number)




"""
Convert the text file of wash command after dleting the second line to CSV and then delete the text file
# Merge the 4th and 5th Column of wps wash command result to the airodump csv file to get WPS info 
# of the respective MAC IDs and then delete the wash command csv file
"""
def merge_columns(first_csv_file, second_csv_file, output_csv_file):
    # Read data from the second CSV file and store it in a dictionary
    wps_data = {}
    with open(second_csv_file, 'r') as wps_file:
        reader = csv.reader(wps_file)
        header = next(reader)  # Skip the header
        for row in reader:
            if len(row) >= 5:  # Ensure the row has at least 5 elements
                bssid = row[0]  # Assuming BSSID is in the 1st column
                wps_value = row[3]  # Assuming WPS is in the 4th column
                lock_value = row[4]  # Assuming Lock is in the 5th column
                wps_data[bssid] = (wps_value, lock_value)

    # Merge data from the second CSV file into the first CSV file
    with open(first_csv_file, 'r') as main_file, \
         open(output_csv_file, 'w', newline='') as output_file:
        reader = csv.reader(main_file)
        writer = csv.writer(output_file)
        
        # Write header
        header = next(reader)
        header.extend(['WPS', 'Lock'])  # Add new columns to the header
        writer.writerow(header)

        # Merge columns and write rows
        for row in reader:
            if len(row) >= 3:  # Ensure the row has at least 3 elements
                bssid = row[2]  # Assuming BSSID is in the 3rd column
                if bssid in wps_data:
                    wps_value, lock_value = wps_data[bssid]
                    row.extend([wps_value, lock_value])  # Append WPS and Lock values to the end of the row
                else:
                    row.extend(['', ''])  # Fill empty values if BSSID not found
                writer.writerow(row)

def text_to_csv(input_file, output_file):
    try:
        # Initialize a list to store the data
        data = []
        # Open the input file and read its contents
        with open(input_file, 'r') as file:
            # Read the lines
            lines = file.readlines()
            # Skip the first line (header)
            data.append(lines[0].strip().split())
            # Read the remaining lines, excluding the second line
            for line in lines[2:]:
                # Split the line based on spaces or tabs
                columns = line.strip().split()
                # Append the columns to the data list
                data.append(columns)

        # Write the data to the CSV file
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            # Write the header
            writer.writerow(data[0])
            # Write the data
            for row in data[1:]:
                writer.writerow(row)
    except Exception as e:
        print(f"\n\n\n\nERROR - While Converting Wash Command Result to CSV: \n{e}")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)


def MergeLockedWPS_Column(input_file):
    output_file = input_file + '_modified.csv'

    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for i, row in enumerate(reader):
            # Rename the 4th column to "Auth"
            if i == 0:  # Assuming the first row contains column headers
                row[7] = "Auth"

            # Check if the value in the 12th column is "Yes"
            if row[11] == "Yes":
                # Remove the corresponding value in the 11th column and replace it with "Locked"
                row[10] = "Locked"

            # If the value in the 11th column is empty, replace it with "No"
            if not row[10]:
                row[10] = "---"

            # Remove the 12th column
            del row[11]

            # Write the modified row to the output CSV file
            writer.writerow(row)
            
    # Rename the output file to the input file
    os.rename(output_file, input_file)




def MonitorModeDisbaled_RedirectProgramA(monitorModeFile):
    check = is_monitor_mode_enabled(interface)
    if check == False:
        clear() ; print(f"MONITOR MODE IS DISBALED ON '{interface}'\n.\n.\n.\n")
        loading_animation("Wait... Turning On Monitor Mode") ; Del_Current_Line() ; clear()

        subprocess.run(['sudo', 'python', monitorModeFile])
        sys.exit()


# def runCaptureFile(interface, BSSID, CHANNEL, path):
#     time.sleep(0.5) ; print(".") ; time.sleep(0.5) ; print(".") ; time.sleep(0.5) ; print(".") 
    
#     loading_animation("Please wait, Starting Handshake Capture... ")
#     Del_Current_Line() ; clear()

#     # python -u "scriptName.py" 'interface-name' 'BSSID' 'CHANNEL'
#     captureFile = path + "utils/C_captureHandshake.py"
#     # print(['sudo', 'python', captureFile, interface, BSSID, CHANNEL, path]) ; input()

#     global proc
#     proc = subprocess.Popen(['sudo', 'python', captureFile, interface, BSSID, CHANNEL], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     sys.exit()






#######################################################################################################
#
#######################################################################################################
# MAIN FUNCTION
# Get path exact name where the script is stored
# print(interface)
# input()

try:
    # Files will be saved to the location where the python script is stored 
    
    requirements() ; print(G)
    
    # path = os.path.abspath(os.path.dirname(__file__)) + "/"
    wpsfile = path + "wps_info_BS.txt"
    wpsfileCSV = path + "wps_info_BS.csv"
    CSVfilePath = path + "airodumped_BS_list"
    fileWithExtension = CSVfilePath+"-01.csv"
    tempFilecSV = path + "New_BS_01.csv"
    # print(path) ; input()
    
    MonitorModeDisbaled_RedirectProgramA(path + "A_monitorMode.py")

    # Remove the file if it exist already
    try: os.remove(fileWithExtension)
    except: pass
    try: os.remove(wpsfile)
    except: pass
    try: os.remove(tempFilecSV)
    except: pass
    try: os.remove(CSVfilePath)
    except: pass
    try: os.remove(wpsfileCSV)
    except: pass
    subprocess.run("clear")


    # Get Interface Name that is in Monitor Mode
    # interface = selected_interface

    # Run airodump command
    run_airodump(interface, CSVfilePath, wpsfile) ; clear() ; print(G) ; loading_animation("Fetching Data... ") ; print(GR)
    
    # Remove all Lines that ain't usefull to show
    specific_line = 'Station MAC'  # The specific line after which you want to remove content
    remove_after_specific_line(fileWithExtension, specific_line)

    #---------------------------------------------------------
    
    # Extract Usefull Columns and overwrite to the file
    extract_specific_columns(fileWithExtension)
    # Sort in Descending order according to the power
    sort_csv_by_column(fileWithExtension)
    
    # Replace empty ESSID names with "Hidden"
    replace_space_with_hidden(fileWithExtension)
    
    # Reorder columns
    reorder_columns(fileWithExtension)
    
    # Serial numbers
    add_line_numbers(fileWithExtension)
    
    # Convert WPS Wash command Text to CSV
    text_to_csv(wpsfile, wpsfileCSV)
    
    # Merge Wash command 4th and 5th column to Main CSV File
    merge_columns(fileWithExtension, wpsfileCSV, tempFilecSV)
    
    
    # Replace 11th and 12th column with 8th and 9th
    # Remove Locked Column of csv and merge it with WPS Column
    MergeLockedWPS_Column(tempFilecSV)
    
    
    # Delete all Old file and Rename the Output to same old one...
    try:
        os.remove(wpsfileCSV)
        os.remove(wpsfile)
        os.remove(fileWithExtension)
    except Exception as e:
        print(f"\n\n\n\nERROR: While Removing Worked Files: \n{e}")
        time.sleep(0.2) ; ReportError() ; sys.exit(1)
    
    os.rename(tempFilecSV, fileWithExtension)
    # subprocess.run(["mv", tempFilecSV, "-T", fileWithExtension, "-f"])
    
    #---------------------------------------------------------
    subprocess.run("clear") ; bann_text()
    print(W+ "-"*124 + G)
    print_csv_file(fileWithExtension)


    with open(fileWithExtension, 'r') as file:
        line_count = sum(1 for line in file)
        line_count = line_count - 1
    
    line_number = 99999 ; i = 1
    while line_number>line_count:
        if i == 2:
            loading_animation("ERROR! Invalid Option...") ; Del_Current_Line()
        try:
            line_number = int(input("\n\n[+] Which ESSID to Hit : "))
            Del_Pre_Line() ; Del_Pre_Line() ; i = 2
        except ValueError:
            Del_Pre_Line() ; Del_Pre_Line() ; i = 1
            loading_animation("Invalid input. Please enter a number.") ; Del_Current_Line()
        except KeyboardInterrupt:
            Del_Current_Line() ; loading_animation("\tPlease wait, Fetching all Info... ") ; Del_Current_Line() ; print("\n\n")
                    
            print(O + f"\n\t~DETAILED INFO~\n" + G)                         ; time.sleep(0.4)
            text = P + f"  [x] Airodump-ng Targets Dump ({res})    : ", W + "\""+CSVfilePath+"-01.csv\"" + G           ; SlowType(text)
            text = P + f"  [x] Interface                         : ", W + interface + G          ; SlowType(text)
            ReportError() ; sys.exit(0)

    entire_line, SelectedESSID, SelectedBSSID, SelectedChannel, Security, WPSinfo = extract_data(fileWithExtension, line_number)

    clear()
    # REMOVE SPACES FROM VARIABLES
    SelectedBSSID = "".join(SelectedBSSID.split())
    SelectedChannel = "".join(SelectedChannel.split())
    
    bann_text()
    print(R + f"\n\t~[[ SELECTED TARGET ]]~\n" + G)                       ; time.sleep(0.4)
    text = C + f"  [+] ESSID    :", B + SelectedESSID + G           ; SlowType(text)
    text = C + f"  [+] BSSID    : ", G + SelectedBSSID + G          ; SlowType(text)
    text = C + f"  [+] CHANNEL  : ", O + str(SelectedChannel) + G   ; SlowType(text)
    text = C + f"  [+] SECURITY : ", P + Security + G               ; SlowType(text)
    text = C + f"  [+] WPS INFO : ", C + WPSinfo + G                ; SlowType(text)
    

    ############################# WORKING CURRENTLY
    # res = input("\nEnter to Start De-Authentication attack and Capture Handshake...\nor 'X' to Disable Monitor Mode! ")
    text = G+ "\n\n     \t\t\t", "-"*30 ; SlowType(text)
    text = "\t\t\t      --Select a Response--\n", "    \t\t\t", "-"*30 ; SlowType(text)
    time.sleep(0.1)
    print("\n  [x] " + P + "Capture Handshake & Start De-auth Attack (All Connected Seperately)     " + O + "  | -> Press ENTER" + G)
    time.sleep(0.1)
    print("  [x] " + P + "Capture Handshake & Start De-auth Attack (All Connected Clients at Once)  " + O + "| -> Press '2'" + G)
    time.sleep(0.1)
    print("  [x] " + P + "Manual Mode || Close and print All Details" + O + "                                | -> Press '3'" + G)
    time.sleep(0.1)
    print("  [x] " + P + "Disable Monitor Mode" + O + "                                                      | -> Press '4'" + G)
    time.sleep(0.1)
    print("  [x] " + P + "Exit Program" + O + "                                                              | -> Press '5'" + G)
    time.sleep(0.1)
    SlowType("\n  -----------> ") ; Del_Pre_Line()
    response = input("  -----------> ")
    
    
    print("\n\n") ; time.sleep(0.4)
    
    if response == '\n' or response == '' or response == '1':
        loading_animation("\tPlease wait, Starting Handshake Capture... ")
        Del_Current_Line() ; clear()

        # python -u "scriptName.py" 'interface-name' 'BSSID' 'CHANNEL'
        captureFile = path + "utils/C_captureHandshake.py"
        SlowType(P+ "Starting the ...\n" +GR) ; time.sleep(0.5) ; subprocess.run(["figlet" , "     DEMON"])
        
        mode = '1'
        subprocess.run(['sudo', 'python', captureFile, interface, SelectedBSSID, SelectedChannel, path, mode])
        sys.exit(0)
        
    elif response == '2':
        loading_animation("\tPlease wait, Starting Handshake Capture... ")
        Del_Current_Line() ; clear()

        # python -u "scriptName.py" 'interface-name' 'BSSID' 'CHANNEL'
        captureFile = path + "utils/C_captureHandshake.py"
        SlowType(P+ "Starting the ...\n" +GR) ; time.sleep(0.5) ; subprocess.run(["figlet" , "     DEMON"])
        
        mode = 2
        subprocess.run(['sudo', 'python', captureFile, interface, SelectedBSSID, SelectedChannel, path, mode])
        sys.exit(0)
        
    elif response == '3':
        loading_animation("\tPlease wait, Fetching all Info... ") ; Del_Current_Line() ; clear_lines(15)
        
        print(O + f"\n\t~DETAILED INFO~\n" + G)                         ; time.sleep(0.4)
        text = P + f"  [x] Airodump-ng Targets Dump ({res})    : ", W + "\""+CSVfilePath+"-01.csv\"" + G           ; SlowType(text)
        text = P + f"  [x] Interface                         : ", W + interface + G          ; SlowType(text)
        exit_pause()
    
    elif response == '4':
        loading_animation(f"\tPlease wait, Disabling Monitor Mode on {interface}... ") ; Del_Current_Line() ; clear_lines(15)
        
        abrakadabra = change_interface_name(interface, "wlan")
        if abrakadabra != "none": interface = abrakadabra
        clear() ; bann_text()
        
        print(O+ f"[[ Selected interface: \"{interface}\" ]]\n.\n.\n" + GR)
        disable_monitor_mode(interface)
        interface = interface[:-3]
        exit_pause()
        
    else:
        time.sleep(0.2) ; ReportError() ; sys.exit(0)


    time.sleep(0.2) ; ReportError() ; sys.exit(0)
except KeyboardInterrupt:
    time.sleep(0.2) ; ReportError() ; sys.exit(1)

except Exception as e:
    print(f"\n\n\n\nERROR 1: {e}")
    time.sleep(0.2) ; ReportError() ; sys.exit(1)
