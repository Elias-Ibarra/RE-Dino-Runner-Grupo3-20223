import pygame
from dino_runner.components.cloud import Cloud
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstaclemanager import ObstacleManager
from dino_runner.components import text_utils
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.clouds = Cloud(CLOUD)
        self.running = True
        self.death_count = 0
        self.power_up_manager = PowerUpManager()
        self.high_score = 0
        self.fill_screen_color = False
        self.ing_game_over = pygame.image.load('dino_runner/assets/Other/GameOver.png')
        self.img_corazon = pygame.image.load('dino_runner/assets/Other/SmallHeart.png')
        self.life = 3
        self.dino_dead = pygame.image.load('dino_runner/assets/DinoWallpaper.png')
        self.btn_restart = pygame.image.load('dino_runner/assets/Other/Reset.png')
        self.bg_over = pygame.image.load('dino_runner/assets/bg_game_over.jpeg')
        self.dead = False
    def run(self):
        self.create_components()
        self.playing = True
        self.game_speed = 20
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player, self)


    def draw(self):
        self.number_bg = 0
        self.score()
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.clouds.draw(self.screen,self.game_speed)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed
    
    def execute (self):
        while self.running:
            if not self.playing:
                    
                self.show_menu()
    
    def show_menu(self):
        self.running = True
        fondo=pygame.image.load('dino_runner/assets/fondo_pantalla_dino.jpeg')
        self.screen.fill((255, 255, 255))
        self.screen.blit(fondo,(0,0))
        self.print_menu_elements()
        self.handle_key_events_on_menu()
        pygame.display.update()
    
        
        
        
        

    def print_menu_elements(self):
        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message('Press any Key to start',550, 300,'Comic Sans MS', 38)
            bienvenido, bienvenido_rect = text_utils.get_centered_message('Dino Runner',550, 50,'Comic Sans MS', 50)
            self.screen.blit(text, text_rect)
            self.screen.blit(bienvenido, bienvenido_rect)
            self.blit_corazon('menu')
            self.screen.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 40, 150))
            
        elif self.life <= 0 or self.life == self.death_count:
            text_game_over, text_game_over_rect = text_utils.get_centered_message('internet connection restored',500, 300,'Comic Sans MS', 38)
            self.screen.blit(self.bg_over, (0, 0))
            self.screen.blit(self.ing_game_over, (300, 250))
            self.screen.blit(self.dino_dead, (500, 350))
            self.screen.blit(text_game_over, text_game_over_rect)
            pygame.display.update()
            pygame.time.wait(5000)
            pygame.display.flip()
            self.reset()
            
            
        else:
            text, text_rect = text_utils.get_centered_message('Press any Key to Restart',500, 50,'Comic Sans MS', 50)
            score, score_rect = text_utils.get_centered_message(('Your Score: ' + str(self.points)),200, 250,'Comic Sans MS', 25)
                                                            
            death, death_rect = text_utils.get_centered_message('Death count: ' + str(self.death_count),900, 250,'Comic Sans MS', 25)
            
            self.screen.blit(self.btn_restart, (850, 20))
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, death_rect)
            self.blit_corazon('menu')
            self.screen.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 40, 150))
            
    # usar el reset en la linea
    def reset(self):
        #self.player.reset()
        #self.obstacle_manager.reset()
        #self.power_up_manager.reset()
        #self.clouds.reset()
        self.life = 3
        self.death_count = 0
        #self.game_speed = 20
        self.points = 0
        
    def blit_corazon(self,posicion):
        if posicion == 'menu':
            pos = 450
        elif posicion == 'game':
            pos = 60
        for i in range(self.life):
            self.screen.blit(self.img_corazon, (pos, 500))
            pos += 50

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()
            
            

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        text, text_rect = text_utils.get_score_element(("Score: " + str(self.points)),900, 50,'Comic Sans MS', 20)
        self.screen.blit(text, text_rect)
        self.blit_corazon('game')
        if self.death_count >= 1:
            text2, text_rect2 = text_utils.get_score_element(("High Score: " + str(self.high_score)),900, 500,'Comic Sans MS', 20)
            self.screen.blit(text2, text_rect2)
        self.player.check_invincibility(self.screen)
    def create_components(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.high_score = max(self.points, self.high_score) 