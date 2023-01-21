# Yksinkertainen fetch jolla saada terminaaliin näkyviin koneen speksit sekä muuta tietoa.
# OS, Host, Kernelin versio, Uptime, CPUn tiedot ja tila(?), muistin määrä ja käyttöaste,
# kiintolevyn / kiintolevyjen koko. 
# WIP

import platform
import os
import psutil
import time
import shutil
import pwd


# ASCII-art
print("  ___ ___ __  __ ___ _    ___   ___ ___ _____ ___ _  _ ")
print(" / __|_ _|  \/  | _ \ |  | __| | __| __|_   _/ __| || |")
print(" \__ \| || |\/| |  _/ |__| _|  | _|| _|  | || (__| __ |")
print(" |___/___|_|  |_|_| |____|___| |_| |___| |_| \___|_||_|")
print("-------------------------------------------------------")

uname = platform.uname()
# OS Info

# current logged in user
def getUser():
    user = pwd.getpwuid(os.getuid())[0]
    return f"Username:      {user} "

# operating system info
def getSystem():
    arch = platform.architecture()[0]
    system = uname.system
    os = uname.version.split()[0] # This is placeholder, doesn't work as intended
    return f"System:        {arch} {system} {os}"

# hostname
def getHost():
    hostname = uname.node
    return f"Hostname:      {hostname}"

# Kernel version
def getKernel():
    kernel = uname.release
    return f"Kernel:        {kernel}"

# machine architecture // Commented out, this is redundant
# def getArch():
#    machine = uname.machine
#    return f"Machine: {machine}"

# processor info
def getProc():
	with open('/proc/cpuinfo', 'r') as f:
		for line in f:
			if 'model name' in line:
				cpuname = line.split(':')[1].strip()
				cpuname = cpuname.replace('  ', '')
				break
	return f"Processor:     {cpuname}"

# system memory
def getMemory():
    totalmem = round(psutil.virtual_memory().total / 1024 **2)
    usedmem = round(psutil.virtual_memory().total / 1024 **2) - round(psutil.virtual_memory().available / 1024 **2) # available memory subtracted from total memory
    return f"Memory:        {usedmem}MiB used / {totalmem}MiB total"

# system uptime
def getUptime(): # TO DO: This should show hours and minutes
    uptime = round((time.time() - psutil.boot_time())) // 60
    return f"Uptime:        {uptime} minutes"

# Returning the info for the user
print(getUser())
print(getSystem())
print(getHost())
print(getKernel())
# print(getArch())
print(getProc())
print(getMemory())
print(getUptime())