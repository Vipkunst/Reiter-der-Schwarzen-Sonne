class KleidungItem:
    name = ""
    schutzbonus = 0
    art = ""

    def __init__(self, name, schutzbonus, art):
        self.name = name
        self.schutzbonus = schutzbonus
        self.art = art