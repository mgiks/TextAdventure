import random
from type_text import type_text


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
