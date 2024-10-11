import random
from helpers.tools import TextTyper
from helpers.random_output import RandomBoolean
from entity.entity import Entity, Fleeable


class Player(Entity, Fleeable):
    def __init__(
        self, name, hp, min_attack, max_attack, defense, luck, coordinates, *items
    ):
        super().__init__(name, hp, min_attack, max_attack)
        self.defense = defense
        self.luck = luck
        self.coordinates = coordinates
        self.inventory = [item for item in items]

    def get_stats(self):
        for stat in (stats := self.__dict__):
            TextTyper.type_text(stats[stat], 1)

    def attack(self):
        damage = random.randint(
            self.min_attack,
            self.max_attack + 1,
        )

        text = f"You did {damage} damage"
        TextTyper.type_text(text, 3)

        return damage

    def flee():
        attempt = RandomBoolean.get_random()

        if attempt:
            TextTyper.type_text("You flee the battle!", 3)
        else:
            TextTyper.type_text("You fail to flee", 3)

        return attempt

    def die():
        text = "You are dead...\n" "Would you like to restart?(Y/N): "
        TextTyper.type_text(text, 1)
        choice = input().lower()

        if choice == "y":
            return 1
        else:
            print(".....")
