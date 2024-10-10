import random
from helpers.tools import TextTyper


class Item:
    item_base = [
        "Sword",
        "Gauntlet",
        "Dagger",
        "Shield",
        "Helmet",
        "Chestplate",
        "Herbs",
        "Potion",
        "Necklace",
        "Stone",
        "Fruit",
    ]

    item_specialization = [
        "Strength",
        "Defense",
        "Health",
        "General",
    ]

    item_quality = [
        "Weakened",
        "Common",
        "Rare",
        "Legendary",
    ]

    @classmethod
    def get_item_base(cls):
        return cls.item_base

    @classmethod
    def get_item_specialization(cls):
        return cls.item_specialization

    @classmethod
    def get_item_quality(cls):
        return cls.item_quality
