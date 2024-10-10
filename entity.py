from abc import ABC, abstractmethod


class Entity(ABC):
    @abstractmethod
    def attack():
        pass

    @abstractmethod
    def die():
        pass


class Fleeable(ABC):
    @abstractmethod
    def flee():
        pass
