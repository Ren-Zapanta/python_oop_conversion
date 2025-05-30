import pygame
import os
from class_intro_manager import IntroManager
from class_prompt_manager import PromptManager
from class_input_manager import InputManager
from class_quiz_manager import QuizManager
from class_display_manager import DisplayManager

def main():
    pygame.init()
    pygame.key.set_repeat(400, 30)
    base_font = pygame.font.SysFont("consolas", 27)
    display = DisplayManager(1200, 720)
    intro = IntroManager(base_font)
    prompt = PromptManager(base_font)
    input_mgr = InputManager(base_font)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "quiz.txt")
    quiz_mgr = QuizManager(file_path)
    running = True

    while running:
        display.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if not intro.is_done():
                intro.handle_event(event)
            else:
                result = input_mgr.handle_event(event)
                if result == 'submit':
                    user_input = input_mgr.user_text
                    input_mgr.reset()
                    response = quiz_mgr.process_input(user_input)
                    if response == "exit":
                        running = False
                    else:
                        prompt.set_prompt(response)

        if not intro.is_done():
            intro.update(display.screen)
        else:
            prompt.update(display.screen)
            input_mgr.update(display.screen)

        display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
