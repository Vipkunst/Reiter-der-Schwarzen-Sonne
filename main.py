import sektionen
import os
import platform

sek_read = 1
total_sections = len(sektionen.hauptpfad)

system = platform.platform()

if "Windows" in system:
    os.system('cls')
else:
    os.system('clear')

for sek in sektionen.hauptpfad:
    progress = sek_read / total_sections * 100
    print(f"Progress: {progress:.2f}%")
    print(sek)
    sek_read += 1
    input()

    if "Windows" in system:
        os.system('cls')
    else:
        os.system('clear')