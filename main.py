import platform
import os


# Yksinkertainen fetch jolla saada terminaaliin näkyviin koneen speksit sekä muuta tietoa.
# OS, Host, Kernelin versio, Uptime, CPUn tiedot ja tila(?), muistin määrä ja käyttöaste,
# kiintolevyn / kiintolevyjen koko

# Lisänä ASCII-art ja muotoilu?

# Arkkitehtuuri
print("Architecture: " + platform.architecture()[0])

print("Computer name:",platform.node())

dist = platform.uname()
dist = " ".join(x for x in dist)
print("Kernel version:",dist.split(" ")[2])


#Ytimien määrä
print("Number of CPU cores:", os.cpu_count())



