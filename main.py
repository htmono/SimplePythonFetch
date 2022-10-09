import platform
import os
import psutil
import time
import shutil



# Yksinkertainen fetch jolla saada terminaaliin näkyviin koneen speksit sekä muuta tietoa.
# OS, Host, Kernelin versio, Uptime, CPUn tiedot ja tila(?), muistin määrä ja käyttöaste,
# kiintolevyn / kiintolevyjen koko

# Lisänä ASCII-art ja muotoilu?



uname = platform.uname()
print(f"System: {uname.system} {platform.architecture()[0]} {uname.version.split()[0]}")
print(f"Hostname: {uname.node}")
print(f"Kernel Release: {uname.release}")
print(f"Machine: {uname.machine}") # Placeholder
print(f"Processor: {uname.processor}","with",os.cpu_count(),"cores") # Placeholder
print(f"Uptime: {round((time.time() - psutil.boot_time())) // 60}min")
print(f"Memory: {round(psutil.virtual_memory().total / 1024 **2)} MiB")
