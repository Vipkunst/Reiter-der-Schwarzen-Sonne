import sektionen

# Print all sections
sek_read = 1
total_sections = len(sektionen.hauptpfad)

for sek in sektionen.hauptpfad:
    progress = sek_read / total_sections * 100
    print(f"Progress: {progress:.2f}%")
    print(sek)
    sek_read += 1
    input()

