import sektionen
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
sek_read = 1
total_sections = len(sektionen.hauptpfad)

for sek in sektionen.hauptpfad:
    clear_console()
    progress = sek_read / total_sections * 100
    print(f"Progress: {progress:.2f}%")
    print(sek)
    sek_read += 1
    input()