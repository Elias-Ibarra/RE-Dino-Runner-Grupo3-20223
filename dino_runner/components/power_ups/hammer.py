from dino_runner.components.power_ups.powerup import PowerUp
from dino_runner.utils.constants import HAMMER, HUAMMER_TYPE


class Hammer(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = HUAMMER_TYPE
        super(Hammer, self).__init__(self.image, self.type)