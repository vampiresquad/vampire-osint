#!/usr/bin/env python3

import os
import sys
import time
import platform

# Colors
R = '\033[1;31m'  # Red
G = '\033[1;32m'  # Green
Y = '\033[1;33m'  # Yellow
B = '\033[1;34m'  # Blue
C = '\033[1;36m'  # Cyan
W = '\033[0m'     # Reset

# Slow print function
def slow_type(text, delay=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear terminal
os.system('clear' if platform.system() != 'Windows' else 'cls')

# Banner
def show_banner():
    banner = f"""
{R}███████╗ █████╗ ███╗   ███╗██████╗ ██╗██████╗ ███████╗
{R}██╔════╝██╔══██╗████╗ ████║██╔══██╗██║██╔══██╗██╔════╝
{R}███████╗███████║██╔████╔██║██████╔╝██║██║  ██║█████╗  
{R}╚════██║██╔══██║██║╚██╔╝██║██╔═══╝ ██║██║  ██║██╔══╝  
{R}███████║██║  ██║██║ ╚═╝ ██║██║     ██║██████╔╝███████╗
{W}-------------------------------------------------------
{G}    Vampire-OSINT Tool | Powered by Vampire Squad
{G}    Author : Muhammad Shourov (VAMPIRE)
{G}    GitHub : https://github.com/vampiresquad
{G}    Facebook: https://facebook.com/Junior.Writer.SHourov
{W}-------------------------------------------------------
"""
    print(banner)

# Disclaimer
def show_disclaimer():
    disclaimer = f"""{Y}
[!] DISCLAIMER:
This tool is created for Educational, Legal, and Ethical OSINT Research only.
Unauthorized tracking, hacking, or identity investigation is strictly prohibited.
By using this tool, you agree that the author holds no responsibility
for any misuse or illegal activity done by users.

Use wisely. Be ethical. Be Vampire.
{W}"""
    slow_type(disclaimer, 0.02)

# Run intro
show_banner()
show_disclaimer()

# Continue to main menu (placeholder)
print(f"\n{C}[~]{W} Loading modules...\n")
time.sleep(1)
# (Tools menu or main function starts from here)
