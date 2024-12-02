import individual
import content
import textwrap
import os
import random
import Classes.Player as Player
import Classes.Gegner as Gegner

def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def show_default_section():

    player = Player.Player()
    
    currentSek = "abs1"
    path = content.zweiter_prototyp_pfad

    while(currentSek != "end"):
        show_section(path, currentSek)

        section = path[currentSek]

        if ("text_options" not in section):
            input("Press Enter to continue...")

        if ("text_options" in section):
            for key, value in section['text_options'].items():
                print(f"{key}: {value}")

            user_input = get_user_input()

            if (user_input == "würfeln"):
                gegner = Gegner("GARTAK, GEFÄNGNISWÄRTER", 2, 11, 10)
                kampf(player, gegner)
            
            currentSek = section["options"][user_input]
            input("Press Enter to continue...")
        else:
            currentSek = section['options']['1']


def kampf(player, gegner):


def wuerfeln (min, max):
    return random.randint(min, max)

def show_stats(player):
    print(f"HP: {player.HP}" + "\n"
          +f"")

def show_section(path, section_key):
    section = path[section_key]
    wrapped_section = textwrap.fill(section['content'], width=100)
    print(f"\n{wrapped_section}")
    return

def get_user_input():
    return input("Wähle deine nächsten Schritte: ")


def init_game():
    current_section = 'abs1'
    while True:
        options = show_section(individual.chapter, current_section)
        user_input = get_user_input()

        if user_input in options:
            current_section = options[user_input]
        else:
            print("Invalid section number. Please enter a valid section number.")

def choose_paths():
    user_choice_path = input("Wähle deinen Pfad: \n1.Individueller Pfad\n2.Standard Pfad\nAuswahl: ")
    if user_choice_path == "1":
        init_game()
    elif user_choice_path == "2":
        show_default_section()
    else:
        print("Invalid input. Please enter a valid input.")
        choose_paths()

def main():
    print("\n")
    choose_paths()


if __name__ == "__main__":
   main()
