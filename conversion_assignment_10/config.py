import os
import pygame

pygame.init()

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "quiz.txt")

screen_width = 1200
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Quiz Program")

base_font = pygame.font.SysFont("consolas", 27)

green = (0, 255, 0)
black = (0, 0, 0)