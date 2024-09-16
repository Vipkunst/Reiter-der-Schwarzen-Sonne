import sektionen
import os

storyArray = [1, 72, 76, 55, 92, 35, 40, 71, 90, 65, 11, 60, 16, 89, 58, 33, 13, 38, 100]


# Print all sections
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def iterate_all_sections():
    sek_read = 1
    total_sections = len(sektionen.erster_prototyp_pfad)
    for sek in sektionen.hauptpfad:
        clear_console()
        progress = sek_read / total_sections * 100
        print(f"Progress: {progress:.2f}%")
        print(sek)
        sek_read += 1
        input("Enter to continue")


iterate_all_sections()

