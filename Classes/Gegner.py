class Gegner:
    HP = 0
    angriff = 0
    verteidigung = 0
    resistenz = 0

    def __init__(self, HP, angriff, verteidigung, resistenz):
        self.HP = HP
        self.angriff = angriff
        self.verteidigung = verteidigung
        self.resistenz = resistenz