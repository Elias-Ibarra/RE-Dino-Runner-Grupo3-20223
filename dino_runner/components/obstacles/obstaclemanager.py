import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

        
    def update(self, game):
        # que salga ramdom un cactus small o large
        objeto= random.randint(1,2)
        if len(self.obstacles) == 0:
            if objeto==0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
                print("small")
            elif objeto==1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
                print("large")
            elif objeto==2:
                self.obstacles.append(Bird(BIRD))  
                print("bird")
              
            
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed , self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(1000)
                game.playing = False
                break

            
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)