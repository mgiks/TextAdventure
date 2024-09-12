import random
import sys
import time
from copy import deepcopy

def type_text(text, speed):
    delay = 0

    match speed:
        case 1:
            delay = 0.05
        case 2:
            delay = 0.035
        case 3:
            delay = 0.02
        case _:
            delay = 0.05

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        if character == " ":
            continue
        time.sleep(delay)

    sys.stdout.write("\n")


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

        # full_map = map_schema.copy()

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
                if y_coordinate >=  0:
                    print("Go up")
                    cls.coordinates.append(
                        (cls.coordinates[-1][0], y_coordinate)
                    )
                else:
                    cls.fail_action()
                    cls.step()

            case "d":
                y_coordinate = cls.coordinates[-1][1] + 1
                if y_coordinate < len(Map.map_layout[0]):
                    print("Go down")
                    cls.coordinates.append(
                        (cls.coordinates[-1][0], y_coordinate)
                    )
                else:
                    cls.fail_action()
                    cls.step()

            case "l":
                x_coordinate = cls.coordinates[-1][0] - 1
                if x_coordinate >= 0:
                    print("Go left")
                    cls.coordinates.append(
                        (x_coordinate, cls.coordinates[-1][1])
                    )
                else:
                    cls.fail_action()
                    cls.step()

            case "r":
                x_coordinate = cls.coordinates[-1][0] + 1
                if x_coordinate < len(Map.map_layout[0]):
                    print("Go right")
                    cls.coordinates.append(
                        (x_coordinate, cls.coordinates[-1][1])
                    )
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

        if choice == "y":
            if chest_has_item:
                return Item.get_random_item()
            else:
                text = "No item..."
                type_text(text, 1)

    @staticmethod
    def die():
        type_text("\n\nYou are dead...\n", 0)
        type_text("\nDo you want to restart?(Y/N): ", 1)
        choice = input().lower()
        if choice == "y":
            pass
        else:
            print(".....")


class Item:

    items = {
        "Strength": ["Sword", "Gauntlet", "Dagger"],
        "Defense": ["Shield", "Helmet", "Chestplate"],
        "Health": ["Herbs", "Bandages", "Health Potion"],
        "General": ["Necklace", "Stone", "Fruit"],
    }

    item_specializations = {
        "Strength": ["min_attack", "max_attack"],
        "Defense": ["defense"],
        "Health": ["health"],
        "General": ["health", "min_attack", "max_attack", "defense", "luck"],
    }

    item_qualities = {
        "Weakened": 1,
        "Common": 5,
        "Rare": 10,
        "Legendary": 100,
    }

    @classmethod
    def get_random_item(cls):
        item_type = random.choice(list(cls.items.keys()))
        item = random.choice(cls.items[item_type])
        item_specialization = random.choice(cls.item_specializations[item_type])
        item_quality = random.choice(list(cls.item_qualities.keys()))
        power = cls.item_qualities[item_quality]

        Player.get_stats()[item_specialization] += power

        type_text(f"You found {item_quality} {item}", 1)
        type_text(f"Your {item_specialization} has increased by {power}", 1)


class Room:

    firstRoomPass = 0
    element = ""

    @staticmethod
    def enter_start_room():
        Player.coordinates = [(0, 0)]
        element = RandomOutput.get_random_element()

        match element:
            case "Water":
                text = (
                    "You wake up to the sound of dripping water from the ceiling.\n"
                    "Your eyes barely adjust to the darkness around you.\n"
                )
            case "Fire":
                text = (
                    "You wake up to the sound of crackling fire.\n"
                    "Your eyes barely adjust to the brightness around you.\n"
                )
            case "Dust":
                text = (
                    "You wake up to the smell of dust.\n" "Your rub your itchy eyes.\n"
                )

        text += (
            "You get up and start planning your next step.\n"
            "You realize there're 4 exists out of this room."
        )

        type_text(text, 1)

        Player.step()

    @staticmethod
    def enter_chest_room():
        text = "You enter a chest room"
        type_text(text, 2)
        Player.openChest()

    @classmethod
    def enter_enemy_room(cls):
        enemy = Enemy("Fire", "Goblin", 500, 1, 10)

        lost_won = 0
        while Player.get_stats()["health"] > 0 and enemy.enemy_hp > 0:
            choice = input("Attack or Flee [A/F]: ").lower()

            match choice:
                case "a":
                    damage = Player.attack()
                    enemy.enemy_hp -= damage
                    text = f"{enemy.enemy_name} health : {enemy.enemy_hp if enemy.enemy_hp > 0 else 0}"
                    type_text(text, 3)

                    if enemy.enemy_hp <= 0:
                        lost_won = 1
                case "f":
                    attempt = Player.flee()
                    if attempt:
                        lost_won = 2
                        break
                case _:
                    Player.fail_action()

            if enemy.enemy_hp > 0:
                enemy_damage = enemy.attack()
                Player.get_stats()["health"] -= enemy_damage
                text = f"Your health = {Player.get_stats()["health"]}"
                type_text(text, 3)

        match lost_won:
            case 1:
                type_text(f"You successfully defeat the {enemy.enemy_name}!", 2)
            case 0:
                Player.die()
            case 2:
                pass

class Map:

    map_layout = [
        ["□"] + ["*"] * 4,
        ["*"] * 5,
        ["*"] * 5,
        ["*"] * 5,
        ["*"] * 5,
    ]

    @classmethod
    def reset_map(cls):
        cls.map_layout = [
            ["*"] * 5,
            ["*"] * 5,
            ["*"] * 5,
            ["*"] * 5,
            ["*"] * 5,
        ]

class Enemy:

    def __init__(
        self,
        element: str,
        enemy_type: str,
        enemy_hp: int,
        enemy_min_attack: int,
        enemy_max_attack: int,
    ):
        self.enemy_name = element + " " + enemy_type
        self.enemy_hp = enemy_hp
        self.enemy_min_attack = enemy_min_attack
        self.enemy_max_attack = enemy_max_attack

    def attack(self):
        enemy_damage = random.randint(self.enemy_min_attack, self.enemy_max_attack + 1)
        text = f"{self.enemy_name} did {enemy_damage} damage"

        type_text(text, 3)

        return enemy_damage


class RandomOutput:

    booleans = [True, False]
    elements = ["Water", "Fire", "Dust"]
    rooms = [Room.enter_chest_room, Room.enter_enemy_room]

    @classmethod
    def get_random_bool(cls):
        result = random.choice(cls.booleans)
        return result

    @classmethod
    def get_random_element(cls):
        result = random.choice(cls.elements)
        return result

    @classmethod
    def get_random_room(cls):
        result = random.choice(cls.rooms)
        result()

while True:
    Player.step()
    Player.print_map()