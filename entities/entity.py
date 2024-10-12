from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, name, hp, min_attack, max_attack):
        self.name = name
        self.hp = hp
        self.min_attack = min_attack
        self.max_attack = max_attack

    @abstractmethod
    def attack():
        pass

    @abstractmethod
    def die():
        pass

    @abstractmethod
    def get_stat():
        pass

class Fleeable(ABC):
    @abstractmethod
    def flee():
        pass
