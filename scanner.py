#!/bin/python
#Produced by abra on behalf of Plexus Network Academy
#Usage: python3 scanner.py <ip>

import sys, socket, timeit, colorama
from colorama import Fore, Back, Style
from datetime import datetime

#Initialize colorama
colorama.init(autoreset=True)

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else: 
	print(Fore.RED + "Invalid amount of arguments.")
	print(Fore.YELLOW + "Syntax : python3 scanner.py <ip>")
	sys.exit()
#Add a pretty banner
start = timeit.default_timer()
print("-" * 50)
print(Fore.YELLOW + "Scanning taget: "+target)
print(Fore.YELLOW + "Time started: "+str(datetime.now()))
print("-" * 50)
found = 0

try: 
	for port in range(1,65535):
		sys.stdout.write("Trying port: " + str(port) + "\r")
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print(Fore.BLUE + "Port {} is open".format(port))
			found += 1

		s.close

except KeyboardInterrupt:
	stop = timeit.default_timer()
	print(Fore.GREEN + "\nFound {} ports on scanned {} ports at {} second.".format(found,port,stop - start))
	print("\n[" + Fore.RED + "!" + Fore.WHITE + "]" +  "Exiting program.")
	sys.exit()
except socket.gierror:
	print(Fore.RED + "Hostname could not be resolved")
	sys.exit()
except socket.error:
	print(Fore.RED + "Couldn't connect to server.")
	sys.exit()

