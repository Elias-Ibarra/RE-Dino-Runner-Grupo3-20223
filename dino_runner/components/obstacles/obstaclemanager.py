import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS, DINO_DEAD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        objeto= random.randint(0, 2)
        if len(self.obstacles)==0:
            if objeto == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
                print("small")
            elif objeto == 1:
                self.obstacles.append(Cactus(LARGE_CACTUS))
                print("large")
            elif objeto == 2:
                self.obstacles.append(Bird(BIRD))
                print("bird")        
                
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    game.player.image = DINO_DEAD
                    game.death_count +=1
                    game.life -=1
                    game.playing = False
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
        