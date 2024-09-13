import random
from copy import deepcopy
from type_text import type_text
from Map import Map
from RandomOutput import RandomOutput
from Item import Item


class Player:

    stats = {
        "health": 100,
        "min_attack": 10,
        "max_attack": 20,
        "defense": 0,
        "luck": 0,
    }

    coordinates = [(0, 0)]
    inventory = []

    @classmethod
    def print_stats(cls):
        for stat in cls.stats:
            type_text(f"{stat} : {cls.stats[stat]}", 3)

    @classmethod
    def get_stats(cls):
        return cls.stats

    @classmethod
    def print_map(cls):
        coordinate = cls.coordinates[-1]

        map_schema = deepcopy(Map.map_layout)

        map_schema[coordinate[1]][coordinate[0]] = "▽"

        for row in range(len(map_schema)):
            map_schema[row] = " ─ ".join(map_schema[row])
            print(map_schema[row])
            if row != len(map_schema) - 1:
                print(
                    *(
                        "|  "
                        for i in range(
                            len(map_schema[row].replace(" ", "").replace("─", ""))
                        )
                    )
                )

    @classmethod
    def step(cls):
        type_text("\nWhere are you headed?(U,D,L,R): ", 2)
        direction = input().lower()

        match direction:

            case "u":
                y_coordinate = cls.coordinates[-1][1] - 1
                if y_coordinate >= 0:
                    print("Go up")
                    cls.coordinates.append((cls.coordinates[-1][0], y_coordinate))
                else:
                    cls.fail_action()
                    cls.step()

            case "d":
                y_coordinate = cls.coordinates[-1][1] + 1
                if y_coordinate < len(Map.map_layout[0]):
                    print("Go down")
                    cls.coordinates.append((cls.coordinates[-1][0], y_coordinate))
                else:
                    cls.fail_action()
                    cls.step()

            case "l":
                x_coordinate = cls.coordinates[-1][0] - 1
                if x_coordinate >= 0:
                    print("Go left")
                    cls.coordinates.append((x_coordinate, cls.coordinates[-1][1]))
                else:
                    cls.fail_action()
                    cls.step()

            case "r":
                x_coordinate = cls.coordinates[-1][0] + 1
                if x_coordinate < len(Map.map_layout[0]):
                    print("Go right")
                    cls.coordinates.append((x_coordinate, cls.coordinates[-1][1]))
                else:
                    cls.fail_action()
                    cls.step()

    @classmethod
    def attack(cls):
        damage = random.randint(
            Player.get_stats()["min_attack"], Player.get_stats()["max_attack"] + 1
        )
        text = f"You did {damage} damage"

        type_text(text, 3)

        return damage

    @staticmethod
    def flee():
        attempt = RandomOutput.get_random_bool()

        if attempt:
            type_text("You flee the battle!", 3)
        else:
            type_text("You fail to flee", 3)

        return attempt

    @staticmethod
    def fail_action():
        type_text("You can't do that", 2)

    @classmethod
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

    @staticmethod
    def die():
        type_text("\n\nYou are dead...\n", 0)
        type_text("\nDo you want to restart?(Y/N): ", 1)
        choice = input().lower()
        if choice == "y":
            pass
        else:
            print(".....")
