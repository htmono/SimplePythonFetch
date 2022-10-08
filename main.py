import platform
import os


# Yksinkertainen fetch jolla saada terminaaliin näkyviin koneen speksit sekä muuta tietoa.
# OS, Host, Kernelin versio, Uptime, CPUn tiedot ja tila(?), muistin määrä ja käyttöaste,
# kiintolevyn / kiintolevyjen koko

# Lisänä ASCII-art ja muotoilu?


uname = platform.uname()
print("System:",uname.system,platform.architecture()[0])
print(f"Hostname: {uname.node}")
print(f"Kernel Release: {uname.release}")
print(f"Version: {uname.version.split()[0]}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}","with",os.cpu_count(),"cores")


