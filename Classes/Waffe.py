class Waffe():
    name = ""
    trefferbonus = 0
    anmerkung = ""

    def __init__(self, trefferbonus, anmerkung, angriff):
        self.trefferbonus = trefferbonus
        self.anmerkung = anmerkung
        self.angriff = angriff