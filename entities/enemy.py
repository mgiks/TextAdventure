from entity.entity import Entity


class Enemy(Entity):
    def __init__(
        self,
        name,
        hp,
        min_attack,
        max_attack,
        element,
    ):
        super().__init__(name, hp, min_attack, max_attack)
        self.element = element

    def attack(self):
        pass

    def die(self):
        pass
