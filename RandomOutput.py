import random


class RandomOutput:

    booleans = [True, False]
    elements = ["Water", "Fire", "Dust"]
    rooms = ["Room.enter_chest_room()", "Room.enter_enemy_room()"]

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
        return result
