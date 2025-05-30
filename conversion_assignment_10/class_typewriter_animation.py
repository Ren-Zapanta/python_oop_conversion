import pygame

class Typewriter:
    @staticmethod
    def animate(text, current, index, last_time, delay):
        now = pygame.time.get_ticks()
        if index < len(text) and now - last_time > delay:
            current += text[index]
            index += 1
            last_time = now
        return current, index, last_time