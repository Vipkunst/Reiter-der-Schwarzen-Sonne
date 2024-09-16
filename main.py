import sektionen
import os

# Print all sections
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def iterate_all_sections():
    sek_read = 1
    total_sections = len(sektionen.erster_prototyp_pfad)
    for sek in sektionen.erster_prototyp_pfad:
        clear_console()
        progress = sek_read / total_sections * 100
        print(f"Progress: {progress:.2f}%")
        print(sek)
        sek_read += 1
        input("Enter to continue")


iterate_all_sections()

