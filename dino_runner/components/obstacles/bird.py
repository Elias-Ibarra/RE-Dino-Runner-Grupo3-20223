
import random
from dino_runner.components.obstacles.obstacle import Obstacle

from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self,image):
        self.image = BIRD[0]
        self.dino_rect = self.image.get_rect()
        self.type = 0
        super().__init__(image,self.type)
        self.index_fly = 0
        self.rect.y = self.height_bird()
        
        
    def height_bird(self):
        height = random.randint(0, 1)
        if height == 0:
            return 250
        elif height == 1:
            return 300
        
    def draw(self, screen):
        # animacion de vuelo
        if self.index_fly >= 10:
            self.index_fly = 0
        if self.index_fly <= 5:
            self.image = BIRD[0]
        else:
            self.image = BIRD[1]

        screen.blit(self.image, self.rect)
        self.index_fly += 1

        
    

    
        



    
        