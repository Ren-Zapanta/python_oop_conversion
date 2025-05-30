import pygame

class DisplayManager:
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Hacker Terminal")
        self.clock = pygame.time.Clock()

    def clear(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        pygame.display.update()
        self.clock.tick(60)
