from helpers.random_output import RandomItem
from helpers.tools import TextTyper

ITEM_BASE_INDEX = 0
ITEM_SPECIALIZATION_INDEX = 1
ITEM_QUALITY_INDEX = 2


class Chest:
    @staticmethod
    def open():
        item_specifications = RandomItem.get_random()

        item_base = item_specifications[ITEM_BASE_INDEX]
        item_specialization = item_specifications[ITEM_SPECIALIZATION_INDEX]
        item_quality = item_specifications[ITEM_QUALITY_INDEX]

        text = f"You have found {item_quality} {item_specialization} {item_base}"

        TextTyper.type_text()
