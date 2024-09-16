import sektionen
import os
import time

end = False
sek_gelesen = 0
total_sections = len(sektionen.hauptpfad)

for sek in sektionen.hauptpfad:
    fortschritt = sek_gelesen / total_sections * 100
    print(f"Progress: {fortschritt:.2f}%")
    print(sek)
    sek_gelesen += 1
    input()