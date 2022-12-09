from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
import random

class Cactus(Obstacle):
    large_cactus_y = 305
    small_cactus_y = 330
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        if image == LARGE_CACTUS:
            self.rect.y = self.large_cactus_y
        elif image == SMALL_CACTUS:
            self.rect.y = self.small_cactus_y