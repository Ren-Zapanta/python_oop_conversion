import pygame

class PromptManager:
    def __init__(self, font):
        self.prompt_text = "Please enter a question: "
        self.typed_prompt = ''
        self.prompt_index = 0
        self.delay = 45
        self.last_type_time = pygame.time.get_ticks()
        self.font = font

    def set_prompt(self, text):
        self.prompt_text = text
        self.typed_prompt = ''
        self.prompt_index = 0
        self.last_type_time = pygame.time.get_ticks()

    def update(self, screen):
        current_time = pygame.time.get_ticks()
        if self.prompt_index < len(self.prompt_text) and current_time - self.last_type_time > self.delay:
            self.typed_prompt += self.prompt_text[self.prompt_index]
            self.prompt_index += 1
            self.last_type_time = current_time

        prompt_surface = self.font.render(self.typed_prompt, True, (0, 255, 0))
        screen.blit(prompt_surface, (100, 250))