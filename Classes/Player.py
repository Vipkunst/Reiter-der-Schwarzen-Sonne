import Kleidung
import Waffe
from typing import Final

class Player:
    schicksalPunkte = [False] * 14
    staerke = 5
    waffen = [Waffe] * 6
    verteidigung = 0
    MAX_HP: Final[int] = 6
    HP = 6
    Geschick = 5
    MAX_Geschick: Final[int] = 6
    tot = False

    utensilien = [""] * 6

    def __repr__(self):
        return (
            f"Player(schicksalPunkte={self.schicksalPunkte}, "
            f"staerke={self.staerke}, waffen={self.waffen}, "
            f"verteidigung={self.verteidigung}, HP={self.HP}, "
            f"utensilien={self.utensilien})",
            f"slots={self.slots})"
        )

    def upadteHealth(self, damage):
        self.HP += damage
        if (self.HP <= -3):
            self.tot = True
            return self.tot
        return self.HP


    class GetrageneKleidung:
        def __init__(self):
            self.slots = {
                "Kopf": None,
                "Arme": None,
                "Füße": None,
                "Rumpf": None,
                "Beine": None,
            }

        def set_item(self, slot, item):
            if slot not in self.slots:
                raise KeyError(f"'{slot}' is not a valid clothing slot.")
            if not isinstance(item, Kleidung):
                raise ValueError("Item must be an instance of KleidungItem.")
            if item.art != slot:
                raise ValueError(f"Item's 'art' must match the slot '{slot}'.")
            self.slots[slot] = item

        def get_item(self, slot):
                return self.slots.get(slot)

        def __repr__(self):
                return repr(self.slots)
