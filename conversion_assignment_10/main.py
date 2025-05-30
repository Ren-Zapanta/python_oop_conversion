import pygame
import sys
import random
from config import screen, black, file_path
from class_animation_logic import Intro
from class_quiz_loader import QuizLoader
from class_question_display import QuestionDisplay
from class_feedback_handler import FeedbackHandler

pygame.init()

intro = Intro()
loader = QuizLoader("quiz.txt")
questions = loader.load_questions()
random.shuffle(questions)

q_display = QuestionDisplay()
feedback = FeedbackHandler()

current_index = 0
user_answer = ""
run = True

while run:
    screen.fill(black)
    now = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif intro.stage == "waiting_key" and event.type == pygame.KEYDOWN:
            intro.proceed_to_quiz()
        elif intro.stage == "quiz" and event.type == pygame.KEYDOWN:
            key = event.unicode.upper()
            if key in ["A", "B", "C", "D"]:
                user_answer = key
                correct = questions[current_index]["answer"]
                feedback.check_answer(user_answer, correct)

    if intro.stage in ["init", "quiz_init", "waiting_key"]:
        intro.update()

    elif intro.stage == "quiz":
        q_display.display_question(questions[current_index])
        if feedback.feedback:
            feedback.display_feedback()
            if feedback.should_advance():
                feedback.reset_feedback()
                current_index += 1
                q_display.reset()
                if current_index >= len(questions):
                    intro.stage = "score"
        else:
            pass  # waiting for user input

    elif intro.stage == "score":
        final_score_text = f"Quiz completed. Your score: {feedback.score}/{len(questions)}"
        typed, index, t_time = Typewriter.animate(final_score_text, "", 0, pygame.time.get_ticks(), 30)
        screen.blit(pygame.font.SysFont("consolas", 27).render(typed, True, (0, 255, 0)), (100, 600))

    pygame.display.flip()

pygame.quit()
sys.exit()