class Gegner:
    name = ""
    HP = 0
    angriff = 0
    verteidigung = 0
    resistenz = 0
    tot = False

    def __init__(self, name, resistenz, angriff, verteidigung):
        self.name = name
        self.angriff = angriff
        self.verteidigung = verteidigung
        self.resistenz = resistenz

