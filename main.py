#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: my-ip (https://github.com/KafetzisThomas/my-ip)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

# Import built in modules
import sys, socket, time
from requests import get
from datetime import datetime
# Get current time in a 24Hour format
CURRENT_TIME = datetime.now().strftime("%H:%M:%S")

# Import other modules
import colorama
from colorama import Fore as F
colorama.init(autoreset=True)

print("\nIt's searching data according your network. This may take a few seconds...")
input(f"\nPress {F.GREEN}Enter{F.RESET} to Continue/{F.RED}Ctrl+C{F.RESET} to Stop")

try:
  while True:
    time.sleep(1)
    print("-" * 42)

    HOSTNAME = socket.gethostname()  # Fetch computer name
    LOCAL_IP = socket.gethostbyname(HOSTNAME)  # Fetch computer ip address
    PUBLIC_IP = get('https://api.ipify.org').text  # Fetch public ip address

    #~~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~~~~~#
    print(f"Current Time:        {F.GREEN}{CURRENT_TIME}")
    print(f"Computer Name:       {F.GREEN}{HOSTNAME}")
    print(f"Computer IP Address: {F.GREEN}{LOCAL_IP}")
    print(f"Public IP Address:   {F.RED}{PUBLIC_IP}")
except KeyboardInterrupt:
  print(f"{F.RED}Operation canceled.")
  sys.exit()
