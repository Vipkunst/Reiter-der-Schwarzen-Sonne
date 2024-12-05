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
    content.player = player
    
    currentSek = "abs1"
    path = content.zweiter_prototyp_pfad

    while(currentSek != "end"):
        show_section(path, currentSek)

        section = path[currentSek]

        if ("event" in section):
            section["event"]["1"]()

        if ("text_options" not in section):
            input("Press Enter to continue...")

        if ("text_options" in section):
            for key, value in section['text_options'].items():
                print(f"{key}: {value}")

            user_input = ""
            while (user_input not in section["text_options"]):
                user_input = get_user_input()
            
            currentSek = section["options"][user_input]
            input("Press Enter to continue...")
        else:
            currentSek = section['options']['1']

        if ("kampfSek" in section and section["kampfSek"] == True):
            kampf(player, section["gegner"])


def kampf(player, gegner):

    print("\n")
    print(f"Gegner: {gegner.name}")
    print(f"Resistenz: {gegner.resistenz}")
    print(f"Angriff: {gegner.angriff}")
    print(f"Verteidigung: {gegner.verteidigung}")

    while(not gegner.tot or not player.tot):
        input("Enter zum Angreifen...")
        wurf = wuerfeln(0, 6)
        basiswuerfel = wuerfeln(0, 6)

        if (test(player.angriff, wurf, basiswuerfel, gegner.verteidigung)):
            gegner.resistenz -= 1

            print("\n")
            print("Du hast die Verteidigung druchbrochen")
            print(f"{gegner.name} resistent - 1")
            print(f"resistenz: {gegner.resistenz}")

        else:
            print("\n")
            print("Du hast die Verteidigung nicht durchbrochen")

        if (gegner.resistenz <= 0):
            gegner.tot = True
            print(f"{gegner.name} ist tot. Du hast gewonnen")
            return

        print(f"{gegner.name} greift an")
        input("Enter zum Weitergehen...")

        wurf = wuerfeln(0, 6)
        basiswuerfel = wuerfeln(0, 6)

        if (test(player.verteidigung, wurf, basiswuerfel, gegner.angriff)):
            print("\n")
            print(f"{gegner.name} hat deine Verteidigung nicht durchbrochen")
        else:
            player.HP -= 1
            print("\n")
            print(f"{gegner.name} hat deine Verteidigung durchbrochen")
            print(f"Deine Vitalität sinkt um 1")
            print(f"Deine Vitalität: {player.HP}")

        if (player.HP <= 0):
            print("\n")
            print(f"Du bist gestorben")
            print(f"---Game Over!---")
            player.tot = True
            return


def test (eigenschaft, wurf, basiswuerfel, gegnerEigenschaft):
    if (eigenschaft + wurf + basiswuerfel >= gegnerEigenschaft):
        return True
    else:
        return False


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
        raise NotImplementedError("")
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
