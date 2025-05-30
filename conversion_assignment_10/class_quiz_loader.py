import os
class QuizLoader:
    def __init__(self, file_name):
            base_dir = os.path.dirname(os.path.abspath(__file__))

            self.file_path = os.path.join(base_dir, "..", "data", file_name)

    def load_questions(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

        blocks = content.split("\n\n")
        questions = []

        for block in blocks:
            lines = block.strip().split("\n")
            if len(lines) >= 6:
                question = lines[0]
                choices = lines[1:5]
                answer = lines[5].strip().upper()[-1]
                questions.append({"question": question, "choices": choices, "answer": answer})

        return questions
