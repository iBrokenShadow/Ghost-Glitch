#!/bin/bash

print_banner() {
    clear
    echo -e "\e[32m"
    echo -e "░██████╗░██╗░░██╗░█████╗░░██████╗████████╗░░░░░░░██████╗░██╗░░░░░██╗████████╗░█████╗░██╗░░██╗"
    echo -e "██╔════╝░██║░░██║██╔══██╗██╔════╝╚══██╔══╝░░░░░░██╔════╝░██║░░░░░██║╚══██╔══╝██╔══██╗██║░░██║"
    echo -e "██║░░██╗░███████║██║░░██║╚█████╗░░░░██║░░░█████╗██║░░██╗░██║░░░░░██║░░░██║░░░██║░░╚═╝███████║"
    echo -e "██║░░╚██╗██╔══██║██║░░██║░╚═══██╗░░░██║░░░╚════╝██║░░╚██╗██║░░░░░██║░░░██║░░░██║░░██╗██╔══██║"
    echo -e "╚██████╔╝██║░░██║╚█████╔╝██████╔╝░░░██║░░░░░░░░░╚██████╔╝███████╗██║░░░██║░░░╚█████╔╝██║░░██║"
    echo -e "░╚═════╝░╚═╝░░╚═╝░╚════╝░╚═════╝░░░░╚═╝░░░░░░░░░░╚═════╝░╚══════╝╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝\n.\n.\n."
    echo -e "\e[0m"  # Reset color
}


footer_banner() {
    echo -e "\e[35m"
    echo -e "\t-------------------------------------------------------------"
    echo -e "\tREPORT ANY ERROR FOR FIXES (Thanks for your Contribution)\n"
    echo -e "\tGiven Contacts : Telegram  : https://t.me/iBrokenShadow"
    echo -e "\t               : Instagram : https://www.instagram.com/iBrokenShadow/"
    echo -e "\t               : Github    : https://github.com/iBrokenShadow\n"
    echo -e "\tThanks! visit https://ibrokenshadow.com"
    echo -e "\t-------------------------------------------------------------"
    echo -e "\e[0m"  # Reset color
    echo -e "\nPress any key to close!"
    read
}


if [ "$EUID" -eq 0 ]; then
    echo ""
else
    print_banner
    echo -e "\e[91m\n\n--------------------------------------------------------------"
    echo -e "\e[91mERROR:\n\nPlease Run the script using SUDO Privileges"
    echo -e "--------------------------------------------------------------"
    echo -e "\e[0m"  # Reset color
    footer_banner
    exit 1
fi



check_files_existence() {
    # Get the directory where the script is located
    script_dir=$(dirname "$0")

    local files=(
        "$script_dir/ghost_glitch.sh"
        "$script_dir/ghost_glitch.py"
        "$script_dir/README.md"
        "$script_dir/requirements.txt"
        "$script_dir/utils/B_handleDumpAirodump-ng.py"
        "$script_dir/utils/C_captureHandshake.py"
        "$script_dir/utils/X_requirement.py"
    )
    local missing_files=()

    # Iterate over each file
    for file in "${files[@]}"; do
        # Check if the file exists
        if [ ! -f "$file" ]; then
            missing_files+=("$file")
        fi
    done

    # Check if there are missing files
    if [ ${#missing_files[@]} -gt 0 ]; then
        print_banner
        echo -e "\e[91m\n\n--------------------------------------------------------------"
        echo -e "\e[91mERROR: The following files are missing:\n"
        for missing_file in "${missing_files[@]}"; do
            echo "$missing_file"
        done
        echo -e "--------------------------------------------------------------"
        echo -e "\e[32m"
        echo -e "Download All Files Now from given Repo:\nhttps://github.com/iBrokenShadow/Ghost-Glitch"
        echo -e "\n"
        echo -e "\e[0m"  # Reset color
        footer_banner
        exit 1
    fi
}

check_files_existence



# Get the directory where the script is located
script_dir=$(dirname "$0")
# Append "/ghost_glitch.py" to the directory path
script_path="$script_dir/ghost_glitch.py"

# Check if lsb_release command is available
if ! command -v lsb_release &> /dev/null; then
    print_banner
    echo -e "\e[91m\n\nERROR:\n\nlsb_release command not found. This script requires lsb_release to run."
    echo -e "\e[0m"  # Reset color
    footer_banner
    exit 1
fi

# Check the distribution ID
distribution=$(lsb_release -si)

# Define the list of Debian-based distributions
debian_based=("Debian" "Kali" "Ubuntu" "Parrot")

# Check if the distribution is Debian-based
if [[ ! " ${debian_based[@]} " =~ " ${distribution} " ]]; then
    print_banner
    echo -e "\e[91m\n\nERROR:\n\nThis script is intended to run on (Debian - Ubuntu - KaliLinux - ParrotOS) systems only."
    echo -e "We'll soon release it on Other Distros"
    echo -e "\e[0m"  # Reset color
    footer_banner
    exit 1
fi

# make a bash function for linux so, it checks for 5 or 6 specified files if they exist or not, if they dont exist then end the program, if they do exist then continue

# Define required packages
required_packages=("figlet" "mdk4" "aircrack-ng" "python3" "lsb-release")

# Initialize variable to store missing packages
missing_packages=()

# Check if required packages are installed
for package in "${required_packages[@]}"; do
    if ! dpkg -s "$package" &> /dev/null; then
        missing_packages+=("$package")
    fi
done

# If there are missing packages, display error with missing packages highlighted
if [ ${#missing_packages[@]} -gt 0 ]; then
    print_banner
    echo -e "\e[91m\n\n--------------------------------------------------------------"
    echo -e "\e[91mError: Some required packages are not installed:\n"
    for package in "${missing_packages[@]}"; do
        echo -e " - $package"
    done
    echo -e "--------------------------------------------------------------"
    echo -e "\n"
    echo -e "\e[0m"  # Reset color
    footer_banner
    exit 1
fi

# Run the Python file
clear
sudo python3 "$script_path"

