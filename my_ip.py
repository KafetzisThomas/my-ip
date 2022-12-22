#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: my-ip (https://github.com/KafetzisThomas/my-ip)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

import sys, socket, time, colorama
from requests import get
from datetime import datetime
from colorama import Fore as F
colorama.init(autoreset=True)

try:
    # Get current time in a 24Hour format
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    
    input(f"\nPress {F.GREEN}Enter{F.RESET} to Continue/{F.RED}Ctrl+C{F.RESET} to Stop")
    while True:
        time.sleep(1)
        print("-" * 42)
        hostname = socket.gethostname()
        LocalIp = socket.gethostbyname(hostname)
        PublicIp = get('https://api.ipify.org').text
  
        print(f"Current Time: {F.GREEN}{currentTime}")
        print(f"Your Computer Name is: {F.GREEN}{hostname}")
        print(f"Your Computer IP Address is: {F.GREEN}{LocalIp}")
        print(f"Your Public IP Address is: {F.RED}{PublicIp}")

except KeyboardInterrupt:
    print(f"{F.RED}Operation canceled.")
    sys.exit()
