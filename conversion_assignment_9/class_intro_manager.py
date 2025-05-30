import pygame

class IntroManager:
    def __init__(self, font):
        self.stage = "init"
        self.texts = {
            "init": "System Initializing...",
            "waiting_key": "Press any key to proceed."
        }
        self.typed_text = ""
        self.index = 0
        self.last_type_time = pygame.time.get_ticks()
        self.delay = 45
        self.start_time = pygame.time.get_ticks()
        self.font = font

    def update(self, screen):
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - self.start_time
        current_text = self.texts[self.stage]

        if self.index < len(current_text) and current_time - self.last_type_time > self.delay:
            self.typed_text += current_text[self.index]
            self.index += 1
            self.last_type_time = current_time

        intro_surface = self.font.render(self.typed_text, True, (0, 255, 0))
        screen.blit(intro_surface, (100, 300))

        if self.stage == "init" and elapsed_time > 3000 and self.index >= len(current_text):
            self.stage = "waiting_key"
            self.typed_text = ""
            self.index = 0
            self.last_type_time = current_time

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and self.stage == "waiting_key":
            self.stage = "done"

    def is_done(self):
        return self.stage == "done"