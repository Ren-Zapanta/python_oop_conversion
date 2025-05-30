import pygame
from class_typewriter_animation import Typewriter
from config import base_font, green, screen, screen_height


class Intro:
    def __init__(self):
        self.stage = "init"
        self.index = 0
        self.typed_text = ""
        self.start_time = pygame.time.get_ticks()
        self.last_type_time = pygame.time.get_ticks()
        self.delay = 45

        self.messages = {
            "init": "System starting, please wait...",
            "quiz_init": "This quiz will determine if you get to live or not.",
            "waiting_key": "Press any key to continue."
        }

    def update(self):
        now = pygame.time.get_ticks()
        current_msg = self.messages[self.stage]

        if now - self.last_type_time > self.delay:
            if self.index < len(current_msg):
                self.typed_text += current_msg[self.index]
                self.index += 1
                self.last_type_time = now
            elif self.stage == "init" and now - self.start_time > 3000:
                self.next_stage("quiz_init", now)
            elif self.stage == "quiz_init" and now - self.start_time > 4500:
                self.next_stage("waiting_key", now)

        if self.stage != "quiz":
            screen.blit(base_font.render(self.typed_text, True, green), (125, screen_height // 2))

    def next_stage(self, stage, now):
        self.stage = stage
        self.typed_text = ""
        self.index = 0
        self.start_time = now

    def proceed_to_quiz(self):
        self.stage = "quiz"
        self.typed_text = ""
        self.index = 0
        self.start_time = pygame.time.get_ticks()