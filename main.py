import sektionen
import os
import textwrap
# Print all sections
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Iterate over all sections
def iterate_all_sections():
    sek_read = 0
    total_sections = len(sektionen.erster_prototyp_pfad)
    for sek in sektionen.erster_prototyp_pfad:
        wrapped_text = textwrap.fill(sek, width=100)
        clear_console()
        progress = sek_read / total_sections * 100
        print(wrapped_text)
        print(f"Progress: {progress:.2f}%")
        sek_read += 1
        input("Enter to continue")


iterate_all_sections()


