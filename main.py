import sektionen

sek_read = 1
total_sections = len(sektionen.hauptpfad)

for sek in sektionen.hauptpfad:
    fortschritt = sek_read / total_sections * 100
    print(f"Progress: {fortschritt:.2f}%")
    print(sek)
    sek_read += 1
    input()