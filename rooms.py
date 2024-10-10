import helpers.tools as tools
from helpers.random_output import RandomElement
from Player import Player
from Enemy import Enemy
from abc import ABC, abstractmethod


class Room(ABC):
    firstRoomPass = 0
    element = ""

    @abstractmethod
    @staticmethod
    def enter_room(cls):
        pass

    def leave_room(cls):
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


class StartRoom(Room):
    @staticmethod
    def enter_room():
        Player.coordinates = [(0, 0)]
        element = RandomElement.get_random_value()

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

        tools(text, 1)

        Player.step()


class ChestRoom(Room):
    @staticmethod
    def enter_room():
        text = "You enter a chest room"
        tools(text, 2)
        Player.openChest()


class EnemyRoom(Room):
    @classmethod
    def enter_room(cls):
        enemy = Enemy("Fire", "Goblin", 500, 1, 10)

        lost_won = 0
        while Player.get_stats()["health"] > 0 and enemy.enemy_hp > 0:
            choice = input("Attack or Flee [A/F]: ").lower()

            match choice:
                case "a":
                    damage = Player.attack()
                    enemy.enemy_hp -= damage
                    text = f"{enemy.enemy_name} health : {enemy.enemy_hp if enemy.enemy_hp > 0 else 0}"
                    tools(text, 3)

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
                tools(text, 3)

        match lost_won:
            case 1:
                tools(f"You successfully defeat the {enemy.enemy_name}!", 2)
            case 0:
                Player.die()
            case 2:
                pass
