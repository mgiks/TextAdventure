import random
from type_text import type_text


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

        type_text(f"You found {item_quality} {item}", 1)
        type_text(f"Your {item_specialization} has increased by {power}", 1)

        return (item_specialization, power)
