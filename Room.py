import type_text
from RandomOutput import RandomOutput
from Player import Player
from Enemy import Enemy


class Room:

    firstRoomPass = 0
    element = ""

    def enter_random_room():
        room = RandomOutput.get_random_room
        exec(room)

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
