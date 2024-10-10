import random
from copy import deepcopy
from helpers.tools import type_text
from helpers.random_output import RandomOutput
from entity import Entity, Fleeable


class Player(Entity, Fleeable):
    def __init__(
        self, name, health, min_attack, max_attack, defense, luck, coordinates, *items
    ):
        self.name = name
        self.health = health
        self.min_attack = min_attack
        self.max_attack = max_attack
        self.defense = defense
        self.luck = luck
        self.coordinates = coordinates
        self.inventory = [item for item in items]

    def display_stats(cls):
        type_text(f"{stat} : {cls.stats[stat]}", 3)

    def attack(cls):
        damage = random.randint(
            Player.get_stats()["min_attack"], Player.get_stats()["max_attack"] + 1
        )
        text = f"You did {damage} damage"

        type_text(text, 3)

        return damage

    def flee():
        attempt = RandomOutput.get_random_bool()

        if attempt:
            type_text("You flee the battle!", 3)
        else:
            type_text("You fail to flee", 3)

        return attempt

    def open_chest(cls):
        type_text("\nOpen chest?(Y/N): ", 1)
        choice = input().lower()
        chest_has_item = RandomOutput.get_random_bool()

        if choice == "y" and chest_has_item:
            if chest_has_item:
                stat = Item.get_random_item()
                Player.get_stats()[stat[0]] += stat[1]
            else:
                text = "No item..."
                type_text(text, 1)
        else:
            text = "Moving on..."
            type_text(text, 2)

    def die():
        type_text("\n\nYou are dead...\n", 0)
        type_text("\nDo you want to restart?(Y/N): ", 1)
        choice = input().lower()
        if choice == "y":
            pass
        else:
            print(".....")
