#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# Project Title: my-ip (https://github.com/KafetzisThomas/my-ip)
# Author / Project Owner: KafetzisThomas (https://github.com/KafetzisThomas)

# Import built in modules
import sys, socket, time, speedtest
from requests import get
from datetime import datetime
# Import other modules
import colorama
from colorama import Fore as F
colorama.init(autoreset=True)

print("\nIt's searching data according your network. This may take a few seconds...")

try:
    # Get current time in a 24Hour format
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%H:%M:%S")
    
    st = speedtest.Speedtest()
    
    # Fetch download & upload speed
    download = st.download()
    upload = st.upload()

    # Fetch ping
    st.get_servers()
    ping = st.results.ping
    
    input(f"\nPress {F.GREEN}Enter{F.RESET} to Continue/{F.RED}Ctrl+C{F.RESET} to Stop")
    while True:
        time.sleep(1)
        print("-" * 42)
        
        # Fetch computer name
        hostname = socket.gethostname()
        # Fetch computer ip address
        LocalIp = socket.gethostbyname(hostname)
        # Fetch public ip address
        PublicIp = get('https://api.ipify.org').text
  
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ OUTPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        print(f"Current Time:        {F.GREEN}{currentTime}")
        print(f"Computer Name:       {F.GREEN}{hostname}")
        print(f"Computer IP Address: {F.GREEN}{LocalIp}")
        print(f"Public IP Address:   {F.RED}{PublicIp}")
        print(f"Download Speed:      {F.GREEN}{'%.2f' % (download / 1_000_000)} Mbps")
        print(f"Upload Speed:        {F.GREEN}{'%.2f' % (upload / 1_000_000)} Mbps")
        print(f"Ping:                {F.GREEN}{ping}")

except KeyboardInterrupt:
    print(f"{F.RED}Operation canceled.")
    sys.exit()
