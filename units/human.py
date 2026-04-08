from core.unitsys import Unit
import random

class HumanUnit(Unit):
    name = "Человек"
    id = 0
    texture = "human"
    
    def update(self, world):
        if random.random() < 0.05:
            self.move(random.randint(-1, 1), random.randint(-1, 1))

def register_unit():
    return HumanUnit
