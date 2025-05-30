import pygame

class InputManager:
    def __init__(self, font):
        self.user_text = ''
        self.font = font

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            elif event.key == pygame.K_RETURN:
                return 'submit'
            else:
                self.user_text += event.unicode
        return None

    def reset(self):
        self.user_text = ''

    def update(self, screen):
        text_surface = self.font.render(self.user_text, True, (0, 255, 0))
        screen.blit(text_surface, (100, 300))

        time_now = pygame.time.get_ticks()
        if (time_now // 500) % 2 == 0:
            text_width = text_surface.get_width()
            cursor_x = 100 + text_width
            cursor_y = 300
            pygame.draw.rect(screen, (0, 255, 0), (cursor_x, cursor_y, 3.5, self.font.get_height()))