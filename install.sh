#!/bin/bash

# Colors
RED='\033[1;31m'
GRN='\033[1;32m'
YEL='\033[1;33m'
CYN='\033[1;36m'
NC='\033[0m' # No Color

clear
echo -e "${GRN}"
echo "=========================================="
echo "      Vampire-OSINT Installer Started"
echo "=========================================="
echo -e "${NC}"
sleep 1

# Fix pip issues in Termux
fix_termux_pip() {
    echo -e "${YEL}[~] Checking pip in Termux...${NC}"
    if ! command -v pip >/dev/null 2>&1; then
        echo -e "${RED}[!] pip not found. Fixing...${NC}"
        curl -sS https://bootstrap.pypa.io/get-pip.py | python
    fi
}

# Detect Platform
if [[ "$OSTYPE" == "linux-android"* ]]; then
    echo -e "${CYN}[+] Detected Termux environment${NC}"
    pkg update -y && pkg upgrade -y
    pkg install python git curl wget -y
    fix_termux_pip
else
    echo -e "${CYN}[+] Detected Linux environment${NC}"
    sudo apt update && sudo apt upgrade -y
    sudo apt install python3 python3-pip git curl wget -y
fi

# Install Python requirements
echo -e "${GRN}[+] Installing Python modules...${NC}"
pip install --upgrade pip
pip install -r requirements.txt || pip3 install -r requirements.txt

# Create output folder
mkdir -p output

# Success message
echo -e "${GRN}[✓] Setup Completed Successfully!${NC}"
echo -e "${YEL}------------------------------------------${NC}"
echo -e "${CYN}>> Run the tool: ${GRN}python3 vampire-osint.py${NC}"
echo -e "${YEL}------------------------------------------${NC}"
