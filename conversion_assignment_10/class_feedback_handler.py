from class_typewriter_animation import Typewriter
from config import base_font, green, screen
import pygame

class FeedbackHandler:
    def __init__(self):
        self.feedback = ""
        self.feedback_timer = 0
        self.typed = ""
        self.index = 0
        self.time = pygame.time.get_ticks()
        self.delay = 30
        self.score = 0

    def check_answer(self, user_input, correct_answer):
        self.feedback = "You're correct." if user_input == correct_answer else "You are wrong."
        if user_input == correct_answer:
            self.score += 1
        self.feedback_timer = pygame.time.get_ticks()
        self.typed = ""
        self.index = 0
        self.time = pygame.time.get_ticks()

    def display_feedback(self):
        self.typed, self.index, self.time = Typewriter.animate(
            self.feedback, self.typed, self.index, self.time, self.delay
        )
        screen.blit(base_font.render(self.typed, True, green), (100, 500))

    def should_advance(self):
        return pygame.time.get_ticks() - self.feedback_timer > 2000

    def reset_feedback(self):
        self.feedback = ""
        self.typed = ""
        self.index = 0
        self.time = pygame.time.get_ticks()