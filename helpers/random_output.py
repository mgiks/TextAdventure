import random
from abc import ABC, abstractmethod
from ..item import Item


class RandomChooser(ABC):
    @abstractmethod
    @classmethod
    def get_random(cls):
        pass


class RandomElement(RandomChooser):
    elements = ["Water", "Fire", "Dust"]

    @classmethod
    def get_random(cls):
        result = random.choice(cls.elements)
        return result


class RandomBoolean(RandomChooser):
    @classmethod
    def get_random(cls):
        result = random.choice(0, 1)
        return result


class RandomRoom(RandomChooser):
    @classmethod
    def get_random(cls):
        result = random.choice(cls.rooms)
        return result


class RandomItem(RandomChooser):
    @classmethod
    def get_random(cls):
        item_base = random.choice(Item.get_item_base())
        item_specialization = random.choice(Item.get_item_specialization())
        item_quality = random.choice(Item.get_item_quality())

        return [item_base, item_specialization, item_quality]
