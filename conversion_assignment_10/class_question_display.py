import pygame
from class_typewriter_animation import Typewriter
from config import base_font, green, screen

class QuestionDisplay:
    def __init__(self):
        self.typed_q = ""
        self.typed_q_index = 0
        self.typed_q_time = pygame.time.get_ticks()

        self.typed_choices = ["", "", "", ""]
        self.typed_choice_index = [0, 0, 0, 0]
        self.typed_choice_time = [pygame.time.get_ticks()] * 4

        self.delay = 30

    def display_question(self, question_data):
        self.typed_q, self.typed_q_index, self.typed_q_time = Typewriter.animate(
            question_data["question"], self.typed_q, self.typed_q_index, self.typed_q_time, self.delay
        )
        screen.blit(base_font.render(self.typed_q, True, green), (100, 260))

        for i, choice in enumerate(question_data["choices"]):
            self.typed_choices[i], self.typed_choice_index[i], self.typed_choice_time[i] = Typewriter.animate(
                choice, self.typed_choices[i], self.typed_choice_index[i], self.typed_choice_time[i], self.delay
            )
            screen.blit(base_font.render(self.typed_choices[i], True, green), (120, 300 + i * 40))

    def reset(self):
        self.typed_q = ""
        self.typed_q_index = 0
        self.typed_q_time = pygame.time.get_ticks()
        self.typed_choices = ["", "", "", ""]
        self.typed_choice_index = [0, 0, 0, 0]
        self.typed_choice_time = [pygame.time.get_ticks()] * 4