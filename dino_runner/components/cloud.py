import pygame
import random
class Cloud:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 1100
        self.rect.y = random.randint(0, 200)
        self.number_cloud = random.randint(0, 1)
        self.distance_x = random.randint(-75, 75)
        self.distance_y = random.randint(5, 75)
        
    def draw(self, screen, game_speed):
        #dibujar 2 nubes
        if self.number_cloud == 0:
            screen.blit(self.image, self.rect)
        elif self.number_cloud == 1:
            screen.blit(self.image, (self.rect.x, self.rect.y))
            screen.blit(self.image, (self.rect.x + self.distance_x, self.rect.y -self.distance_y))
        
        self.update(game_speed)    
        
    def update(self, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            self.distance_random()
        
    def distance_random(self):
        self.rect.x = random.randint(1100, 1200)
        self.rect.y = random.randint(0, 200)
        self.number_cloud = random.randint(0, 1)
        self.distance_x = random.randint(-75, 75)
        self.distance_y = random.randint(5, 75)
            