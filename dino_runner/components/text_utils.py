import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
# importar un font style
# SysFont
#fuente= pygame.font.SysFont("Arial", 20)
#FONT_STYLE= 
black_color = (0, 0, 0)

def get_score_element(points,pos_x,pos_y,font_style,font_size):
    font = pygame.font.SysFont(font_style, font_size)
    text = font.render( str(points), True, black_color )
    text_rect = text.get_rect()
    text_rect.center = (pos_x, pos_y)
    
    return text, text_rect

def get_centered_message (message, width = SCREEN_WIDTH // 2, height = SCREEN_HEIGHT // 2, font_style = "arial", font_size = 30): 
    font = pygame.font.SysFont(font_style, font_size)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    
    return text, text_rect